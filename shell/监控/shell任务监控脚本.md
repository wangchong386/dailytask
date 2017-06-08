## 主要介绍任务监控
### 1. 短信报警
> 为了更好的检测服务器状态，遇到问题可以发短信和邮件的方式通知运维人员进行处理，与公司运维同事协商开放了短信、邮件两个接口，通过脚本的方式将监控服务器状态，遇到故障后通过脚本方式发送报警。

* 目标分析：
  1、登陆用户数
  2、CPU负载
  3、服务探测
  4、硬盘空间（根分区、应用分区、备份分区）
  5、内存资源
  6. ETL任务
* 脚本：
```
#!/bin/bash
#监控用户登录
Usermonitor ()  {
        LoginUser=`uptime | awk '{print $6}'`
        if [ $LoginUser -ge 2 ]
                then
                        Critical="当前系统登录用户人数超过1人，具体人数为：$LoginUser 个,请确认操作者人数。"
                        status=0
                else
                        echo "loginuser ok"
                        status=1
        fi
}
#监控内存
MemMonitor () {
        MemTotal=`free -m | grep Mem | awk -F: '{print $2}' | awk '{print $1}'`
        MemFree=`free -m | grep cache | awk NR==2 | awk '{print $4}'`
        MemFreeB=`awk 'BEGIN{printf "%.2f%\n",'$MemFree/$MemTotal\*100'}'`
        MemFreeS=`awk 'BEGIN{printf "%.f",'$MemFree/$MemTotal\*100'}'`
        if [ $MemFreeS -lt  10 ]
                then
                        Critical="系统可用内存小于10%，实际可用内存为：$MemFreeB ,请处理。"
                        status=0
                elif [ $MemFreeS -lt 20 ]
                        then
                                Warning="系统可用内存小于20%，实际可用内存为：$MemFreeB ，请查看。"
                                WarningT="内存报警"
                                status=1
                        else
                                echo "Mem OK"
                                status=2
        fi
}
#监控分区空间大小
DiskMonitorG () {
        #根分区
        DiskGB=`df -h | awk NR==2 | awk '{print $5}'`
        DiskGS=`df -h | awk NR==2 | awk '{print $5}' | awk -F% '{print $1}'`
        if [ $DiskGS -gt 90 ]
                then
                        Critical="根分区使用率超过90%，实际已使用 $DiskGB ,请处理。"
                        status=0
                elif [ $DiskGS -gt 80 -a $DiskGS -lt 90 ]
                then
                        Warning="根分区使用率超过80%，实际已使用 $DiskGB , 请查看。"
                        WarningT="根分区报警"
                        status=1
                else
                        echo "DiskGB Ok"
                        status=2
        fi
                }
DiskMonitorA () {
        #应用分区
        ApplyB=`df -h | awk NR==4 | awk '{print $5}'`
        ApplyS=`df -h | awk NR==4 | awk '{print $5}' | awk -F% '{print $1}'`
        if [ $ApplyS -gt 90 ]
                then
                        Critical="应用分区使用率超过90%，实际已使用 $ApplyB ,请处理."
                        status=0
                elif [ $ApplyS -gt 80 -a $ApplyS -lt 90 ]
                then
                        Warning="应用分区使用率超过80%，实际已使用 $ApplyB ，请查看。"
                        WarningT="应用分区报警"
                        status=1
                else
                        echo "Apply ok"
                        status=2
        fi
}
#监控CPU负载
CPULoad () {
        CPULoad1=`uptime | awk '{print $10}' | awk -F. '{print $1}'`
        CPULoad2=`uptime`
        if [ $CPULoad1 -gt 5 ]
                then
                        Critical="CPU负载过高，请即使处理。 $CPULoad2 "
                        status=0
                elif [ $CPULoad1 -gt 3 -a $CPULoad1 -lt 5 ]
                then
                        Warning="CPU负载警告， $Warning "
                        WarningT="CPU负载报警"
                        status=1
                else
                        echo "CPU OK"
                        status=2
        fi
}
#监控服务状态
ServerMonitor () {
#服务状态监控
        timeout=10
        makfails=2
        fails=0
        success=0
        while true
                do
                        /usr/bin/wget --timeout=$timeout --tries=1 http://192.168.20.84/ -q -O /dev/null
                        if [ $? -ne 0 ]
                                then
                                        let fails=fails+1
                                        success=0
                                else
                                        fails=0
                                        let success=1
                        fi
                        if [ $success -ge 1 ]
                                then
                                        exit 0
                        fi
                        if [ $fails -ge 1 ]
                                then
                                        Critical="TMS应用服务出现故障，请紧急处理！"
                                        echo $Critical | mutt -s "服务down" hao.lulu@chinaebi.com
                                        exit -1
                        fi
        done
}
//发送报警短信、报警邮件
for n in Usermonitor MemMonitor DiskMonitorG DiskMonitorA CPULoad ServerMonitor
        do
                $n
                if [ $status -eq 0 ]
                        then
                                curl "http://172.20.36.118/app/tms.do?tranCode=TM0311&content=$Critical"
                        elif [ $status -eq 1 ]
                                then
                                curl "http://172.20.36.118/app/tms.do?tranCode=TM0310&title=$WarningT&content=Warning"
                        else
                                echo "ok"
                fi
done
```