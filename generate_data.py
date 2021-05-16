from phantominator import shepp_logan
from cv2 import imwrite

size_list = [256 * 2 ** i for i in range(3)]

if __name__ == '__main__':
    for size in size_list:
        sl = shepp_logan(size)
        sl = (sl * 255).astype(int)
        imwrite("res/shepp-logan{}.jpg".format(size), sl)


