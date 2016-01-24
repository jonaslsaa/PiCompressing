#Made by VOX

import binascii
from math import factorial
from decimal import Decimal, getcontext
import datetime

def calc(d): #Calculate Pi
    getcontext().prec=d
    n=1
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)                                   
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return pi

#STR TO BIN
string = "vox"
binary = bin(int.from_bytes(string.encode(), 'big'))

#BIN TO STR
#n = int(binary, 2)
#n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

#BIN TO DEC
dec = int(binary, 2)

#DEC TO BIN
#binary = bin(dec)

print("Started: "+str(datetime.datetime.now())+"\n")
print("Digits_in, String_Status, String_to_Decimal")
found = False
hop_amount = 1000+len(str(dec))
digits = hop_amount
str_pi = str(calc(digits))
print("Searching every "+str(hop_amount)+" digits.")
while(found == False):
    passed = digits-hop_amount
    if(str(dec) in str_pi[passed:]):
        found = True
    print(str(digits)+", "+str(found)+", "+str(dec))
    digits=digits+hop_amount
    str_pi = str(calc(digits))
encoded = [str_pi.find(str(dec)), str_pi.find(str(dec))+len(str(dec))]
print("\n\nEncode Format: [start_in_pi, end_in_pi] ")
print(string+" to "+str(encoded))

#Get Compression Ration
ec_bin1 = bin(int.from_bytes(str(encoded[0]).encode(), 'big'))
ec_bin2 = bin(int.from_bytes(str(encoded[1]).encode(), 'big'))
ec_length = len(ec_bin1)+len(ec_bin2)
print("\nCompression Ratio: "+str((round(ec_length/len(binary)*100)))+"%")
print("Finished: "+str(datetime.datetime.now())+"\n")
