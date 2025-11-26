from PIL import Image
import os
import matplotlib.pyplot as plt

def desaturate_gray(img):
    w, h = img.size
    out = Image.new("L", (w, h))  # L = grayscale
    px = img.load()
    opx = out.load()

    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            gray = (r + g + b) // 3       # DESATURATION FORMULA
            opx[x, y] = gray
    return out

input_path = r"D:/360ExtremeBrowserDownload/Blur Img 01.png"
os.makedirs("quant_results", exist_ok=True)

img = Image.open(input_path).convert("RGB")

gray = desaturate_gray(img)
gray.save("quant_results/desaturation_gray.png")

plt.figure(figsize=(12, 4))

plt.subplot(1, 4, 1)
plt.title("Desaturation Gray")
plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.show()
