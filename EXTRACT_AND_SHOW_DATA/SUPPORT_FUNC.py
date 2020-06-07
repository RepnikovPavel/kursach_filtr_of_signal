import numpy as np
from numpy.fft import rfft, rfftfreq

def indeces2time(index, RATE):
    tmp_sek = index / RATE

    min = np.uint8(tmp_sek / 60)
    sek = np.uint8(tmp_sek - min * 60)
    ms = np.uint16((tmp_sek - min * 60 - sek) * 1000)

    final_str = str(min) + str(':') + str(sek) + str(':') + str(ms)

    return final_str

def time2indeces(time, RATE):
    m, s, ms = time.split(":")
    t = np.uint8(m) * 60 + np.uint8(s) + np.uint8(ms) / 1000
    index = np.uint32(t * RATE)
    return index

def get_spectrum(x):
    sp = rfft(x)
    print(len(sp))
    return sp
def get_frequencies(x, frame_discritization):
    y= rfftfreq(len(x), 1/frame_discritization)
    print(len(y))
    return y


