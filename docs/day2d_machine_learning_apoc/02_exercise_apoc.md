# Exercise: Interactive pixel and object classification

In this exercise we will train two [Random Forest Classifiers](https://en.wikipedia.org/wiki/Random_forest): 
one for pixel classification, and one for classifying segmented objects. 
We will use the napari plugins [napari-accelerated-pixel-and-object-classification](https://www.napari-hub.org/plugins/napari-accelerated-pixel-and-object-classification).

## Getting started

Open a terminal window and activate your conda environment:

```
conda activate devbio-napari-env
```

Afterwards, start up Napari:

```
napari
```

Load the "Blobs" example dataset from the menu `File > Open Sample > clEsperanto > Blobs (from ImageJ)`

![](apoc1.png)

## Pixel classification and Object Segmentation in Napari

For segmenting objects, we can use the Object Segmentation tool in APOC. Under the hood it uses a pixel classifier and [connected component labeling](https://en.wikipedia.org/wiki/Connected-component_labeling). 
The following procedure is also shown in [this video](apoc_object_segmentation.mp4).

Start the object segmentation from the `Tools > Segmentation / Labeling > Object Segmentation (APOC)` menu.

![](apoc2.png)

Add a new labels layer by clicking on this button:
![](apoc3.png)

Change the brush size to a small number such as 2 or 3.
![](apoc4.png)

Click on the `Paint brush` button.
![](apoc5.png)

Start annotating the `background` region where there is no object.
![](apoc6.png)

Increase the label that is drawn by one.
![](apoc7.png)

Draw an annotation within the objects of interest. Draw background and object annotation close by each other. The closer these two annotations are drawn, the smaller is the degree of freedom the computer has when optimizing the model later.
![](apoc8.png)

Within the `Object segmentation` user interface on the right, select the image/channel that should be processed.
![](apoc9.png)

Also select the annotation label image you have just drawn.
![](apoc10.png)

Click on `Train`. A label image should show up.
![](apoc11.png)

If the segmentation works well, consider backing up the `ObjectSegmenter.cl` file that has been saved. If you didn't change the file location before training, it will be located in the folder from where you started napari on the command line.

Close the `Object segmentation` user interface and hide or delete the `Labels` layer with your manual annotation.

## Object classification
Objects can also be classified according to their propeties such as size, intensity and shape.
The following procedure is also shown in [this video](apoc_object_classification.mp4).

Add another label image.
![](apoc21.png)

Rename the label image e.g. to `Label class annotation` to not mix it up with the other.
![](apoc22.png)

Activate the `Brush tool`.
![](apoc23.png)

Put small dots with label `1` into small roundish objects (for training purposes: really just the smaller ones).
![](apoc24.png)

Increase the `label` to `2`.
![](apoc25.png)

Draw a line throught the larger elongated objects in the center of the image.
![](apoc26.png)

Start the object classification tool from the menu `Tools > Segmentation post-processing > Object classification (APOC)`
![](apoc27.png)

In this user-interface, activate the `shape` checkbox.
![](apoc28.png)

Select `image`, `labels` and `annotation` like this:
![](apoc29.png)

Click on `Run`. After a second a new labels layer with brown / blue annotated objects should appear. Some larger round objects will be blue unintentionally.
![](apoc30.png)

Hide the newly created classification layer.
![](apoc31.png)

Select your annotation layer.
![](apoc32.png)

Annotate some more roundish objects, this time the larger ones.
![](apoc33.png)

Train the classifier again.
![](apoc34.png)

If you are happy with the trained classifier, copy the file to a safe place. When training the next classifier this one might be overwritten.

## Extra exercise
Retrain the classifier so that it can differentiate three different classes:
* Small round objects
* Large round objects
* Large elongated objects
