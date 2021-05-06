import numpy as np
from scipy import fft, ifft


def getRotatedCoords(x, y, matrix, size):
    src = np.vstack((x, y, np.ones_like(x)))
    dst = np.floor(matrix @ src).astype(int)
    dst[dst > size - 1] = size - 1
    return dst


def getRotated(image, transform_matrix, scanLineNum):
    size = image.shape[0]
    rotated = np.zeros(scanLineNum)

    for scanLine in np.arange(scanLineNum):
        coord_x = np.arange(size)
        coord_y = np.full_like(coord_x, scanLine)
        transformed = getRotatedCoords(coord_x, coord_y, transform_matrix, size)
        rotated[scanLine] = np.mean(image[transformed[0], transformed[1]]) if transformed.size else 0

    return rotated


def _get_fourier_filter(size, filter_name):
    """Construct the Fourier filter.

    This computation lessens artifacts and removes a small bias as
    explained in [1], Chap 3. Equation 61.

    Parameters
    ----------
    size: int
        filter size. Must be even.
    filter_name: str
        Filter used in frequency domain filtering. Filters available:
        ramp, shepp-logan, cosine, hamming, hann. Assign None to use
        no filter.

    Returns
    -------
    fourier_filter: ndarray
        The computed Fourier filter.

    References
    ----------
    .. [1] AC Kak, M Slaney, "Principles of Computerized Tomographic
           Imaging", IEEE Press 1988.

    """
    n = np.concatenate((np.arange(1, size / 2 + 1, 2, dtype=int),
                        np.arange(size / 2 - 1, 0, -2, dtype=int)))
    f = np.zeros(size)
    f[0] = 0.25
    f[1::2] = -1 / (np.pi * n) ** 2

    # Computing the ramp filter from the fourier transform of its
    # frequency domain representation lessens artifacts and removes a
    # small bias as explained in [1], Chap 3. Equation 61
    fourier_filter = 2 * np.real(fft(f))  # ramp filter
    if filter_name == "ramp":
        pass
    elif filter_name == "shepp-logan":
        # Start from first element to avoid divide by zero
        omega = np.pi * fft.fftfreq(size)[1:]
        fourier_filter[1:] *= np.sin(omega) / omega
    elif filter_name == "cosine":
        freq = np.linspace(0, np.pi, size, endpoint=False)
        cosine_filter = fft.fftshift(np.sin(freq))
        fourier_filter *= cosine_filter
    elif filter_name == "hamming":
        fourier_filter *= fft.fftshift(np.hamming(size))
    elif filter_name == "hann":
        fourier_filter *= fft.fftshift(np.hanning(size))
    elif filter_name is None:
        fourier_filter[:] = 1

    return fourier_filter[:, np.newaxis]


# Apply filter in Fourier domain
def _iradon_filter(image, filter_name):
    img_shape = image.shape[0]
    fourier_filter = _get_fourier_filter(img_shape, filter_name)
    projection = fft(image, axis=0) * fourier_filter
    return np.real(ifft(projection, axis=0)[:img_shape, :])
