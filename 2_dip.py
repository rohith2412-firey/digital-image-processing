from PIL import Image
import os
import matplotlib.pyplot as plt

def octree_quantize(gray_img, colors=16):
    return gray_img.quantize(colors=colors, method=2)\
                    .convert("L")

input_path = r"D:/360ExtremeBrowserDownload/Blur Img 01.png"
os.makedirs("quant_results", exist_ok=True)

img = Image.open(input_path).convert("RGB")

octree = octree_quantize(gray, 16)
octree.save("quant_results/octree_gray_16.png")

plt.subplot(1, 4, 4)
plt.title("Octree (Gray)")
plt.imshow(octree, cmap="gray")
plt.axis("off")
plt.show()
