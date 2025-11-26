from PIL import Image
import os
import matplotlib.pyplot as plt

def median_cut_quantize(gray_img, colors=16):
    return gray_img.convert("P", palette=Image.ADAPTIVE, colors=colors)\
                   .convert("L")

input_path = r"D:/360ExtremeBrowserDownload/Blur Img 01.png"
os.makedirs("quant_results", exist_ok=True)

img = Image.open(input_path).convert("RGB")

median = median_cut_quantize(gray, 16)
median.save("quant_results/median_cut_gray_16.png")

plt.subplot(1, 4, 3)
plt.title("Median Cut (Gray)")
plt.imshow(median, cmap="gray")
plt.axis("off")
plt.show()
