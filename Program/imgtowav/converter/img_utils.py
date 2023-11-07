from PIL import Image

def GetRgbList(path):
    rgb_list = []
    image = Image.open(path).convert('RGB')
    img_height, img_width = image.size

    rgb_list.append(img_height)
    rgb_list.append(img_width)

    for x in range(img_height):
        for y in range(img_width):
            r, g, b = image.getpixel((x, y))
            int_color = int((1<<24)|(r << 16) | (g << 8) | b)
            rgb_list.append(int_color)

    return rgb_list


