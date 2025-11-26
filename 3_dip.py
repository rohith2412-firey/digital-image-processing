from matplotlib.image import imread
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import torch
import numpy as np

image = imread("C:/Users/Sri Vishal/Downloads/Background Foreground Blur Img 01.png")
if image.dtype != np.uint8:
    image = (image * 255).astype(np.uint8)

X = image.reshape(-1, 3)
X_t = torch.from_numpy(X).float()

kmeans = KMeans(n_clusters=5, random_state=0, n_init=10)
labels = kmeans.fit_predict(X_t.numpy())

centroids = kmeans.cluster_centers_.astype(np.uint8)
segmented_pixels = centroids[labels]
segmented_img = segmented_pixels.reshape(image.shape)

plt.imshow(segmented_img)
plt.axis("off")
plt.show()

plt.imsave('images/5.jpg', segmented_img)
