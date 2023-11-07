import string
from .img_utils import GetRgbList
from PIL import Image as img

class Image:
    _path: string
    _width: int
    _height: int
    _rgb_list = []

    def openImg(self, path=""):
        self._path = path
        self._rgb_list = GetRgbList(path)
        self._height = self._rgb_list[0]
        self._width = self._rgb_list[1]

    def saveImg(self):
        new_image = img.new("RGB", (self._height, self._width))
        new_pixel_map = new_image.load()
        i = 0

        for x in range(self._height):
            for y in range(self._width):
                 new_pixel_map[x, y] = self._rgb_list[i]
                 i += 1
               
        new_image.save("temp/temp_img.jpg")

    def setRgbList(self, temp_rgb_list):
        self._height = temp_rgb_list[0]
        self._width = temp_rgb_list[1]
        self._rgb_list = temp_rgb_list[2:]


       