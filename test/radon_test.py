from src import *
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('../res/shepp-logan256.jpg', cv2.IMREAD_GRAYSCALE)

    radon_image = radon(img)
    reconstruct_image = iradon(radon_image,filter_name="ramp")
    plt.subplot(131)
    plt.imshow(img, cmap='gray')
    plt.subplot(132)
    plt.imshow(radon_image, cmap='gray')
    plt.subplot(133)
    plt.imshow(reconstruct_image, cmap='gray')
    plt.show()
