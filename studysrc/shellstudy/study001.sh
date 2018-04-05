myname="liuwei"
unset myname
echo $myname
myname="aaaa"
readonly myname
myname="bbbb"
echo $myname 

#!/bin/bash
# author:阿里云大学
# url:edu.aliyun.com
echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";


#!/bin/bash# author:阿里云大学
# url:edu.aliyun.com
echo "Shell 传递参数实例！";
echo "第一个参数为：$1";
echo "参数个数为：$#";
echo "传递的参数作为一个字符串显示：$*";


#!/bin/bash
# author:阿里云大学
# url:edu.aliyun.com
echo "-- \$* 演示 ---"
for i in "$*"; do
echo $i
done
echo "-- \$@ 演示 ---"
for i in "$@"; do
echo $i
done

#!/bin/bash
# author:阿里云大学
# url:edu.aliyun.com
my_array=(A B "C" D)
echo "第一个元素为: ${my_array[0]}"
echo "第二个元素为: ${my_array[1]}"
echo "第三个元素为: ${my_array[2]}"
echo "第四个元素为: ${my_array[3]}"

my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组的元素为: ${my_array[*]}"
echo "数组的元素为: ${my_array[@]}"
echo "数组元素个数为: ${#my_array[*]}"
echo "数组元素个数为: ${#my_array[@]}"


#!/bin/bash
# author:阿里云大学
# url:edu.aliyun.com
a=10
b=20
val=`expr $a + $b`
echo "a + b : $val"
val=`expr $a - $b`
echo "a - b : $val"
val=`expr $a \* $b`
echo "a * b : $val"
val=`expr $b / $a`
echo "b / a : $val"
val=`expr $b % $a`
echo "b % a : $val"
if [ $a == $b ]
then
echo "a 等于 b"
fi
if [ $a != $b ]
then
echo "a 不等于 b"
fi


#!/bin/bash
# author:阿里云大学
# url:edu.aliyun.com
a=10
b=20
if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi
if [ $a -ne $b ]
then
   echo "$a -ne $b: a 不等于 b"
else
   echo "$a -ne $b : a 等于 b"
fi
if [ $a -gt $b ]
then
   echo "$a -gt $b: a 大于 b"
else
   echo "$a -gt $b: a 不大于 b"
fi
if [ $a -lt $b ]
then
   echo "$a -lt $b: a 小于 b"
else
   echo "$a -lt $b: a 不小于 b"
fi
if [ $a -ge $b ]
then
   echo "$a -ge $b: a 大于或等于 b"
else
   echo "$a -ge $b: a 小于 b"
fi
if [ $a -le $b ]
then
   echo "$a -le $b: a 小于或等于 b"
else
   echo "$a -le $b: a 大于 b"
fi


#!/bin/bash
# author:阿里云大学
# url:edu.aliyun.com
a=10
b=20
if [ $a != $b ]then
echo "$a != $b : a 不等于 b"
else
echo "$a != $b: a 等于 b"
fi
if [ $a -lt 100 -a $b -gt 15 ]
then
echo "$a -lt 100 -a $b -gt 15 : 返回 true"
else
echo "$a -lt 100 -a $b -gt 15 : 返回 false"
fi
if [ $a -lt 100 -o $b -gt 100 ]
then
echo "$a -lt 100 -o $b -gt 100 : 返回 true"
else
echo "$a -lt 100 -o $b -gt 100 : 返回 false"
fi
if [ $a -lt 5 -o $b -gt 100 ]
then
echo "$a -lt 100 -o $b -gt 100 : 返回 true"
else
echo "$a -lt 100 -o $b -gt 100 : 返回 false"
fi


#!/bin/bash
# author:阿里云大学
# url:edu.aliyun.com
a=10
b=20
if [[ $a -lt 100 && $b -gt 100 ]]
then
echo "返回 true"
else
echo "返回 false"
fi
if [[ $a -lt 100 || $b -gt 100 ]]
then
echo "返回 true"
else
echo "返回 false"
fi


#!/bin/bash
# author:阿里云大学
# url:edu.aliyun.com
file="./array001.sh"
if [ -r $file ]
then
echo "文件可读"
else
echo "文件不可读"
fi
if [ -w $file ]
then
echo "文件可写"
else
echo "文件不可写"
fi
if [ -x $file ]
then
echo "文件可执行"
else
echo "文件不可执行"
fi
if [ -f $file ]
then
echo "文件为普通文件"
else
echo "文件为特殊文件"
fi
if [ -d $file ]
then
echo "文件是个目录"
else
echo "文件不是个目录"
fi
if [ -s $file ]
then
echo "文件不为空"
else
echo "文件为空"
fi
if [ -e $file ]
then
echo "文件存在"
else
echo "文件不存在"
fi



#!/bin/sh
read name
echo "$name is me"