def printFancy(quo,r1,r2,rem,s1,s2,s,t1,t2,t,printgcd):
    if printgcd==True:
        txt="{:^7}|{:^7}|{:^7}|{:^7}||{:^7}|{:^7}|{:^7}"
        print(txt.format(quo,r1,r2,rem,s1,s2,s))
    else:
        txt="{:^7}|{:^7}|{:^7}|{:^7}||{:^7}|{:^7}|{:^7}||{:^7}|{:^7}|{:^7}"
        print(txt.format(quo,r1,r2,rem,s1,s2,s,t1,t2,t))

def printGiven(r1,r2,printgcd):
    if printgcd==True:
        txt="Given the Numbers {0},{1} we find  the gcd as follows:"
        print(txt.format(r1,r2))
    else:
        txt="We find s & t value as follows: \n As per extended euclidean algorithm, \n we assume \n\t s1=1,s2=0 & t1=0,t2=1 \n & calculate \n\t s=s1-s2*q \n\t t=t1-t2*q"
        print(txt)

def gcd(r1,r2,printgcd):
    modulo=r2
    # if r1<r2:
    #     temp=r2
    #     r2=r1
    #     r1=temp
    s1,s2=1,0
    t1,t2=0,1
    printGiven(r1,r2,printgcd)
    print("-"*81)
    printFancy("quo","r1","r2","rem","s1","s2","s","t1","t2","t",printgcd)
    printFancy("-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,printgcd)

    while(True):
        quo=r1//r2
        rem=r1%r2
        #print(r1,"=",r2,"*",quo,"+",rem)
        s=s1-s2*quo
        t=t1-t2*quo
        printFancy(quo,r1,r2,rem,s1,s2,s,t1,t2,t,printgcd)
        s1=s2
        s2=s
        t1=t2
        t2=t
        r1=r2
        r2=rem
        if(r2==0):
            printFancy("x",r1,r2,"x",s1,s2,"x",t1,t2,"x",printgcd)
            printFancy("-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,"-"*7,printgcd)
            printFancy("",r1,"","",s1,"","",t1,"","",printgcd)
            break
    if(r1==1):
        if(s1<0):
            inv=modulo+s1
        else:
            inv=s1
    else:
        inv="Nothing, Because GCD of given number and modulo number is not 1"
    return r1,s1,t1,inv

'''
    Write the input here in line 60 and 61
'''
integer=101  #which ever number inverse is expected
modulo=17  #the mod value
g,s,t,inv=gcd(integer,modulo,printgcd=False) #Everyrhing (Inv, GCD, values of s and t)
#g,s,t,inv=gcd(integer,modulo,printgcd=True)  #only GCD Table And Inverse

print("-"*81)
print("1. GCD of(",integer,",",modulo,") is",g)
print("2. Modulo inverse of",integer,"is",inv)
print("-"*81)
print("3. Finding s & t:")
print("\t Number with",integer,"is",s)
print("\t Number with",modulo,"is",t)
print("-"*81)
