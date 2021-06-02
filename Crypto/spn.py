import os

#  Learn more: https://en.wikipedia.org/wiki/Substitution-permutation_network

# s-box values
#piS = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14, 0]
piS = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]

# s-box with redundant keys piS
#piP = [2, 5, 10, 1, 11, 6, 3, 4, 7, 9, 13, 14, 15, 16, 12, 8]
piP = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]


getBin = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100",
          "1101", "1110", "1111"]


# the binary xor operation on strings
def xor(a, b):
    if a == "1" and b == "1":
        return 0
    elif a == "0" and b == "1":
        return 1
    elif a == "1" and b == "0":
        return 1
    else:
        return 0


def getU(w, k):
    # gets the u value for the SPN

    u = ""

    for i in range(len(w)):
        u += str(xor(w[i], k[i]))

    return u


def getV(u):
    uSplit = [int(u[0:4], 2), int(u[4:8], 2), int(u[8:12], 2), int(u[12:16], 2)]
    newSplit = ""

    for num in uSplit:
        newSplit += getBin[piS[num]]

    return newSplit


def getW(v):
    w = [None] * 16

    for i in range(16):
        # each bit will be saved to word array as per the P-box.
        # ( e.,g 1st bit of v will be value of first bit in Pbox)
        w[piP[i] - 1] = v[i]

    return ''.join(w)


def getCipherText(v, last_key):
    y = ""
    for i in range(len(v)):
        y += str(xor(v[i], last_key[i]))
    return y


def print_block(block, partition_size):
    no_of_blocks = int(len(block) / partition_size)
    for x in range(no_of_blocks):
        temp = block[:partition_size]
        print(f"{''.join(map(str, temp))}", end=" ")
        block = block[partition_size:]


def spn(plain, keys):
    w = plain
    i = 0
    print(f"w0:", end=" ")
    print_block(w, 4)

    last_2_keys = keys[-2:]

    for key in keys[:-2]:
        u = getU(w, key)
        v = getV(u)
        w = getW(v)
        i += 1

        print(f"\nk{i}:", end=" ")
        print_block(key, 4)

        print(f"\nu{i}:", end=" ")
        print_block(u, 4)

        print(f"\nv{i}:", end=" ")
        print_block(v, 4)

        print(f"\nw{i}:", end=" ")
        print_block(w, 4)

    # second last round, P-box is not applied
    u = getU(w, last_2_keys[0])
    v = getV(u)
    i += 1

    print(f"\nk{i}:", end=" ")
    print_block(last_2_keys[0], 4)

    print(f"\nu{i}:", end=" ")
    print_block(u, 4)

    print(f"\nv{i}:", end=" ")
    print_block(v, 4)
    i += 1

    # last round is just the output of second-last round xor last key
    print(f"\nk{i}:", end=" ")
    print_block(last_2_keys[1], 4)

    y = getCipherText(v, last_2_keys[1])

    print(f"\ny :", end=" ")
    print_block(y, 4)


def Str_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


def key_schedule(key):
    k = [key[:16], key[4:20], key[8:24], key[12:28], key[16:32]]
    return k


if __name__ == '__main__':
    #os.system('clear')

    # plain = '0010011010110111'
    # k= '00111010100101001101011000111111'
    # keys = key_schedule(k)
    # spn(plain,keys)

    plain = '0010011010110111'
    k = '00111010100101001101011000111111'

    print ("len of key:",len(k))
    keys = key_schedule(k)
    spn(plain, keys)
