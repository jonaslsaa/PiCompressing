#Made by VOX
#Needs dictonary
import binascii
from math import factorial
from decimal import Decimal, getcontext
import datetime

#STR TO BIN
string = "vox"
binary = bin(int.from_bytes(string.encode(), 'big'))

#BIN TO STR
#n = int(binary, 2)
#n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

#BIN TO DEC
raw_dec = int(binary, 2)

#DEC TO BIN
#binary = bin(dec)

#Pre-Compression
dec = int(raw_dec) #Nothing yet (GOAL: to compress to fewest ammount of bits)


found = False
hop_amount = 100000+len(str(dec))
digits = hop_amount
passed = 0

def calc(seek, buffer_size): #Imports Pi
    pi_dict = open("dict.txt", 'r')
    pi_dict.seek(seek)
    chunk = pi_dict.read( buffer_size )
    pi_dict.close()
    return chunk

str_pi = str(calc(passed, digits))

print("Started: "+str(datetime.datetime.now())+"\n")
print("Digits_in, Search_Status, String_to_Decimal")
print("Searching every "+str(hop_amount)+" digits.")
while(found == False):
    if(str(dec) in str_pi):
        found = True
    print(str(digits)+", "+str(found)+", "+str(dec))
    digits=digits+hop_amount
    str_pi = str(calc(passed, digits))
    passed = passed+hop_amount
encoded = [str_pi.find(str(dec)), str_pi.find(str(dec))+len(str(dec))]
print("\n\nEncode Format: [start_in_pi, end_in_pi] ")
print(string+" to "+str(encoded))

#Get Compression Ration
ec_bin1 = bin(int.from_bytes(str(encoded[0]).encode(), 'big'))
ec_bin2 = bin(int.from_bytes(str(encoded[1]).encode(), 'big'))
ec_length = len(ec_bin1)+len(ec_bin2)
print("\nCompression Ratio: "+str((round(ec_length/len(binary)*100)))+"%")
print("Finished: "+str(datetime.datetime.now())+"\n")
