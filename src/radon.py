import numpy as np
from src._utils import getRotated

# TODO reconstruct
def radon(image, thetaNum=180, scanLineNum=None):
    """
    Calculates the radon transform of an image given specified
    projection angles.
    Parameters
    ----------
    image : array_like
        Input image. The rotation axis will be located in the pixel with
        indices ``(image.shape[0] // 2, image.shape[1] // 2)``.
    thetaNum : int, optional
        Number of projection angles (in degrees). If `None`, the value is set to 180.
    scanLineNum : int, optional
        Num of parallel scan line. If `None`, the value is set to min(image.shape)
    Returns
    -------
    radon_image : ndarray
        Radon transform (sinogram).  The tomography rotation axis will lie
        at the pixel index ``radon_image.shape[0] // 2`` along the 0th
        dimension of ``radon_image``.
    References
    ----------
    .. [1] AC Kak, M Slaney, "Principles of Computerized Tomographic
           Imaging", IEEE Press 1988.
    .. [2] B.R. Ramesh, N. Srinivasa, K. Rajgopal, "An Algorithm for Computing
           the Discrete Radon Transform With Some Applications", Proceedings of
           the Fourth IEEE Region 10 International Conference, TENCON '89, 1989
    """
    if image.ndim != 2:
        raise ValueError('The input image must be 2-D')

    theta = np.arange(thetaNum)
    shape_min = min(image.shape)

    center = image.shape[0] // 2
    radon_image = np.zeros((image.shape[0], len(theta)),
                           dtype=image.dtype)

    if scanLineNum is None:
        scanLineNum = shape_min

    # Do radon Transform
    for i, angle in enumerate(np.deg2rad(theta)):
        cos_a, sin_a = np.cos(angle), np.sin(angle)
        R = np.array([[cos_a, -sin_a, -center * (cos_a - sin_a - 1)],
                      [sin_a, cos_a, -center * (cos_a + sin_a - 1)],
                      [0, 0, 1]])
        rotated_data = getRotated(image, R, scanLineNum)
        radon_image[:, i] = rotated_data

    print('Radon transform finished')
    return radon_image
