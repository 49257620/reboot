myname="liuwei"
unset myname
echo $myname
myname="aaaa"
readonly myname
myname="bbbb"
echo $myname 

#!/bin/bash
# author:�����ƴ�ѧ
# url:edu.aliyun.com
echo "Shell ���ݲ���ʵ����";
echo "ִ�е��ļ�����$0";
echo "��һ������Ϊ��$1";
echo "�ڶ�������Ϊ��$2";
echo "����������Ϊ��$3";


#!/bin/bash# author:�����ƴ�ѧ
# url:edu.aliyun.com
echo "Shell ���ݲ���ʵ����";
echo "��һ������Ϊ��$1";
echo "��������Ϊ��$#";
echo "���ݵĲ�����Ϊһ���ַ�����ʾ��$*";


#!/bin/bash
# author:�����ƴ�ѧ
# url:edu.aliyun.com
echo "-- \$* ��ʾ ---"
for i in "$*"; do
echo $i
done
echo "-- \$@ ��ʾ ---"
for i in "$@"; do
echo $i
done

#!/bin/bash
# author:�����ƴ�ѧ
# url:edu.aliyun.com
my_array=(A B "C" D)
echo "��һ��Ԫ��Ϊ: ${my_array[0]}"
echo "�ڶ���Ԫ��Ϊ: ${my_array[1]}"
echo "������Ԫ��Ϊ: ${my_array[2]}"
echo "���ĸ�Ԫ��Ϊ: ${my_array[3]}"

my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "�����Ԫ��Ϊ: ${my_array[*]}"
echo "�����Ԫ��Ϊ: ${my_array[@]}"
echo "����Ԫ�ظ���Ϊ: ${#my_array[*]}"
echo "����Ԫ�ظ���Ϊ: ${#my_array[@]}"


#!/bin/bash
# author:�����ƴ�ѧ
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
echo "a ���� b"
fi
if [ $a != $b ]
then
echo "a ������ b"
fi


#!/bin/bash
# author:�����ƴ�ѧ
# url:edu.aliyun.com
a=10
b=20
if [ $a -eq $b ]
then
   echo "$a -eq $b : a ���� b"
else
   echo "$a -eq $b: a ������ b"
fi
if [ $a -ne $b ]
then
   echo "$a -ne $b: a ������ b"
else
   echo "$a -ne $b : a ���� b"
fi
if [ $a -gt $b ]
then
   echo "$a -gt $b: a ���� b"
else
   echo "$a -gt $b: a ������ b"
fi
if [ $a -lt $b ]
then
   echo "$a -lt $b: a С�� b"
else
   echo "$a -lt $b: a ��С�� b"
fi
if [ $a -ge $b ]
then
   echo "$a -ge $b: a ���ڻ���� b"
else
   echo "$a -ge $b: a С�� b"
fi
if [ $a -le $b ]
then
   echo "$a -le $b: a С�ڻ���� b"
else
   echo "$a -le $b: a ���� b"
fi


#!/bin/bash
# author:�����ƴ�ѧ
# url:edu.aliyun.com
a=10
b=20
if [ $a != $b ]then
echo "$a != $b : a ������ b"
else
echo "$a != $b: a ���� b"
fi
if [ $a -lt 100 -a $b -gt 15 ]
then
echo "$a -lt 100 -a $b -gt 15 : ���� true"
else
echo "$a -lt 100 -a $b -gt 15 : ���� false"
fi
if [ $a -lt 100 -o $b -gt 100 ]
then
echo "$a -lt 100 -o $b -gt 100 : ���� true"
else
echo "$a -lt 100 -o $b -gt 100 : ���� false"
fi
if [ $a -lt 5 -o $b -gt 100 ]
then
echo "$a -lt 100 -o $b -gt 100 : ���� true"
else
echo "$a -lt 100 -o $b -gt 100 : ���� false"
fi


#!/bin/bash
# author:�����ƴ�ѧ
# url:edu.aliyun.com
a=10
b=20
if [[ $a -lt 100 && $b -gt 100 ]]
then
echo "���� true"
else
echo "���� false"
fi
if [[ $a -lt 100 || $b -gt 100 ]]
then
echo "���� true"
else
echo "���� false"
fi


#!/bin/bash
# author:�����ƴ�ѧ
# url:edu.aliyun.com
file="./array001.sh"
if [ -r $file ]
then
echo "�ļ��ɶ�"
else
echo "�ļ����ɶ�"
fi
if [ -w $file ]
then
echo "�ļ���д"
else
echo "�ļ�����д"
fi
if [ -x $file ]
then
echo "�ļ���ִ��"
else
echo "�ļ�����ִ��"
fi
if [ -f $file ]
then
echo "�ļ�Ϊ��ͨ�ļ�"
else
echo "�ļ�Ϊ�����ļ�"
fi
if [ -d $file ]
then
echo "�ļ��Ǹ�Ŀ¼"
else
echo "�ļ����Ǹ�Ŀ¼"
fi
if [ -s $file ]
then
echo "�ļ���Ϊ��"
else
echo "�ļ�Ϊ��"
fi
if [ -e $file ]
then
echo "�ļ�����"
else
echo "�ļ�������"
fi



#!/bin/sh
read name
echo "$name is me"