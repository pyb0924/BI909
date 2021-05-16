import time
from pathlib import Path
import pandas as pd
import cv2
from skimage import transform
from src import radon, iradon

if __name__ == '__main__':
    imagePath = Path('res')
    file_name_list = list(imagePath.glob('shepp-logan*.jpg'))

    method_list = ['my algorithm', 'skimage']

    results = []

    for file in file_name_list:
        print('begin ' + str(file))
        for method in method_list:
            if method == 'my algorithm':
                radon1 = radon
                iradon1 = iradon
            else:
                radon1 = transform.radon
                iradon1 = transform.iradon
            img = cv2.imread(str(file), cv2.IMREAD_GRAYSCALE)
            start1 = time.time()
            sinogram = radon1(img)
            end1 = time.time()

            start2 = time.time()
            reconstruct = iradon1(sinogram, filter_name=None)
            end2 = time.time()

            start3 = time.time()
            filtered_reconstruct = iradon1(sinogram, filter_name='ramp')
            end3 = time.time()

            results.append({'file': file, 'method': method, 'radon': end1 - start1, 'iradon(direct)': end2 - start2,
                            'iradon(filter)': end3 - start3})

    df = pd.DataFrame(results).round(2)
    df.set_index(['file', 'method'], inplace=True)
    df.to_csv('time_cost.csv')
