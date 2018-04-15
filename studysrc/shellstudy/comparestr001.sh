a='abc'
b='efg'
c=''
if [ a = b ]
then
  echo 'a = b'
else
  echo 'a != b'
fi

if [ $a ]
then
  echo 'a not is null'
else
  echo 'a is null'
fi

if [ $c ]
then
  echo 'c not is null'
else
  echo 'c is null'
fi

if [ -z $c ]
then
 echo 'c len is 0'
else
 echo 'c len is ${#c}'
fi


