from skimage.io import imread
from skimage.morphology import white_tophat, disk
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label, regionprops_table
from typing import List
from pathlib import Path
import pandas as pd
import numpy as np

from enum import Enum

from napari.types import ImageData, LabelsData, LayerDataTuple

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

def subtract_bg_and_denoise(image: ImageData, background_subtraction_radius: int = 15, particle_radius: int = 5) -> List[LayerDataTuple]:
    """Apply background removal and denoising"""
    footprint = disk(background_subtraction_radius)
    background_subtracted = white_tophat(image, footprint=footprint)
    denoised = gaussian(background_subtracted, sigma=particle_radius)
    
    background_subtracted_layer = (background_subtracted, {}, "image")
    denoised_layer = (denoised, {"colormap": "plasma"}, "image")
    return [background_subtracted_layer, denoised_layer]

def extract_features(image: ImageData, labels: LabelsData, area: bool = True, mean_intensity: bool = True, output_path: str = ''):
    """Measure specified properties"""
    requested_measurements = ['label']
    if area:
        requested_measurements.append('area')
    if mean_intensity:
        requested_measurements.append('mean_intensity')

    regionprops = regionprops_table(image, labels, properties=requested_measurements)
    table = pd.DataFrame(regionprops)
    
    table.to_csv(Path(output_path, 'table.csv'))
    return


