## Membuat Belah ketupat bintang
print("Hello ini adalah bentuk belah ketupat")
t = int(5)
for i in range(t):
    for j in range(t,i,-1):
        print(" ",end= "")
    for j in range(2*i+1):
        print("*",end= "")
    print()
for i in range(t-2,-1,-1):
    for j in range(t,i,-1):
        print(" ",end= "")
    for j in range(2*i+1):
        print("*",end= "")
    print()