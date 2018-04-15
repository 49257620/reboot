for i in 1 2 3 4 5 6
do
echo "num is ${i}"
done


for file in `ls ./`
do
echo $file
done

for str in "this is a string"
do
echo -e " ${str} \n"
done
