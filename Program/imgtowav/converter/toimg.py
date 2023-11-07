from .img import Image
from .wav_utils import hzFromWav


def WavToImg(path):
     temp_hz_list = hzFromWav(path)
     temp_rgb_list = hzListToRGB(temp_hz_list)
     temp_img = Image()
     temp_img.setRgbList(temp_rgb_list)
     temp_img.saveImg()
   
    
def hzListToRGB (hz_list):
     temp_rgb_list = []
     temp_rgb_list.append(hz_list[0])
     temp_rgb_list.append(hz_list[1])
     for item in hz_list[2:]:
          item = HEX_to_RGB(item)
          temp_rgb_list.append(item)
     return temp_rgb_list


def HEX_to_RGB(hex):
     b = hex & 0xff
     g = (hex >> 8) & 0xff
     r = (hex >> 16) & 0xff
     return r, g, b
