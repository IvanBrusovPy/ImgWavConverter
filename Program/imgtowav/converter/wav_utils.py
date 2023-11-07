import wavio
import wave
import struct

from .wav import Wav

def saveWav(temp = Wav):
         wavio.write("temp/temp_wav.wav", temp._hz_list, temp.RATE, sampwidth=4)

def hzFromWav(path):
    hz_list = []

    wave_file = wave.open(path, 'rb')
    byte_height = wave_file.readframes(1)
    height = int.from_bytes(byte_height,'little', signed="True")
    hz_list.append(height)
    byte_width = wave_file.readframes(1)
    width = int.from_bytes(byte_width ,'little', signed="True")
    hz_list.append(width)

    frame_data = wave_file.readframes(height*width)
    format = f"{height*width}i"
    byte_list = list(struct.unpack(format, frame_data))
    for item in byte_list:
        hz_list.append(item)

    return hz_list









