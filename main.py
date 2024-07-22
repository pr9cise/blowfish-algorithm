import encryption
import decryption
choice1 = input("Введіть функцію (1 - шифрування; 2 - дешифрування): ")
if choice1 == "1":
    encryption.encryptionfunction()
elif choice1 == "2":
    decryption.decryptionfunction()
else:
    print("InputError!")