S = [0 for i in range (256)]

# Key-Scheduling Algorithm (KSA)
# Inisialisasi array S dengan bilangan genap lalu diikuti bilangan ganjil
for i in range(128):
    S[i] = i*2

for i in range(128, 256):
    S[i] = 1 + (i-128)*2

# Modifikasi LFSR
# Inisialisasi LFSR menggunakan kunci masukan pengguna
K = input()
KinB = bytes(K,'utf-8')
arr = []
for byte in KinB:
    arr.append(byte)
    # print(byte)
Ks = []
for i in range(len(arr)):
    temp = arr[len(arr)-1] ^ arr[0]
    Ks.append(arr[0])
    
    for j in range(len(arr)-1):
        arr[j] = arr[j+1]
    arr[len(arr)-1] = (temp)
    # print(arr)

# print("Final KinB: " + str(arr))

j = 0
for i in range(256):
    j = (j + S[i] + arr[i % len(arr)]) % 256
    
    # Swap
    temp = S[i]
    S[i] = S[j]
    S[j] = temp

SC = []
for i in S:
    SC.append(i)

# Enkripsi
def encrypt(plainteks, is_file, filename):
    # Pseudo-random Generation Algorithm (PRGA)
    if(is_file):
        f=open(filename,"rb")
        file_bytes = f.read()
        f.close()
        PinB = file_bytes
    else:
        P = plainteks
        PinB = bytes(P,'utf-8')
    # print(bytes)
    # for byte in bytes:
    #     print(bytes
    
    arrP = []
    for byte in PinB:
        arrP.append(byte)

    arrC = []
    strC = []
    i = 0
    j = 0

    for idx in range(len(arrP)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        
        # Swap
        temp = S[i]
        S[i] = S[j]
        S[j] = temp

        t = (S[i] * S[j]) % 256
        u = S[t]
        C = u ^ arrP[idx]
        # print("Tipe C: " , type(C))
        # print("Tipe u: " , type(u))
        # print("Tipe arrP : " , type(arrP[idx]))
        # C = bytes(str(C),'utf-8')
        # print(C)
        strC.append(chr(C))
        arrC.append(C)

    if(is_file):
        arrCB = bytearray(arrC)    
        # print("Ciperteks= " , ''.join(strC))
        
        w=open("encrypt-results.pdf", "wb")
        w.write(arrCB)
        
        return arrCB

    return arrC

# Dekripsi
def decrypt(arrC):
    # Pseudo-random Generation Algorithm (PRGA)
    # print(arrC)
    # CinB = bytes(C, 'utf-8')
    # arrC = []
    # for byte in CinB:
    #     arrC.append(byte)

    # print(type(arrC))
    is_file = False
    
    if(type(arrC) is bytearray):
        is_file = True
        temp = []
        for byte in arrC:
            temp.append(byte)
        arrC = temp

    arrP = []
    arrPB = []
    i = 0
    j = 0

    # print(CinB)
    
    for idx in range(len(arrC)):
        i = (i + 1) % 256
        j = (j + SC[i]) % 256
        
        # Swap
        temp = SC[i]
        SC[i] = SC[j]
        SC[j] = temp

        t = (SC[i] * SC[j]) % 256
        u = SC[t]
        P = u ^ arrC[idx]
        # print("Tipe C: " , type(C))
        # print("Tipe u: " , type(u))
        # print("Tipe arrP : " , type(arrP[idx]))
        # C = bytes(str(C),'utf-8')
        # print(C)
        arrPB.append(P)
        arrP.append(chr(P))
    
    # print(is_file)
    
    if(is_file):
        arrPB = bytearray(arrPB)  
        w=open("decrypt-results.pdf", "wb")
        w.write(arrPB)
    else:
        print("Plainteks= " ,''.join(arrP))

is_file = False
filename = ""
plainteks = ""
choice = input("Pilih plainteks(A) atau upload file(B)? ")
if(choice == "B"):
    is_file = True
    filename = input("Masukkan nama file: ")
else:
    plainteks = input("Plainteks: ")
    
cipherteks = encrypt(plainteks, is_file, filename)
decrypt(cipherteks)
