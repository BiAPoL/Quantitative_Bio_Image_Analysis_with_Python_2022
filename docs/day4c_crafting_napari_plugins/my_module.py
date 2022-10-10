from skimage.io import imread
from skimage.morphology import white_tophat, disk
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label, regionprops_table
from typing import List
import pandas as pd
import numpy as np
from magicgui.widgets import Select, ListEdit

from enum import Enum

class RefractiveIndex(Enum):
    Oil = 1.515
    Water = 1.33
    Air = 1.0
    
from magicgui.widgets import ComboBox, Container

items = [('box1', ('a', 'b', 'c')), ('box2', ('d', 'e', 'f'))]
widgets = [ComboBox(choices=c, label=l) for l, c in items]
container = Container(widgets=widgets)
    

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

def segment_image_with_features(image: ImageData, requested_measurements: RefractiveIndex) -> LayerDataTuple:
    """Apply thresholding and connected component analysis and measure specified properties"""
    binary = image > threshold_otsu(image)
    labels = label(binary)
    print(requested_measurements)
    # regionprops = regionprops_table(image, labels, properties=requested_measurements)
    # table = pd.DataFrame(regionprops)
    
    layer_properties = {"name": "segmented",
                        # "properties": table,
                       }
    
    labels_layer = (labels, layer_properties, "labels")
    return labels_layer


                    

def extract_features(image, labels, requested_measurements):
    """Measure specified properties"""
    regionprops = regionprops_table(image, labels, properties=requested_measurements)
    table = pd.DataFrame(regionprops)
    return table

def analyse_average_total_intensity(filename, background_subtraction_radius = 15, particle_radius = 5):
    """Load an image, segment objects and measure their mean total intensity."""
    # load data
    image = imread(filename)
    
    denoised = preprocess_image(image, background_subtraction_radius, particle_radius)
    labels = segment_image(denoised)
    
    requested_measurements = ["area", "mean_intensity"]
    table = extract_features(image, labels, requested_measurements)

    # descriptive statistics
    mean_total_intensity = np.mean(table["area"] * table["mean_intensity"])
    
    return mean_total_intensity
