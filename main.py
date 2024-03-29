import PIL.Image

img_flag = True
path = input("Enter image path here: \n")

try:
	img = PIL.Image.open(path)
	img_flag = True
except:
	print(path, "unable to find img path ");

width, height = img.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))

img = img.convert('P')
#you can pick any character you want
chars = ["^", "V", "~", "7", "I", "Q", "e", ";", "`", "B", ":"]

pixels = img.getdata()
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
#you can change the output.txt to any filename.txt
with open("output.txt", "w") as f:
	f.write(ascii_image)