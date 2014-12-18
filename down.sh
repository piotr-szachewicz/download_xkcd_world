for ns in 's' 
do
    for we in 'w'
    do
        for i in {2..22}
        do
            for j in {17}
            do
                wget "http://imgs.xkcd.com/clickdrag/$i$ns$j$we.png"
            done
        done
    done
done
