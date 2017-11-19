### 获取log日志
```
#!/bin/sh
dir_name=$(dirname $1)
base_name=$(basename $1)
start_time_file=$(mktemp)
grep -E 'Executing command :' $1 \
    | awk -F ' - ' '{print $2"\t"$1}' | sort -k 1b,1 > $start_time_file
end_time_file=$(mktemp)
cat $start_time_file | awk -F '\t' '{print $1}'  \
    | while read line
      do
          grep " - $line - " $1 \
              | tail -n 1 \
              | awk -F ' - ' '{print $2"\t"$1}'
      done \
    | sort -k 1b,1  > $end_time_file
# ------ test -------
echo ''
echo 'Start'
cat $start_time_file
echo ''
echo 'End'
cat $end_time_file
# ------ test -------
printf "SCRIPT_NAME\tSTART_TIME\tEND_TIME\n" \
    > $dir_name/parsed[$base_name].tsv
join -t $'\t' $start_time_file $end_time_file \
    >> $dir_name/parsed[$base_name].tsv
# ------ test -------
echo ''
cat $dir_name/parsed[$base_name].tsv
# ------ test -------
rm -f $start_time_file $end_time_file
```
