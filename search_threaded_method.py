#Made by VOX
#Needs dictonary
import binascii
from math import factorial
from decimal import Decimal, getcontext
import datetime
import threading

string = "test"
numThreads = 2
threads = []

abc = "abcdefghijklmnopqrstuvwxyz"
dec = ""
for i in string:
    dec=dec+str(abc.find(i)+10)
binary=bin(int.from_bytes(str(dec).encode(), 'big'))

found = False
hop_amount = 100000+len(str(dec))
digits = hop_amount
passed = 0

def calc(seek, buffer_size): #Imports Pi
    pi_dict = open("dict.txt", 'r')
    pi_dict.seek(seek)
    chunk = pi_dict.read( int(buffer_size) )
    pi_dict.close()
    return chunk


print("Started: "+str(datetime.datetime.now())+"\n")
print("Digits_in, Search_Status, String_to_Decimal, Thread")
print("Searching every "+str(hop_amount)+" digits.")

def search(thread, dec):
    while(found == False):
        if(str(dec) in str_pi):
            found = True
        print(str(digits)+", "+str(found)+", "+str(dec)+", Thread-"+str(thread))
        digits=digits+hop_amount
        str_pi = str(calc(passed*thread+thread, digits*thread+thread))
        print(str_pi)
        passed = (passed+hop_amount)*thread
        
thread = 0
while thread < numThreads:
    thread=thread+1
    print("Started Thread-"+str(thread))
    str_pi = str(calc(passed*thread+thread, digits*thread+thread))
    t = threading.Thread(target=calc, args=(thread, dec,))
    threads.append(t)
    t.start()

encoded = [str_pi.find(str(dec)), str_pi.find(str(dec))+len(str(dec))]
print("\n\nEncode Format: [start_in_pi, end_in_pi] ")
print(string+" to "+str(encoded))

#Get Compression Ration
ec_bin1 = bin(int.from_bytes(str(encoded[0]).encode(), 'big'))
ec_bin2 = bin(int.from_bytes(str(encoded[1]).encode(), 'big'))
ec_length = len(ec_bin1)+len(ec_bin2)
print("\nCompression Ratio: "+str((round(ec_length/len(binary)*100)))+"%")
print("Finished: "+str(datetime.datetime.now())+"\n")
