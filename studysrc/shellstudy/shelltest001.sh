a=10
b=20

if test $a -eq $b
then
echo 'yes'
else
echo 'no'
fi

if [ $a -eq $b ]
then
echo 'yes'
else
echo 'no'
fi

a=5
b=6
result=$[a+b] # 注意等号两边不能有空格
echo "result 为： $result"
