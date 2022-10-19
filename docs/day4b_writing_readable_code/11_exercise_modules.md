# Exercise modularization

Go through the code from yesterday and identify a workflow that worked well and contained these steps:

* Image preprocessing
* Instance segmentation

Copy & paste code from the notebooks you worked with yesterday into a new custom function within the module `my_analysis.py`. Write a new notebook that demonstrates how to use the functions of your `my_analysis module`.

Hint: The function should approximately have this signature:

```
def my_workflow(input_image, ...):
    """
    Description of the algorithm and explanation of the parameters
    """
    
    return label_image
```
