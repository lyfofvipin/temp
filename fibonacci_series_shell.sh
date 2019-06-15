fibo()
{
    x=$1
    l=0
    m=0
    e=1
    while [ "$x" -gt "0" ]
    do
        echo $l
        e=$(($m+$e))
        m=$l
        l=$e
        x=$(($x-1))
    done
}

fibo 8



# echo "Enter a number : "
# read x
# s=0
# m=0
# l=1
# while [ "$x" -gt "0" ]
# do
#     echo $s
#     l=$(($m+$l))
#     m=$s
#     s=$l
#     x=$(($x-1))
# done