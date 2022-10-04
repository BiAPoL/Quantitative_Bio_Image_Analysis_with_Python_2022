# Interactive dimensioanlity reduction and clustering 

The [napari-clusters-plotter](https://github.com/BiAPoL/napari-clusters-plotter) offers tools to perform various dimensioality reduction algorithms and clustering methods interactively in napari.

## Usage

### Starting point
For clustering objects according to their properties, the starting point is a [grey-value image](example_data/blobs.tif) and a label image
representing a segmentation of objects. For segmenting objects, you can for example use the
[Voronoi-Otsu-labelling approach](https://github.com/haesleinhuepf/napari-segment-blobs-and-things-with-membranes#voronoi-otsu-labelling)
in the napari plugin [napari-segment-blobs-and-things-with-membranes](https://www.napari-hub.org/plugins/napari-segment-blobs-and-things-with-membranes).

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/starting_point.png)

### Measurements
The first step is deriving measurements from the labelled image and the corresponding pixels in the grey-value image.
You can use the menu `Tools > Measurement > Measure intensity, shape and neighbor counts (ncp)` for that.
Just select the image, the corresponding label image and the measurements to analyse and click on `Run`.
A table with the measurements will open:

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/measure.png)

Afterwards, you can save and/or close the measurement table. Also, close the Measure widget.
If you are uploading your own measurements make sure that there is a column that specifies the which measurement belongs to which label
by adding a column with the name "label". If you don't specify this column it will be assumed that measurements start at 1 and each
column describes the next label.

#### Time-Lapse Measurements
If you have 3D time-lapse data this will automatically be detected. In case you have 2D time-lapse data you need to
convert it into a suitable shape using the function: `Tools > Utilities > Convert 3D stack to 2D time-lapse (time-slicer)`,
which can be found in the [napari time slicer](https://www.napari-hub.org/plugins/napari-time-slicer).
Note that tables for time-lapse data will include an additional column named "frame", which indicates which slice in
time the given row refers to. If you want to import your own csv files for time-lapse data make sure to include this column!
If you have tracking data where each column specifies measurements for a track instead of a label at a specific time point,
this column must not be added.

### Plotting

Once measurements were made, these measurements were saved in the `properties` of the labels layer which was analysed.
You can then plot these measurements using the menu `Tools > Measurement > Plot measurement (ncp)`.

In this widget, you can select the labels layer which was analysed and the measurements which should be plotted
on the X- and Y-axis. If you cannot see any options in axes selection boxes, but you have performed measurements, click
on `Update Axes/Clustering Selection Boxes` to refresh them. Click on `Run` to draw the data points in the plot area.

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/plot_plain.png)

You can also manually select a region in the plot. To use lasso (freehand) tool use left mouse click, and to use a
rectangle - right click. The resulting manual clustering will also be visualized in the original image. To optimize
visualization in the image, turn off the visibility of the analysed labels layer.

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/plot_interactive.png)

Hold down the SHIFT key while annotating regions in the plot to manually select multiple clusters.

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/multi-select-manual-clustering.gif)

#### Time-Lapse Plotting
When you plot your time-lapse datasets you will notice that the plots look slightly different.
Datapoints of the current time frame are highlighted in white and you can see the datapoints move through the plot if you press play:

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/plotting_time-lapse_data_as_movie.gif)

You can also manually select groups using the lasso tool and plot a measurement per frame and see how the group behaves in time.
Furthermore, you could also select a group in time and see where the datapoints lie in a different feature space:

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/timelapse_manual_clustering_tips.gif)

### Dimensionality reduction: UMAP, t-SNE or PCA

For getting more insights into your data, you can reduce the dimensionality of the measurements, e.g.
using the [UMAP algorithm](https://umap-learn.readthedocs.io/en/latest/), [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)
or [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html).
To apply it to your data use the menu `Tools > Measurement > Dimensionality reduction (ncp)`.
Select the label image that was analysed and in the list below, select all measurements that should be
dimensionality reduced. By default, all measurements are selected in the box. If you cannot see any measurements, but
you have performed them, click on `Update Measurements` to refresh the box. You can read more about parameters of both
algorithms by hovering over question marks or by clicking on them. When you are done with the selection, click on `Run`
and after a moment, the table of measurements will re-appear with two additional columns representing the reduced
dimensions of the dataset. These columns are automatically saved in the `properties` of the labels layer so there is no
need to save them for usage in other widgets unless you wish to do so.

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/umap.png)

Afterwards, you can again save and/or close the table. Also, close the Dimensionality Reduction widget.

### Clustering
If manual clustering, as shown above, is not an option, you can automatically cluster your data, using these implemented algorithms:
* [k-means clustering (KMEANS)](https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a)
* [Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN)](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html)
* [Gaussian Mixture Model (GMM)](https://scikit-learn.org/stable/modules/mixture.html)
* [Mean Shift (MS)](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#sphx-glr-auto-examples-cluster-plot-mean-shift-py)
* [Agglomerative clustering (AC)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)

Therefore, click the menu `Tools > Measurement > Clustering (ncp)`,
again, select the analysed labels layer.
This time select the measurements for clustering, e.g. select _only_ the `UMAP` measurements.
Select the clustering method `KMeans` and click on `Run`.
The table of measurements will reappear with an additional column `ALGORITHM_NAME_CLUSTERING_ID` containing the cluster
ID of each datapoint.

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/clustering.png)

Afterwards, you can again save and/or close the table. Also, close the clustering widget.

### Plotting clustering results
Return to the Plotter widget using the menu `Tools > Measurement > Plot measurement (ncp)`.
Select `UMAP_0` and `UMAP_1` as X- and Y-axis and the `ALGORITHM_NAME_CLUSTERING_ID` as `Clustering`, and click on `Run`.

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/hdbscan_clusters_plot.png)

Example of k-means clustering results:

![](https://github.com/BiAPoL/napari-clusters-plotter/raw/main/images/kmeans_clusters_plot.png)
