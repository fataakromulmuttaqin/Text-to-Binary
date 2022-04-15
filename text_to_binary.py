import binascii
import time

print(30*'=')
print("Masukkan teks apapun untuk melihat binary nya.")
print(30*'=')
time.sleep(0.5)

print("Masukkan teks: ")
time.sleep(0.5)
binary = input("==> ")
time.sleep(0.5)

print("Kode Binary mu: ")
print(' '.join(format(ord(x), 'b') for x in binary))
time.sleep(0.5)

time.sleep(1)
print("Terima kasih sudah menggunakan program ini.")
time.sleep(1)
print("Bye")