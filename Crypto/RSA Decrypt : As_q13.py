'''
    This code deals with breaking the RSA.
    Here the assumption is n and e are given public key = [e,n]
    n is very small number and can be factorized easily
    here the user will factorize the n and will find p & q
    as n = p*q
    e.g : 18923 = 1, 127,149,18923
    => p*q = 127 * 149 (so this way calculate the values and enter)
    website ref. provided

'''

# def find_num_with_gcd_1(p):
#     #find e such that gcd(e,phi)=1
#     val = None
#     for i in range(2,p):
#         hcf = find_hcf(i,p)
#         if(hcf == 1):
#             val = i
#             #val = 7 for testing sir's inputs
#             break
#     if val is not None:
#         return val
#
# #find HCF of 2 numbers
# def find_hcf(a,b):
#     small = a
#     hcf = 1
#     if a>b:
#         small = b
#     for i in range(2,small+1):
#         if (a%i == 0 and b%i == 0):
#             hcf =  i
#     return hcf

#find modulus inverse for a with mod value m
def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

#encrypt/decrypt based on key provided
def encrypt_decrypt_rsa(message,key):
    return pow(message,key[0])%key[1]


def driver(input_cipher,p,q,n,e):
    print_final_val ("Refer : https://www.calculatorsoup.com/calculators/math/factors.php")
    print_final_val ("Calculate the factors and provide p and q below")
    # select global values p and q and n
    # p = int(input("Enter a prime number : p : "))
    # q = int(input("Enter a prime number : q : "))
    # n = int(input("Enter value : n : "))
    # e = int(input("Enter value: e : "))
    p=p
    q=q
    n=n
    e=e
    #cipher = int(input("Enter cipher integer val : e : "))
    cipher = input_cipher

    phi_n = (p-1)*(q-1)
    print_final_val ("Totient Function,T =  (p-1)*(q-1) = "+str(phi_n))
    print_final_val ("We know, private key d is calculated as below: (e inverse mod n)")
    print_final_val ("private value -> d = e^-1 mod n")
    d = modInverse(e,phi_n)
    print_final_val ("d = "+str(d))
    print_final_val ("Now we have public and private keys, we have broken it from the value of n given to us")
    public_key = [e,n] #PU
    private_key = [d,n] #PR
    print_final_val ("Public Key : PU : [e,n] : {"+str(e)+","+str(n)+"}")
    print_final_val ("Private Key : PR :[d,n]  {" + str(d) + "," + str(n) + "}")

    print_final_val ("*********Decryption*********")
    print_final_val("Decryption = x = y^d mod n")
    print_final_val("")
    print_final_val ("Cipher text : "+str(cipher))
    retrieved_plain_text = encrypt_decrypt_rsa(cipher, private_key)
    str_val = str(cipher)+"^"+str(private_key[0])+" mod "+str(private_key[1])
    print_final_val("For succesive squaring steps refer: \n https://www.mathcelebrity.com/modexp.php?num=+11%5E13+mod+53&pl=Successive+Squaring")
    print_final_val(str_val)
    print_final_val ("decrypted Message : " + str(retrieved_plain_text))

    print_final_val ("*********Convert to plain english text*********")
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    #eg. 𝐷𝑂𝐺 → 3 × 26ଶ + 14 × 26 + 6 = 2398
    #retrieved_plain_text = [2398,1371,17575,453]
    retrieved_plain_text = [retrieved_plain_text]
    for retrieved_val in retrieved_plain_text:
        retr_string = "retrieved_val : "+str(retrieved_val)
        print_final_val(retr_string)
        print()
        print_final_val("place_3 = "+str(retrieved_val)+" mod 26 ")
        place_3 = int(retrieved_val % 26)
        temp_place = (retrieved_val - place_3)/26
        print_final_val("temp_place = " + str(retrieved_val - place_3) + "/26 ")
        place_2 = int(temp_place % 26)
        print_final_val("place_2 = " + str(temp_place) + " mod 26 ")
        place_1 =int((temp_place - place_2) / 26)
        print_final_val("place_1 = " + str(temp_place - place_2) + "/26 ")
        if place_1 > 25:
            place_1 = place_1%26
        fin_val = str(place_1)+" "+str(place_2)+" "+str(place_3)
        print ()
        #print_final_val (fin_val)
        plain_retrieved = [alphabets[place_1],alphabets[place_2],alphabets[place_3]]
        val1 = "place_1 : "+str(place_1)+" = "+str(plain_retrieved[0])
        val2 = "Place_2 : "+str(place_2)+" = "+str(plain_retrieved[1])
        val3 = "Place_3 : "+str(place_2)+" = "+str(plain_retrieved[2])
        valfin = "plain_retrieved = "+str("".join(plain_retrieved))
        print_final_val (val1)
        print_final_val (val2)
        print_final_val (val3)
        print (valfin)

def print_final_val(x,flag=True):
    if flag:
        print (x)

if __name__ == "__main__":
    '''
        Main function for a RSA - Rivest, Shamir, Adelman Algo
    '''
    p=127
    q = 149
    n = 18923
    e = 1261
    cipher_input = 12423
    driver(int(cipher_input), p, q, n, e)
    #input_data = open('inputfile.txt')
    # for i in input_data:
    #     for j in i.split(" "):
    #         driver(int(j.strip()),p,q,n,e)
