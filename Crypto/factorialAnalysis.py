primes = [2, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
a = 13

print ("Suppose p is a prime and p^a divides n! and p^(a+1) does not divide n!"
       "If [x] = greatest integer not greater than x,"
       "then a = [n/p]+[n/p^2]+[n/p^3]+[n/p^4]+ ....."
       "So the number of zeroes in "+str(a)+"! is the number a such that 5^a divides "+str(a)+"! and 5^(a+1) does not divide !")

print ("Multiples of "+str(a)+"="+"5,10,15,20,....\n\nSo,")
n1=int(a/5)
n2=int(a/25)

print (str(a)+"/5 = n1 = ",n1)
print (str(a)+"/5^2 = n2 = ",n2)
n = n1+n2
print ("Hence, Number of Zeroes in "+str(a)+"! will be : n1 + n2 = ",n)
lst_from_primes = []
for i in primes:
    if i <= a:
        print ("==========================")
        print ("for :",i)
        x=a
        sum = 0
        while (x!=0):
            print(str(x) + "/" + str(i))
            x=int(x/i)
            print ("    =",x)
            sum = sum+x
        print ("sum = ",sum)
        if (i == 2):
            print ("For 2, "+str(sum) +"- No of zeros =  "+str(sum)+" - "+str(n)+" = ",sum-n)
            lst_from_primes.append(sum-n)
        else:
            lst_from_primes.append(sum)

print (lst_from_primes)

print ("Multiplyinh all the below values :")
mult = 1
for i in range(0,len(lst_from_primes)):
    t1 = pow(primes[i],lst_from_primes[i])
    t2 = t1%10
    mult = mult*t2
    print (str(primes[i])+"^"+str(lst_from_primes[i])+"mod 10 = ",t1," mod 10 = ",t2)

print ("\n=>mult =",mult)
last_dig = list(str(mult))
print ("The last digit is : ",last_dig[len(last_dig)-1])
