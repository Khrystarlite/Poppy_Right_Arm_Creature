from __future__ import print_function
from tqdm import tqdm
import alsaaudio, time, audioop, sys, librosa,json
import numpy as np



# Open the device in nonblocking capture mode. The last argument could
# just as well have been zero for blocking mode. Then we could have
# left out the sleep call in the bottom of the loop
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

# Set attributes: Mono, 8000 Hz, 16 bit little endian samples
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

# The period size controls the internal number of frames per period.
# The significance of this parameter is documented in the ALSA api.
# For our purposes, it is suficcient to know that reads from the device
# will return this many frames. Each frame being 2 bytes long.
# This means that the reads below will return either 320 bytes of data
# or 0 bytes of data. The latter is possible because we are in nonblocking
# mode.
inp.setperiodsize(160)

start = time.time()
data_table = []
for i in tqdm(range(11000),ncols=4):
    # Read data from device
    l,data = inp.read()
    if l:
        # Return the maximum of the absolute value of all samples in a fragment.
        data_table.append(audioop.max(data,2))
       # print audioop.max(data, 2)
    time.sleep(.001)


data_num = np.asarray(data_table)

for x in tqdm(range(len(data_table))):
	print(data_table[x])
