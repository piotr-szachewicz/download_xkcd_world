for ns in 'n' 's' 
do
    for we in 'w' 'e'
    do
        for i in {1..6}
        do
            for j in {1..50}
            do
                wget "http://imgs.xkcd.com/clickdrag/$i$ns$j$we.png"
            done
        done
    done
done
