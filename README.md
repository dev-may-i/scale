<H1>scale.py - Calculate semitone-steps into frequencies (Hz) </H1>

Prerequisite Python Packages: <b>math</b>

Calculate the frequency of each semitone - starting with standard pitch: "A" (@440Hz) - as well as the "distance multiplier" to the next half-tone.

For the calculation the following formular was used: f = a*2^(1/n) <BR>
( https://en.wikipedia.org/wiki/Semitone )

The execution of the scale.py script will produce the following output:
``` 
Step 	Tone 	Freq Hz 		Distance multiplier
------------------------------------------------------------
 1 	A   	440                  	0                   
 2 	A#  	466.1637615180899    	1.0594630943592953  
 3 	B   	493.8833012561241    	1.122462048309373   
 4 	C   	523.2511306011972    	1.189207115002721   
 5 	C#  	554.3652619537442    	1.2599210498948732  
 6 	D   	587.3295358348151    	1.3348398541700344  
 7 	D#  	622.2539674441617    	1.414213562373095   
 8 	E   	659.2551138257398    	1.4983070768766815  
 9 	F   	698.4564628660078    	1.5874010519681994  
10 	F#  	739.9888454232688    	1.681792830507429   
11 	G   	783.9908719634985    	1.7817974362806785  
12 	G#  	830.6093951598903    	1.8877486253633868  
------------------------------------------------------------
13 	A   	880.0                	2.0                 
```
<HR>

<H1>prime.py - A prime number based bechmark test</H1>

This cript will run for 10 seconds (as default) and tries to calculate as much prime numbers as possible. If it gets called with an integer as argument this number will become the new running time (in seconds) <BR>
The purpose of this version will is only to output the amount of found primes within n-seconds - not to print the primes themselves. <BR>
```
Usage: prime.py [seconds]  
``` 
<HR>
