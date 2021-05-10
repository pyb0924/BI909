from phantominator import shepp_logan
import cv2

size_list = [256 * 2 ** i for i in range(3)]

if __name__ == '__main__':
    for size in size_list:
        sl = shepp_logan(size)
        sl = (sl * 255).astype(int)
        cv2.imwrite("res/shepp-logan{}.jpg".format(size), sl)


