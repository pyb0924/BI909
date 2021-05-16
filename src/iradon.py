import numpy as np
from functools import partial
from scipy.interpolate import interp1d
from src._utils import _iradon_filter


def iradon(radon_image, angles_count=180, filter_name=None, interpolation="linear"):
    """Inverse radon transform.

    Reconstruct an image from the radon transform, using the filtered
    back projection algorithm.

    Parameters
    ----------
    radon_image : ndarray
        Image containing radon transform (sinogram). 
    
    angles_count : array_like, optional
        Number of construction angles (in degrees). Default: linspace(0,180,180)

    filter_name : str, optional
        Filter used in frequency domain filtering. 
        Filters available: ramp, shepp-logan, cosine, hamming, hann.

    interpolation : str, optional
        Interpolation method used in reconstruction. Methods available:
        'linear', 'nearest', and 'cubic' ('cubic' is slow).

    Returns
    -------
    reconstructed : ndarray
        Reconstructed image. 
    """
    theta = np.linspace(0, 180, angles_count, endpoint=False)

    img_shape = radon_image.shape[0]
    output_size = radon_image.shape[0]

    # Do filter
    radon_filtered = _iradon_filter(radon_image, filter_name)

    # Reconstruct image
    reconstructed = np.zeros((output_size, output_size))
    radius = output_size // 2
    xpr, ypr = np.mgrid[:output_size, :output_size] - radius
    x = np.arange(img_shape) - img_shape // 2

    for col, angle in zip(radon_filtered.T, np.deg2rad(theta)):
        t = ypr * np.cos(angle) - xpr * np.sin(angle)
        
        interpolant = interp1d(x, col, kind=interpolation,bounds_error=False, fill_value=0)
        reconstructed += interpolant(t)

    # Background processing
    if filter_name is not None:
        out_reconstruction_circle = (xpr ** 2 + ypr ** 2) >= radius ** 2 - 10 * radius
        reconstructed[out_reconstruction_circle] = 0
    reconstructed[reconstructed < 0] = 0

    print('iRadon transform finished')
    return reconstructed * np.pi / (2 * angles_count)
