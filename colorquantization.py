import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


original_image = cv2.imread("lena.jpg")
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.axis("off")

