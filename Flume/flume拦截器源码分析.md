## Flume Interceptor拦截器源码分析
有的时候希望通过Flume将读取的文件再细分存储，比如讲source的数据按照业务类型分开存储，具体一点比如类似：将source中web、wap、media等的内容分开存储；比如丢弃或修改一些数据。这时可以考虑使用拦截器Interceptor。

　　flume通过拦截器实现修改和丢弃事件的功能。拦截器通过定义类继承`org.apache.flume.interceptor.Interceptor`接口来实现。用户可以通过该节点定义规则来修改或者丢弃事件。Flume支持链式拦截，通过在配置中指定构建的拦截器类的名称。在source的配置中，拦截器被指定为一个以空格为间隔的列表。拦截器按照指定的顺序调用。一个拦截器返回的事件列表被传递到链中的下一个拦截器。当一个拦截器要丢弃某些事件时，拦截器只需要在返回事件列表时不返回该事件即可。若拦截器要丢弃所有事件，则其返回一个空的事件列表即可。

　　先解释一下一个重要对象Event：event是flume传输的最小对象，从source获取数据后会先封装成event，然后将event发送到channel，sink从channel拿event消费。event由头`(Map<String, String> headers)`和(body)两部分组成：Headers部分是一个map，body部分可以是String或者byte[]等。其中body部分是真正存放数据的地方，headers部分用于本节所讲的`interceptor`。

### Flume-NG自带拦截器有多种：

　　1、HostInterceptor：使用IP或者hostname拦截；

　　2、TimestampInterceptor：使用时间戳拦截；

　　3、RegexExtractorInterceptor：该拦截器提取正则表达式匹配组，通过使用指定的正则表达式并追加匹配组作为事件的header。它还支持可插拔的serializers用于在添加匹配组作为事件header之前格式化匹配组；

　　4、RegexFilteringInterceptor：该拦截器会选择性地过滤事件。通过以文本的方式解析事件主体，用配置好的规则表达式来匹配文本。提供的正则表达式可以用于包含事件或排除事件；这个和上面的那个区别是这个会按照正则表达式选择性的让event通过，上面那个是提取event.body符合正则的内容作为headers的value。

　　5、StaticInterceptor：可以自定义event的header的value。

　　这些类都在org.apache.flume.interceptor包下。

　　这些interceptor都比较简单我们选取HostInterceptor来讲解interceptor的原理，以及如何自己定制interceptor。

### 这些interceptor都实现了org.apache.flume.interceptor.Interceptor接口，该接口有四个方法以及一个内部接口：

　　1、public void initialize()运行前的初始化，一般不需要实现（上面的几个都没实现这个方法）；

　　2、public Event intercept(Event event)处理单个event；

　　3、public List<Event> intercept(List<Event> events)批量处理event，实际上市循环调用上面的2；

　　4、public void close()可以做一些清理工作，上面几个也都没有实现这个方法；

　　5、 public interface Builder extends Configurable 构建Interceptor对象，外部使用这个Builder来获取Interceptor对象。

　　如果要自己定制，必须要完成上面的__2,3,5__

　　下面，我们来看看org.apache.flume.interceptor.HostInterceptor，其全部代码如下：

```
package org.apache.flume.interceptor;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.List;
import java.util.Map;
import org.apache.flume.Context;
import org.apache.flume.Event;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class HostInterceptor
  implements Interceptor
{
  private static final Logger logger = LoggerFactory.getLogger(HostInterceptor.class);
  private final boolean preserveExisting;
  private final String header;
  private String host = null;
  
  private HostInterceptor(boolean preserveExisting, boolean useIP, String header)
  {
    this.preserveExisting = preserveExisting;
    this.header = header;
    try
    {
      InetAddress addr = InetAddress.getLocalHost();
      if (useIP) {
        this.host = addr.getHostAddress();
      } else {
        this.host = addr.getCanonicalHostName();
      }
    }
    catch (UnknownHostException e)
    {
      logger.warn("Could not get local host address. Exception follows.", e);
    }
  }
  
  public void initialize() {}
  
  public Event intercept(Event event)
  {
    Map<String, String> headers = event.getHeaders();
    if ((this.preserveExisting) && (headers.containsKey(this.header))) {
      return event;
    }
    if (this.host != null) {
      headers.put(this.header, this.host);
    }
    return event;
  }
  
  public List<Event> intercept(List<Event> events)
  {
    for (Event event : events) {
      intercept(event);
    }
    return events;
  }
  
  public void close() {}
  
  public static class Builder
    implements Interceptor.Builder
  {
    private boolean preserveExisting = HostInterceptor.Constants.PRESERVE_DFLT;
    private boolean useIP = HostInterceptor.Constants.USE_IP_DFLT;
    private String header = HostInterceptor.Constants.HOST;
    
    public Interceptor build()
    {
      return new HostInterceptor(this.preserveExisting, this.useIP, this.header, null);
    }
    
    public void configure(Context context)
    {
      this.preserveExisting = context.getBoolean(HostInterceptor.Constants.PRESERVE, Boolean.valueOf(HostInterceptor.Constants.PRESERVE_DFLT)).booleanValue();
      this.useIP = context.getBoolean(HostInterceptor.Constants.USE_IP, Boolean.valueOf(HostInterceptor.Constants.USE_IP_DFLT)).booleanValue();
      this.header = context.getString(HostInterceptor.Constants.HOST_HEADER, HostInterceptor.Constants.HOST);
    }
  }
  
  public static class Constants
  {
    public static String HOST = "host";
    public static String PRESERVE = "preserveExisting";
    public static boolean PRESERVE_DFLT = false;
    public static String USE_IP = "useIP";
    public static boolean USE_IP_DFLT = true;
    public static String HOST_HEADER = "hostHeader";
  }
}

```