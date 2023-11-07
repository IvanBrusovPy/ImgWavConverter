from .img import Image
from .wav import Wav

from .wav_utils import saveWav

def ImgToWav(path):
        temp_img = Image()
        temp_img.openImg(path)
        temp_wav = Wav(temp_img._rgb_list)
        saveWav(temp_wav)

        
  