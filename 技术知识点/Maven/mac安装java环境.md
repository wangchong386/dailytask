## 1. mac中配置java开发环境
* 官网中下载[java jdk安装包](http://www.oracle.com/technetwork/java/javase/archive-139210.html)
  选择以前的版本oracle for Archive
* 通过java -version来进行验证:
 ```
 java version "1.7.0_80"
 Java(TM) SE Runtime Environment (build 1.7.0_80-b15)
 Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode)
 ```
* 配置环境变量
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

* 卸载
    * sudo rm -fr /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin
    * sudo rm -fr /Library/PreferencesPanes/JavaControlPanel.prefpane
    * cd /Library/Java/JavaVirtualMachines
    * rm -rf jdk1.7.0_06.jdk
    
 ## 2.安装IntelliJ IDEA
* download IntelliJ IDEA
 
  download link:https://www.jetbrains.com/idea/download/#section=mac
 
  ---> you can choose to download: Ultimate or Community version
* Commonly Install Community version

  Install cracked version Link : http://www.sdifen.com/intellijidea15.html
