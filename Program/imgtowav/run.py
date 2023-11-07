import os
import timeit
from pathlib import Path
import converter

def clear_temp():
        dir = r'temp'
        for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

def convert():
        file_path = Path(r'C:\Users\aginity\Desktop\DIPLOM\Program\imgtowav\path.txt').read_text()
        # file_path = r'C:\Users\aginity\Desktop\DIPLOM\tester\WAV\temp_wav.wav'
        extension = os.path.splitext(file_path)[1]
        # clear_temp()
        try:
                if(os.path.exists('storage')):
                        raise ValueError("File doesn`t exist")
                if(extension == ".wav"):
                        
                        converter.WavToImg(file_path)
                elif(extension == ".png" or extension == ".jpg" or extension == ".jpeg"):
                        converter.ImgToWav(file_path)
                else:
                        raise ValueError("Wrong wav file")
        except ValueError as e:
                print(e)

convert() 


