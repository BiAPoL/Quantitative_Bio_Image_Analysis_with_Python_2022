from skimage.io import imread
from skimage.morphology import white_tophat, disk
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label, regionprops_table
import pandas as pd
import numpy as np

# reusable functions
def preprocess_image(image, background_subtraction_radius, particle_radius):
    """Apply background removal and denoising"""
    footprint = disk(background_subtraction_radius)
    background_subtracted = white_tophat(image, footprint=footprint)
    denoised = gaussian(background_subtracted, sigma=particle_radius)
    return denoised

def segment_image(image):
    """Apply thresholding and connected component analysis"""
    binary = image > threshold_otsu(image)
    labels = label(binary)
    return labels

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