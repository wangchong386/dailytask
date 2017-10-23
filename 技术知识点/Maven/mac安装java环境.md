## 1. mac中配置java开发环境
* 官网中下载[java jdk安装包](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
* 通过java -version来进行验证


* 卸载
sudo rm -fr /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin
sudo rm -fr /Library/PreferencesPanes/JavaControlPanel.prefpane
cd /Library/Java/JavaVirtualMachines
rm -rf jdk1.7.0_06.jdk
