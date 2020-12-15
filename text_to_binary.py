import binascii
import time

print(30*'=')
print("Enter any text to see its binary form.")
print(30*'=')
time.sleep(0.5)

print("Enter your text: ")
time.sleep(0.5)
binary = input("==> ")
time.sleep(0.5)

print("Your binary code: ")
print(' '.join(format(ord(x), 'b') for x in binary))
time.sleep(0.5)

time.sleep(1)
print("Thanks for using my code.")
time.sleep(1)
print("Bye")