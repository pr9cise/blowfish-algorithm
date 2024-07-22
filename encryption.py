import keygen
import function
def encryptionfunction():
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
    bintext = ""
    for i in range (len(inputtext)):
            binletter = bin(ord(inputtext[i]))[2:]
            fullbinletter = ""
            if len(binletter) < 8:
                m = 8 - len(binletter)
                n = ""
                for j in range(m):
                    n += "0"
                n += binletter
                fullbinletter = n
            else:
                fullbinletter = binletter
            bintext += fullbinletter
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
    for i in range (amount):
        partedtext = textarr[i]
        print(f"partedtext = {partedtext}")
        L = partedtext[:32]
        R = partedtext[32:]
        R1 = ""
        for j in range (16):
            xor1 = int(pbox[j], 2) ^ int(L, 2)
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
        leftxor = int(L, 2) ^ int(pbox[17], 2)
        rightxor = int(R, 2) ^ int(pbox[16], 2)
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
    amount = int(len(resultbin) / 8)
    hexresulttext = ""
    for i in range(amount):
        binhex = ""
        for j in range(8):
            binhex += resultbin[i * 8 + j]
        print(binhex)
        hexoutputtext = hex(int(binhex, 2))[2:]
        fullhex1 = ""
        if len(hexoutputtext) < 2:
            m = 2 - len(hexoutputtext)
            n = ""
            for i in range(m):
                n += "0"
            n += hexoutputtext
            fullhex1 = n
        else:
            fullhex1 = hexoutputtext
        print(fullhex1)
        hexresulttext += fullhex1 + " "
    print(hexresulttext)
    return hexresulttext