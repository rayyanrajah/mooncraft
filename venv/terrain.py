from PIL import Image

# Open image
img = Image.open("assets/crater2.png")

# Resize smoothly down to 32x32 pixels
result = img.resize((32,32), resample=Image.Resampling.BILINEAR)

result.save('assets/result.png')

pix = result.load()
print(result.size)

terrain_dict = {}

for x in range(-16,16):
    for z in range(-16,16):
        terrain_dict[(x,z)] = pix[x+16,z+16]

print(terrain_dict)