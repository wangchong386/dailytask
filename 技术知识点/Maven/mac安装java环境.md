## 1. mac中配置java开发环境
* 官网中下载[java jdk安装包](http://www.oracle.com/technetwork/java/javase/archive-139210.html)
  选择以前的版本oracle for Archive
* 通过java -version来进行验证:
```
java version "1.7.0_80"
Java(TM) SE Runtime Environment (build 1.7.0_80-b15)
Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode)
```
* 
/Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk

* 卸载
    * sudo rm -fr /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin
    * sudo rm -fr /Library/PreferencesPanes/JavaControlPanel.prefpane
    * cd /Library/Java/JavaVirtualMachines
    * rm -rf jdk1.7.0_06.jdk
