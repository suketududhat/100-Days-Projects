import random
import colorgram

colors = colorgram.extract("Intermediate/18 Hirst Painting/image.jpg", 54)

rgb_list = []
for i in range(0, len(colors)):
    current_color = colors[i]
    rgb = current_color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    color_tuple = (r, g, b)
    rgb_list.append(color_tuple)

print(rgb_list)
