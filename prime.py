#!/usr/bin/python3
import time
import sys
import threading

c = 10                          # default: 10 seconds
a = 0                           # amount of found primes

if (len(sys.argv) > 1):
  c = int(sys.argv[1])

print("Running prime number calculator for " + str(c) + " seconds")

##########################################################################

def prime_calculator(e):
  x = 1
  global a                      # prime counter

  while True:
    if not e.is_set():            # run as long as there's no stop-signal
      x += 1                      # current number to test
      for i in range(2, 10):      # test if a modulo of 2,3,4,5,6,7,8,9,10 would result in 0  
        if (x % i) == 0:          # a "rest of 0" indicates that this number is NOT a prime
          break                   # this is not a prime - stop looking further
        else: 
          a += 1                  # we found a new prime, let's increase the counter
    else:
      break

def countdown(c):
  for i in range(c,0,-1):
    print('{}   '.format(i), end='\r')   # mint the tailing <space> chars! This is a 'dirty hack' as of my python 3.10 the "flush" does not work and won't clean the line
    time.sleep(1)


##########################################################################

e = threading.Event()
t1 = threading.Thread(target=prime_calculator, args=(e,) )
t2 = threading.Thread(target=countdown, args=(c,) )

t1.start()                       # start the thread
t2.start()

t1.join(c)                       # wait "c" seconds for the thread to finish
e.set()                          # set event to stop the thread 

t1.join()                        # wait for the thread to finish and clean up
t2.join()

print(str(a) + " Primes calculated in: " + str(c) + " seconds")
