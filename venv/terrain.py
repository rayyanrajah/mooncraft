from PIL import Image

# Open image
img = Image.open('assets/crater.png')

# Resize down to 32x32 pixels
# result is pixelated image of img
result = img.resize((32,32), resample=Image.Resampling.BILINEAR)

result.save('assets/result.png')

pix = result.load()

terrain_dict = {}

# get RGB value for every pixel in pix
for x in range(-16,16):
    for z in range(-16,16):
        terrain_dict[(x,z)] = pix[x+16,z+16]
