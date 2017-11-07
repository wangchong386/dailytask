## 1. mac configure java development environment
* 官网中download [java jdk installation package](http://www.oracle.com/technetwork/java/javase/archive-139210.html)
  select the previous version:oracle for Archive
* 通过java -version来进行验证:
 ```
 java version "1.7.0_80"
 Java(TM) SE Runtime Environment (build 1.7.0_80-b15)
 Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode)
 ```
* configure environment variable
  vim /etc/profile(该文件为readonly,无读写权限，需要使用sudo chmod赋予读写权限。就可以正常编辑了)
  [sudo chmod a+rwx /etc/profile]
  在文件尾部，添加java路径
     * JAVA_HOME = "/Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk"
     * CLASS_PATH="$JAVA_HOME/lib"
     * PATH=".;$PATH:$JAVA_HOME/bin"
     
  要想马上生效，输入 source /etc/profile
* 验证是否配置成功
  echo $JAVA_HOME
  /Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk

* uninstall:
    * sudo rm -fr /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin
    * sudo rm -fr /Library/PreferencesPanes/JavaControlPanel.prefpane
    * cd /Library/Java/JavaVirtualMachines
    * rm -rf jdk1.7.0_06.jdk
    
 ## 2.Install IntelliJ IDEA
* download IntelliJ IDEA
 
  download link:https://www.jetbrains.com/idea/download/#section=mac
 
  ---> you can choose to download: Ultimate or Community version
* Commonly Install Community version

     * Install cracked version Link : http://www.sdifen.com/intellijidea15.html
  
     * And I can also refer to Link:http://blog.csdn.net/testcs_dn/article/details/51771422
## 3. configure maven
* download maven link:http://maven.apache.org/download.cgi
* configure environment variable:
     * vim /etc/profile, And add the following code
     * export M2_HOME=/Users/wangchong/software/maven/apache-maven-3.5.2
     * export PATH=$PATH:$M2_HOME/bin
* Check if the installation is correct？
```
wangchong$ echo $M2_HOME
/Users/wangchong/software/maven/apache-maven-3.5.2
wangchong$ mvn -version
Apache Maven 3.5.2 (138edd61fd100ec658bfa2d307c43b76940a5d7d; 2017-10-18T15:58:13+08:00)
Maven home: /Users/wangchong09/software/maven/apache-maven-3.5.2
Java version: 1.7.0_80, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk/Contents/Home/jre
Default locale: zh_CN, platform encoding: UTF-8
OS name: "mac os x", version: "10.11.6", arch: "x86_64", family: "mac"
```
