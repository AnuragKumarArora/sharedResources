import numpy as np

def form_equations_matrix(x):
    eq = []
    for i in range(x):
        temp = []
        for j in range(x):
            temp.append(pow((i+1),(j)))
        eq.append(temp)
    return eq

def print_eqns(eqtn,f):

    for i in range(len(f)):
        eq = ""
        eq+= str(f[i])+" = "
        for j in range(len(eqtn[i])):
            eq += str(eqtn[i][j])+"*a"+str(j)+" + "
        print(eq[:-2])

def find_secretmessage_coeff(f):
    eqns = form_equations_matrix(len(f))
    print("*"*30)
    print("Equations formed")
    print_eqns(eqns, f)
    A = np.array(eqns)
    b = np.array(f)
    x = np.linalg.solve(A, b)
    return x

if __name__ == "__main__":
    # setting up the variables

    k = 3
    p = 11
    n = 5
    f = [12, 19, 28] # f(1), f(2) , f(3) ...

    if(not k == len(f)):
        print("ERROR! Length of f should be equal to ",k)
        exit()

    print("===> What is the degree of the polynomial  used for the Share algorithm ? : ",k-1)

    s = find_secretmessage_coeff(f)
    m = s[0]
    print("Secret message : ",m)
    print("Coefficients : ",s[1:])

    print("*" * 30)
    print("\nRemaining f values")
    for fv in range(n-k):
        val = 0
        x = fv+k+1
        for i in range(len(s)):
            val += s[i]*pow(x,i)
        print ("==> f("+str(x)+") : ",val, " = ",val%p, " [ taking mod ", p,"]")
