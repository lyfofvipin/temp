func()
{
    fact=1
    echo "Enter a number : "
    read x
    while [ "$x" -gt "0" ]
    do
        fact=$(($x*$fact))
        x=$(($x-1))
    done
    echo "Factorial is ${fact}."        
}
func