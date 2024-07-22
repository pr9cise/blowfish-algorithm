import keygen
import function
def decryptionfunction():
    inputtext = input("Введіть текст:\n")
    inputkey = input("Введіть ключ:\n")
    inputkey = int(inputkey)
    #checking key for compatibility
    if len(bin(inputkey)[2:]) < 32 or len(bin(inputkey)[2:]) >= 576:
        print("InputKeyError!")
        quit()
    #converting key
    if len(bin(inputkey)[2:]) % 32 != 0:
        n = ""
        for i in range (32 - (len(bin(inputkey)[2:]) % 32)):
            n += "0"
        n += bin(inputkey)[2:]
        fullkey = n
    else:
        fullkey = bin(inputkey)[2:]
    print(fullkey)
    print(len(fullkey))
    #generating pboxes
    pbox = keygen.keygenfunction(fullkey)
    #converting text
    fraction = int(len(inputtext) / 3)
    bintext = ""
    fullbit = ""
    for i in range (fraction):
        hex1 = inputtext[i * 3] + inputtext[i * 3 + 1]
        print(f"hex = {hex1}")
        bit = bin(int(hex1, 16))[2:]
        if len(bit) < 8:
            m = 8 - len(bit)
            n = ""
            for i in range(m):
                n += "0"
            n += bit
            fullbit = n
        else:
            fullbit = bit
        bintext += fullbit
    print(f"bintext\n{bintext}")
    print(len(bintext))
    if len(bintext) % 64 != 0:
        diff = 64 - (len(bintext) % 64)
        for i in range (diff):
            bintext += "0"
    print(bintext)
    print(len(bintext))
    amount = int(len(bintext) / 64)
    textarr = []
    for i in range(amount):
        k0 = ""
        for j in range(64):
            k0 += bintext[i * 64 + j]
        textarr.append(k0)
    print(textarr)
    #actual encryption
    resultbin = ""
    reverse = []
    for i in range (18):
        reverse.append(17-i)
    print(reverse)
    for i in range (amount):
        partedtext = textarr[i]
        print(f"partedtext = {partedtext}")
        L = partedtext[:32]
        R = partedtext[32:]
        R1 = ""
        for j in range (16):
            xor1 = int(pbox[reverse[j]], 2) ^ int(L, 2)
            if len(bin(xor1)[2:]) < 32:
                m = 32 - len(bin(xor1)[2:])
                n = ""
                for j in range(m):
                    n += "0"
                n += bin(xor1)[2:]
                xor1bin = n
            else:
                xor1bin = bin(xor1)[2:]
            print(f"xor1bin = {xor1bin}")
            R1 = xor1bin
            sbox = function.sboxcalculatoins(xor1bin)
            xor2 = int(sbox, 2) ^ int(R, 2)
            if len(bin(xor2)[2:]) < 32:
                m = 32 - len(bin(xor2)[2:])
                n = ""
                for j in range(m):
                    n += "0"
                n += bin(xor2)[2:]
                xor2bin = n
            else:
                xor2bin = bin(xor2)[2:]
            L = xor2bin
            R = R1
        M = L
        L = R
        R = M
        leftxor = int(L, 2) ^ int(pbox[reverse[17]], 2)
        rightxor = int(R, 2) ^ int(pbox[reverse[16]], 2)
        if len(bin(leftxor)[2:]) < 32:
            m = 32 - len(bin(leftxor)[2:])
            n = ""
            for j in range(m):
                n += "0"
            n += bin(leftxor)[2:]
            Lxor = n
        else:
            Lxor = bin(leftxor)[2:]
        if len(bin(rightxor)[2:]) < 32:
            m = 32 - len(bin(rightxor)[2:])
            n = ""
            for j in range(m):
                n += "0"
            n += bin(rightxor)[2:]
            Rxor = n
        else:
            Rxor = bin(rightxor)[2:]
        finalbin = Lxor + Rxor
        resultbin += finalbin
    print(resultbin)
    # converting text from binary to char
    decryptedtext = ""
    fraction = int(len(resultbin) / 8)
    for i in range(fraction):
        letter = ""
        for j in range(8):
            letter += resultbin[i * 8 + j]
        if letter == "00000000":
            break
        decryptedtext += chr(int(letter, 2))
    print(f"decrypted text is \n{decryptedtext}")
    return decryptedtext