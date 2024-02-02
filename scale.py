#!/usr/bin/python3
import math

a = 440
c = 0
d = a
dec = ["0","A","A#","B","C","C#","D","D#","E","F","F#","G","G#","A"]

print ("Step \t" + "Tone \t" + "Freq Hz \t\t" + "Distance multiplier")
print ("------------------------------------------------------------")
for i in range (1, 14):
  if i == 13 :
    print ("------------------------------------------------------------")  
  row = [i, dec[i], d, c]
  print("{: >2} \t{: <3} \t{: <20} \t{: <20}".format(*row))
  b = 2 ** i
  c = b ** (1/12)
  d = a * c
