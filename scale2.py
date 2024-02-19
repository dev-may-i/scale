#!/usr/bin/python3
import math
import re

a = 440

t_start = "a"
t_stop  = "g#"

scale = "C_Maj"


### Functions ################################################################

def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))

def d_scales():
  global scale
  t_dict_C_Maj = { "A": 0, "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7, "F": 8, "F#": 9, "G": 10, "G#": 11, 
                   0: "A", 1: "A#", 2: "B", 3: "C", 4: "C#", 5: "D", 6: "D#", 7: "E", 8: "F", 9: "F#", 10: "G", 11: "G#" }

  try:
    match scale:
      case C_Maj:
        return t_dict_C_Maj

  except:
    print("Error: Scale not found. Exiting")
    return False


def calc_tone_no(tone):
  global a
  global scale

  l = len(tone)
  t = [0, 0]

  try:
    t_scale = d_scales()
  except:
    exit(1)

  tone = tone.title()
  if not ( has_numbers(tone) ):
    tone = tone + "5"

  try:
    if ( tone[1] != "#" and tone[1] != "b" ):
      t[0] = int(t_scale[tone[0]])
      t[1] = int(tone[1:]) 
    else:
      t[0] = int(t_scale[tone[:2]])
      t[1] = int(tone[2:])
  except:
    print("Tone " + tone + " not found. Exiting")
    exit(1) 

  out = dict( tone=tone, octave=t[1], step=t[0] )
  return out


def calc_feq(tnr):
#  print("step: " + str(tnr[0]))
#  print("octave: " + str(tnr[1]))

  if tnr[1] >= 5:
    m = a * (tnr[1] - 4)
  else:
    m = a * (2 ** (tnr[1]-5))

  b = 2 ** int(tnr[0])
  c = b ** (1/12)
  f = m * c

  return f

###############################################################################

dsc = d_scales()

x_start = calc_tone_no(t_start)
x_stop = calc_tone_no(t_stop)

start_value = (x_start['octave'] * 8) + x_start['step']
stop_value = (x_stop['octave'] * 8) + x_stop['step']

t_diff = stop_value - start_value
if ( t_diff < 0 ):
  sign = -1
  stop_value = stop_value -1
else:
  sign = 1
  stop_value = stop_value +1

print("Scale: " + scale)
print("start: " + x_start['tone'])
print("stop: " + x_stop['tone'])
print("distance: " + str(t_diff) )
print("")
for s in range(start_value, stop_value, sign):
  octave = int(s/8)
  step   = s % 8
  frequ  = calc_feq([step, octave])
  row = [dsc[step], octave, frequ]
  print("{: <2}{: <3} \tf = {: <20}".format(*row))
