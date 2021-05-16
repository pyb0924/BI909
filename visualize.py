from src import *
from skimage import transform
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('res/shepp-logan256.jpg', cv2.IMREAD_GRAYSCALE)

    radon_image = radon(img)
    reconstruct_image = iradon(radon_image)
    filter_reconstruct_image = iradon(radon_image, filter_name='ramp')
    plt.figure(figsize=(20,10))
    plt.rcParams.update({"font.size": 20})  # 此处必须添加此句代码方可改变标题字体大小
    plt.subplot(241)
    plt.title('original')
    plt.imshow(img, cmap='gray')
    plt.subplot(242)
    plt.title('sinogram')
    plt.imshow(radon_image, cmap='gray')
    plt.subplot(243)
    plt.title('direct\nreconstruction')
    plt.imshow(reconstruct_image, cmap='gray')
    plt.subplot(244)
    plt.title('filter\nreconstruction')
    plt.imshow(filter_reconstruct_image, cmap='gray')

    radon_image = transform.radon(img)
    reconstruct_image = transform.iradon(radon_image, filter_name=None)
    filter_reconstruct_image = transform.iradon(radon_image, filter_name='ramp')

    plt.subplot(246)
    plt.imshow(radon_image, cmap='gray')
    plt.subplot(247)
    plt.imshow(reconstruct_image, cmap='gray')
    plt.subplot(248)
    plt.imshow(filter_reconstruct_image, cmap='gray')

    plt.savefig('../image/sl_model.png')
    plt.show()
