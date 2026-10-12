from PIL import Image, ImageDraw

N = 1024
SS = 4
W = N * SS
img = Image.new("RGBA", (W, W), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

r = 224 * SS
d.rounded_rectangle([0, 0, W - 1, W - 1], radius=r, fill=(255, 255, 255, 255))

top = (37, 99, 235)
bot = (6, 182, 212)
grad = Image.new("RGB", (1, W))
for y in range(W):
    t = y / (W - 1)
    grad.putpixel((0, y), tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
grad = grad.resize((W, W))

mask = Image.new("L", (W, W), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, W - 1, W - 1], radius=r, fill=255)
img.paste(grad, (0, 0), mask)

d = ImageDraw.Draw(img)
white = (255, 255, 255, 255)
keyhole = (30, 27, 75, 255)

sw = 64 * SS
d.arc([372 * SS, 330 * SS, 652 * SS, 640 * SS], start=180, end=360, fill=white, width=sw)

d.rounded_rectangle(
    [292 * SS, 520 * SS, 732 * SS, 830 * SS], radius=40 * SS, fill=white
)

cx, cy, kr = 512 * SS, 636 * SS, 62 * SS
d.ellipse([cx - kr, cy - kr, cx + kr, cy + kr], fill=keyhole)
d.polygon(
    [
        (cx - 34 * SS, cy + 30 * SS),
        (cx + 34 * SS, cy + 30 * SS),
        (cx + 52 * SS, cy + 150 * SS),
        (cx - 52 * SS, cy + 150 * SS),
    ],
    fill=keyhole,
)

img = img.resize((N, N), Image.LANCZOS)
img.save(
    "favicon.ico",
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)
print("wrote favicon.ico", img.size)
