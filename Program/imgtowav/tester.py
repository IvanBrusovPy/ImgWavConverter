import os
import time
from pathlib import Path
import converter

def clear_temp():
        dir = 'temp'
        for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

clear_temp()
aver = 0
file_path = Path('path.txt').read_text()
extension = os.path.splitext(file_path)[1]    
if(extension == ".wav"):
    for i in 10:
        start = time.time()
        converter.WavToImg(file_path)
        end = time.time()
        print(end - start)
elif(extension == ".png" or extension == ".jpg" or extension == ".jpeg"):
    for i in range(0,10):
        start = time.time()
        converter.ImgToWav(file_path)
        end = time.time()
        print(end - start)
        aver += end - start
    print(aver/10)
