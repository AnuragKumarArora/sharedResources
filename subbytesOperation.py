#ref : https://github.com/popcornell/pyGF2/blob/master/pyGF2/gf2_inv.py

def mod2adjust7(val):
    if val < 8:
        return val
    else:
        return val%8


if __name__ == '__main__':
    input_hex = '41'
    modified_polynomial = 'x^8 + x^5 + x^4 + x^3 + 1'

    #hexa = bin(int(input_hex, 16))
    #print(input_hex+" = "+hexa)
    hexa = "{0:08b}".format(int(input_hex, 16))
    print(input_hex + " = " + hexa[0:4]+" "+hexa[4:8])
    poly = ""
    power_of_x =7
    for i in str(hexa):
        if i == '1':
            if power_of_x == 0:
                poly += "1 + "
            else:
                poly += "x^"+str(power_of_x)+" + "
        power_of_x-=1
    poly=poly[0:len(poly)-2]
    print ("Polynomial Obtained : "+poly)

    print ("\nPlease visit to calculate inverse and provide the values below :\n https://mathsci2.appstate.edu/~cookwj/sage/algebra/Euclidean_algorithm-poly.html")
    print ("Input : a(x) = "+modified_polynomial)
    print ("Input : b(x) = "+str(poly))
    print ("go to the bottom and select Ring = Zn and n = 2")
    print ("ENTER THE INVERSE OBTAINED:")

    inverse_polynomial = 'x^7 + x^5 + x^3 + x'
    #inverse_polynomial = 'x^6 + x^3'
    print ("Inverse is : "+inverse_polynomial)
    a = [0]*8
    for bit_val in inverse_polynomial.split('+'):
        temp = bit_val.strip()
        if temp.startswith('x'):
            if temp == 'x':
                a[1] = 1
            else:
                a[int(temp[2])] = 1
        elif temp == '1':
            a[0] =1

    print ("a = a0,a1,a2,a3,a4,a5,a6,a7 = "+ str(a))
    #a=  a0,a1,a2,a3,a4,a5,a6,a7

    c = [1,1,0,0,0,1,1,0]
    #c= c0,c1,c2,c3,c4,c5,c6,c7
    print ("c = c0,c1,c2,c3,c4,c5,c6,c7 = "+ str(c))

    b = []
    #formula_for_b= a[i]+ a[i+4] + a[i+5] + a[i+6] + a[i+7] + c[i]
    for i in range(8):
        temp = a[i]+ a[mod2adjust7(i+4)] + a[mod2adjust7(i+5)] + a[mod2adjust7(i+6)] + a[mod2adjust7(i+7)]  + c[i]
        temp = temp%2
        print ("b("+str(i)+") = a("+str(i)+") + " + "a("+str(mod2adjust7(i+4))+") + " + "a("+str(mod2adjust7(i+5))+") + " + "a("+str(mod2adjust7(i+6))+") + " + "a("+str(mod2adjust7(i+7))+") + " + "c("+str(i)+") mod 2 = "+str(temp))
        b.append(temp)
    b.reverse()
    str1 = ""
    st = str1.join(map(str, b))
    print ("b : "+st[0:4]+" "+st[4:8])

    print ("Hex("+st[0:4]+" "+st[4:8]+") = " + str(hex(int(st[0:4],2)))[2:] + str(hex(int(st[4:8],2)))[2:])


