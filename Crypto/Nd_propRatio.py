# e(a, b) = ( NL(a, b) − 8)/16
# P(x=0) = e + 1/2
from functools import reduce

def calculate_xstar_y(sbox,x_dash,count_of):
    y_dashes = []
    for i in range(0,len(sbox)):
        xi = f'{i:04b}'
        xorval = int(xi, 2)^int(x_dash,2) #x_star in decimal
        xor_of_x = f'{xorval:04b}' #x_star in binary
        y = f'{sbox[i]:04b}' #sbox(x)
        y_star = f'{sbox[xorval]:04b}' #sbox(x)
        y_dash_xor = int(y, 2)^int(y_star,2) #y_star in decimal
        y_dash = f'{y_dash_xor:04b}'  # y_star in binary
        y_dashes.append(y_dash)

        print(" ",xi,"    ", xor_of_x,"    ",x_dash,"       ",y,"      ",y_star,"     ",y_dash)
    calculateCounts(sbox,y_dashes,count_of)

def calculateCounts(sbox,y_dash,count_of):
    counts = []*len(sbox)
    nd_val = None
    print ("\n==========================")
    print ("val    Counts")
    for i in range(0,len(sbox)):
        xi = f'{i:04b}'
        print(xi,"===>",y_dash.count(xi))
        if (xi == count_of):
            nd_val = y_dash.count(xi)
    print ("\n=============================")
    print ("ND Value : ",nd_val)
    calculate_prop_ratio(nd_val)

def calculate_prop_ratio(nd_value):
    print("\n=============================")
    print("Propogation ratio")
    print ("Assuming 2^m = 16")
    print (nd_value,"/16 = ",nd_value/16)

def find_xor(lst):
        return reduce(lambda x,y:x^y,lst)

def count_zeroes(lst):
    count = 0
    for j in lst:
        if j == 0:
            count +=1
    return count

if __name__=='__main__':
    #sbox = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14, 0]
    sbox = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
    input_user = [
        [11,2]
    ]
    for n in input_user:
        x= (f'{n[0]:04b}')
        count_of= (f'{n[1]:04b}')
        print ("input Binary : "+x)
        print ("   X         X*    x_dash(given)    y            y*     y_dash")
        calculate_xstar_y(sbox,x,count_of)

        # print ("NL"+str(n)+" = "+nl)
        # bias = (int(nl) - 8)
        # print("Bias = : ",str(bias)+"/16")
        # print ("===================================================")

    #print_xbox(sbox)
