a=10
b=20
if [ $a -eq $b ]
then
echo 'a = b'
elif [ $a -gt $b ]
then
echo 'a > b'
elif [ $a -lt $b ]
then
echo 'a < b'
fi
