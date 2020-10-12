page = 1
url = f"https://weibo.com/fav?page={page}"

f = open('./test.txt','a')

for i in range(1,375):
    if i==1:
        f.write(f"https://weibo.com/fav?page={i}")
    elif i%5==0:
        f.write(f"\nhttps://weibo.com/fav?page={i}\n")
    else:
        f.write(f"\nhttps://weibo.com/fav?page={i}")

f.close()


f = open('./python2do.txt','a')

for i in range(1,20):
    f.write(f"Chapter {i}\n")

f.close()