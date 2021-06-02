# e(a, b) = ( NL(a, b) − 8)/16
# P(x=0) = e + 1/2
from functools import reduce

def x_box(sbox,X,Y):
    final_list = []
    for i in range(0,len(sbox)):
        xi = f'{i:04b}'
        yi = f'{sbox[i]:04b}'
        temp_list = []
        for i in range(0,len(X)):
            xor_val = None
            if X[i] == '1':
                temp_list.append(int(xi[i]))
            if Y[i] == '1':
                temp_list.append(int(yi[i]))
        xor_val = find_xor(temp_list)
        final_list.append(xor_val)
        print(xi, " XOR ",yi, " = XOR OF ==>",temp_list," = ",xor_val)
    print("FINAL XOR VALS : "+ str(final_list))
    return str(count_zeroes(final_list))

def find_xor(lst):
        return reduce(lambda x,y:x^y,lst)

def count_zeroes(lst):
    count = 0
    for j in lst:
        if j == 0:
            count +=1
    return count

if __name__=='__main__':
    sbox = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14, 0]
    input_user = [
        [9,4],
        [12,13],
        [2,11],
        [15,10]
    ]
    for n in input_user:
        x= (f'{n[0]:04b}')
        y= (f'{n[1]:04b}')
        print ("input Binary : "+x,y)
        print ("  X   XOR   Y                 VALS TO XOR   XOR(X,Y)")
        nl = x_box(sbox,x,y)
        print ("NL"+str(n)+" = "+nl)
        bias = (int(nl) - 8)
        print("Bias = : ",str(bias)+"/16")
        print ("===================================================")

    #print_xbox(sbox)
