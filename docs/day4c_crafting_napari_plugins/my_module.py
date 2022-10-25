from skimage.morphology import white_tophat, disk
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label
import numpy as np

from napari.types import ImageData, LabelsData

# reusable functions

def preprocess_image(image: ImageData, background_subtraction_radius: int = 15, particle_radius: int = 5) -> ImageData:
    """Apply background removal and denoising"""
    footprint = disk(background_subtraction_radius)
    background_subtracted = white_tophat(image, footprint=footprint)
    denoised = gaussian(background_subtracted, sigma=particle_radius)
    return denoised

def segment_image(image: ImageData) -> LabelsData:
    """Apply thresholding and connected component analysis"""
    binary = image > threshold_otsu(image)
    labels = label(binary)
    return labels


