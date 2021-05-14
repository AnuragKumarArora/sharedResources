def find_num_with_gcd_1(p):
    #find e such that gcd(e,phi)=1
    val = None
    for i in range(2,p):
        hcf = find_hcf(i,p)
        if(hcf == 1):
            val = i
            #val = 7 for testing sir's inputs
            break
    if val is not None:
        return val

#find HCF of 2 numbers
def find_hcf(a,b):
    small = a
    hcf = 1
    if a>b:
        small = b
    for i in range(2,small+1):
        if (a%i == 0 and b%i == 0):
            hcf =  i
    return hcf

#find modulus inverse for a with mod value m
def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

#encrypt/decrypt based on key provided
def encrypt_decrypt_rsa(message,key):
    return pow(message,key[0])%key[1]


if __name__ == "__main__":
    '''
        Main function for a RSA - Rivest, Shamir, Adelman Algo
    '''

    # select global values p and q
    p = input("Enter a prime number : p : ")
    q = input("Enter a prime number : q : ")

    n = p*q
    phi_n = (p-1)*(q-1)
    e = find_num_with_gcd_1(phi_n)
    '''de = 1 mod phi_n 
        d = e^(-1) mod phi_n'''
    d = modInverse(e,phi_n)
    public_key = [e,n] #PU
    private_key = [d,n] #PR
    print "Public Key : PU : {"+str(e)+","+str(n)+"}"
    print "Private Key : PR : {" + str(d) + "," + str(n) + "}"

    print "*********Encryption*********"
    message = input("Enter message to be Encrypted using RSA : ")
    cipher = encrypt_decrypt_rsa(message,public_key)
    print "Encrypted Message : "+str(cipher)

    print "*********Dencryption*********"
    print "Cipher text : "+str(cipher)
    retrieved_plain_text = encrypt_decrypt_rsa(cipher, private_key)
    print "decrypted Message : " + str(retrieved_plain_text)
