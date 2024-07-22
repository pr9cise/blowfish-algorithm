Pbox = ["243f6a88", "85a308d3", "13198a2e",
        "03707344", "a4093822", "299f31d0",
        "082efa98", "ec4e6c89", "452821e6",
        "38d01377", "be5466cf", "34e90c6c",
        "c0ac29b7", "c97c50dd", "3f84d5b5",
        "b5470917", "9216d5d9", "8979fb1b"]
def keygenfunction(Key):
    a = 0
    pboxresult = []
    for i in range (18):
        pboxbin = bin(int(Pbox[i], 16))[2:]
        if len(pboxbin) < 32:
            n = 32 - len(pboxbin)
            m = ""
            for j in range (n):
                m += "0"
            m += pboxbin
            fullpboxbin = m
        else:
            fullpboxbin = pboxbin
        result = bin(int(fullpboxbin, 2) ^ int((Key[a:a + 32]), 2))[2:]
        if len(result) < 32:
            n = 32 - len(result)
            m = ""
            for j in range (n):
                m += "0"
            m += result
            fullresult = m
        else:
            fullresult = result
        print(f"Subkey №{i} = {fullresult}")
        pboxresult.append(fullresult)
        a = (a + 32) % len(Key)
    return pboxresult