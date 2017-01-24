from __future__ import division # the python 3 division - outputs double instead of am int
from __future__ import print_function # the python 3 print function - print()
from tqdm import tqdm # library add a progrees bar for an iterating for loops

from explauto.environment import environments # library environment for modeling implementation

# pypot libraries - the lower level of the poppy framework
import pypot.dynamixel # library to control the servo motors
import pypot.robot  # pypot library for robtic controlss

import time,datetime # librraies to keep track of times
import threading  # library for multithreading workloads

import wave  # library for recording sound and exporting as a wave file
import alsaaudio, audioop, sys, librosa  # library for recording sound

import numpy as np # python's standard linear algebra library: needed for static arrays
import matplotlib.pyplot as plt # library for graphing data
from matplotlib.pyplot import draw, show

import Poppy_Right_Arm as arm



poppy = pypot.robot.from_config(arm.config())  # initiates the poppy object

poppy.start_sync()  # sync the motors so he
time.sleep(2)  # pauses the program 


# for loop primes the motors to be programmed
for m in poppy.motors:
    m.compliant = False
    m.goto_behavior = 'minjerk' # prevents jerky movements



# specific arrays for the rattle shaking movement
data_table = []  # stores the sound features of a recording
spike = [[],[]]  # stores instances of abnormal spikes in sound features and a given timestamp


# activate microphone - A Logitech webcam
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK,device='sysdefault:CARD=C920')
inp.setchannels(2)
inp.setrate(88200)
inp.setformat(alsaaudio.PCM_FORMAT_GSM)
inp.setperiodsize(160)






# audio recording setup
# creates a new wavefile for each run
def outFile():
    return "../out_Data/rattle_{}.wav".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S'))


# function causes the rattle to shake and record audio
def alsa_rattle():
    # set up the wave file
    w = wave.open(outFile(),'w')
    # Open the device in nonblocking capture mode. The last argument could
    # just as well have been zero for blocking mode. Then we could have
    # left out the sleep call in the bottomvim of the loop

    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(44100)

    total = 0
    
    # allows function to run in parallel
    t = threading.Thread(target=arm.rattle_shake)
    t.start()
    timeStart = time.time()
    while t.is_alive():
        timeStop = time.time()
        l,data = inp.read()
        if l:
            # Return the maximum of the absolute value of all samples in a fragment.
            frame = audioop.max(data,2)
            data_table.append(frame)
            total += frame
            ave = total / len(data_table)
            if(len(data_table) > 25) :
                if (frame > ave * 1.34):
                    spike[0].append(timeStop - timeStart)
                    spike[1].append(frame)
            w.writeframes(data)
            # print audioop.max(data, 2)
        time.sleep(.001)
    rest_position()


# execute the rattle command
alsa_rattle()
rest_position()

plt.plot(spike[0],spike[1])
plt.plot(data_table)
show()

