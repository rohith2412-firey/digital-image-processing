from PIL import Image
import os
import matplotlib.pyplot as plt

def uniform_quantize(gray_img, levels=16):
    factor = 255 // (levels - 1)
    w, h = gray_img.size
    out = Image.new("L", (w, h))
    px = gray_img.load()
    opx = out.load()

    for y in range(h):
        for x in range(w):
            g = px[x, y]
            q = round(g / factor) * factor
            opx[x, y] = q
    return out

input_path = r"D:/360ExtremeBrowserDownload/Blur Img 01.png"
os.makedirs("quant_results", exist_ok=True)

img = Image.open(input_path).convert("RGB")

uniform = uniform_quantize(gray, 16)
uniform.save("quant_results/uniform_quantized_16.png")

plt.subplot(1, 4, 2)
plt.title("Uniform (16 levels)")
plt.imshow(uniform, cmap="gray")
plt.axis("off")
plt.show()
