myname="liuwei"
unset myname
echo $myname
myname="aaaa"
readonly myname
myage=30
echo $myname
echo "hello ${myname}"
echo "hello \"${myname}\""
str1="hello"${myname}":"${myage}
echo "length:"${#str1}
string="runoob is a great site"
echo ${string:1:4}
string="runoob is a great company"
echo `expr index "$string" is`
