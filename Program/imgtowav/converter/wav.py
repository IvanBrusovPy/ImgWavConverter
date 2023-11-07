import numpy as np

class Wav:
    RATE = 44100
    _samp_num: int
    _duration: int
    _time_val: int
    _hz_list = []
    
    def __init__(self, hz_list):
        self._samp_num = int(len(hz_list)) 
        self._duration = self._samp_num/self.RATE
        self._time_val = np.arange(self._samp_num)/self.RATE
        self._hz_list = hz_list

   