myfun(){
echo "我的第一个函数"
}

myfun2(){
echo "第一个参数是 $0"
echo "第二个参数是 $1"
echo "第三个参数是 $2"
echo "全部参数是 $@"
echo "参数一共 $#"
return $(($1+$2))
}

myfun3(){

return $(($1+$2))
}

myfun3 1 2 3 4 5
echo "返回值是 $?"
