## Creating a plugin from a template using the cookiecutter

Well, first things first: [create a new conda environment](https://biapol.github.io/blog/johannes_mueller/entry_user_interf2/Readme.md#creating-your-environment). ("Another one?" 😩) Yes, better safe than sorry 😉. Don't forget to activate it.

The napari website has a complete [tutorial](https://napari.org/plugins/stable/for_plugin_developers.html) for creating plugins, and I would say the easiest way is by using [cookiecutter](https://napari.org/plugins/stable/for_plugin_developers.html#cookiecutter-template).

So, let's install and run the cookiecutter as suggested in the [template readme](https://github.com/napari/cookiecutter-napari-plugin):

```
pip install cookiecutter
cookiecutter https://github.com/napari/cookiecutter-napari-plugin
```
(`'pip' is not recognized as ...` ?? 🙀 -> `conda install pip` 😸)

(`'git' is not installed.` ?? 🙀 -> `conda install git` 😸)

The cookiecutter will then start asking you questions about your project. We will answer them one by one, but here is an overview of all of them:

⚠️Spoiler alert⚠️
![](images/cookiecutter_questions1.png)

  1. `full_name [Napari Developer]:` ***type your name***
  2. `email [yourname@example.com]:` ***type your email**, so that people can reach you to talk about your new plugin*
  3. `github_username_or_organization [githubuser]:` ***type your github username** (if you don't have a Github account, you should [create one now](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home))*
  4. `plugin_name [napari-foobar]:` ***type your plugin name** ex: 'flood-napari'*
  5. `Select github_repository_url:`  
     `1 - https://github.com/your_github_username/your_plugin_name`  
     `2 - provide later`  
     `Choose from 1, 2 [1]:`  ***type '1'**, even if you did not create your repository yet, we'll do that later*  
    *Obs: values or words inside square brackets `[]` are the default option if you just hit 'Enter'*
  
  6. `module_name [flood_napari]:` ***type your plugin module name** (our plugin has a single module, ex: 'flood_napari')*
  7. `short_description [A simple plugin to use with napari]:` ***type a brief description of your plugin***
  8. `include_reader_plugin [y]:` ***type 'n'**, because our example plugin is not a plugin for reading certain image file types*
  9. `include_writer_plugin [y]:` ***type 'n'**, because our example plugin does not write anything*
  10. `include_dock_widget_plugin [y]:` ***type 'y' or just hit 'Enter'**, because we want to dock our plugin to napari framework*
  11. `include_function_plugin [y]:` ***type 'n' for this example**, however it could be useful to organize functions into separate files*
  12. `use_git_tags_for_versioning [n]:` ***hit 'Enter'***
  13. `Select docs_tool:`  
       `1 - mkdocs`  
       `2 - sphinx`  
       `3 - none`  
      `Choose from 1, 2, 3 [1]:` ***type '2' for this example**, check [this post](https://biapol.github.io/blog/johannes_mueller/entry_sphinx/) to learn more about sphinx*  
  14. `Select license:`  
       `1 - BSD-3`  
       `2 - MIT`  
       `3 - Mozilla Public License 2.0`  
       `4 - Apache Software License 2.0`  
       `5 - GNU LGPL v3.0`  
       `6 - GNU GPL v3.0`  
      `Choose from 1, 2, 3, 4, 5, 6 [1]:` ***we like to use '1'**, you can also change this later if you want, check options [here](https://ufal.github.io/public-license-selector/)*
      
Done! You will see the screen below with further instructions. 

![](images/cookiecutter_questions2.png)

We will just do instruction number 1 to install this default napari plugin locally:
```
cd flood-napari    # replace 'flood-napari' by your plugin name to go to the right directory
pip install -e .   # install your plugin locally
```

Install napari in your environment (`pip install napari[all]`) and run napari with `napari`.
When you go to the 'Plugins' menu now, you will see your plugin name there. Don't worry now with the sub-menus, we will edit them afterwards.

![](images/napari_plugin1.png)

## Adding your local repository to Github

We will use [Github Desktop](https://desktop.github.com/) to publish our local repository into the Github page. It has a great user interface and integration. So first [download](https://desktop.github.com/) and install Github Desktop. It should be a straight-forward [installation procedure](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop). If this is your first time using it, you will need to authenticate your account as explained [here](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/authenticating-to-github).

Now open it and let's add your local repository by clicking on 'File -> Add local repository...'.

![](images/github_desktop1.png)

After that, you have to specify your local plugin address. It should be a directory located where you were when you typed cookiecutter commands (typically 'C:/Users/Your_user_name' for Windows). It has the plugin name and the following contents:

<img alt="directory_items" id="directory_items" src="images/directory_items.png" />

Find it and click on 'Add repository'. You will see that it now appears as the current repository and you will add it to Github.com by clicking on 'Publish repository'.

![](images/github_desktop1b.png)

Then a small window should pop-up. Specify the name of your repository (same name of your plugin, cookiecutter question 4) and click on 'Publish Repository'.

![](images/github_desktop1c.png)

Now, if you log in into your Github account through the browser and look at your repositories, you should see your new repository there, like this:

![](images/github_repo_page.png)
     
Notice how the contents are the same as [the ones in your local folder](#directory_items). Your template is online!

## Putting your GUI into the template

Now we will modify the code to add our widgets. In Github Desktop, let's create a separate branch for your modifications. Click on the current branch, type a new branch name and click on 'Create new branch':

![](images/new_branch.png)

Good, now all modifications will go into your new branch!

First, in order for our 'qt designer version' to work (see [previous post](https://biapol.github.io/blog/marcelo_zoccoler/entry_user_interf3#importing-your-fancy-gui-to-napari)), we have to copy its interface (`flood_tool.py`, found [here](https://github.com/BiAPoL/blog/blob/master/marcelo_zoccoler/entry_user_interf3/scripts/flood_tool.py)) to your local repository address (look for where you created your local version, something like `C:/Users/Your_user_name/flood-napari/src/flood_napari`).

Then, let's replace the default `Example Q Widget` and `example_magic_widget` by your GUI. With your favorite editor, open the file `_dock_widget.py` located in your local repository address. It should contain this code:

```Python
"""
This module is an example of a barebones QWidget plugin for napari

It implements the ``napari_experimental_provide_dock_widget`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""
from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QPushButton
from magicgui import magic_factory


class ExampleQWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        btn = QPushButton("Click me!")
        btn.clicked.connect(self._on_click)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(btn)

    def _on_click(self):
        print("napari has", len(self.viewer.layers), "layers")


@magic_factory
def example_magic_widget(img_layer: "napari.layers.Image"):
    print(f"you have selected {img_layer}")


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    # you can return either a single widget, or a sequence of widgets
    return [ExampleQWidget, example_magic_widget]
```

We will delete the `ExampleQWidget` and the `example_magic_widget` (I will also delete initial comments for clarity). We are left with this:
```Python
from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QPushButton
from magicgui import magic_factory

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    # you can return either a single widget, or a sequence of widgets
    return [ExampleQWidget, example_magic_widget]
```

The function decorated with `@napari_hook_implementation` appends its outputs to your plugin menu in napari. So, let's add all 3 GUI versions of our flood widget before it. Although they all refer to the same function, for clarity, we will rename our `flood` function to 3 different versions: `flood_qt`, `flood_magic_factory` and `flood_fgui`. Also, we will rename the Qt class from `MainWindow` to `Qt_Designer_flood` and the `FunctionGui` class from `MyGui` to `FunctionGui_flood`. 

Once we add them to the code (along with importing necessary libraries), it becomes like this:

```Python
from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QPushButton
from magicgui import magic_factory

"""
Qt Designer version
"""
from skimage.io import imread
from qtpy.QtWidgets import QMainWindow
from qtpy import uic
from pathlib import Path

def flood_qt(image, delta):
    new_level = delta*85
    label_image = image <= new_level
    label_image = label_image.astype(int)*13 # label 13 is blue in napari
    return(label_image, new_level)

# Define the main window class
class Qt_Designer_flood(QMainWindow,  Ui_MainWindow):
    def __init__(self, napari_viewer):          # include napari_viewer as argument (it has to have this name)
        super().__init__()
        self.viewer = napari_viewer
        self.UI_FILE = str(Path(__file__).parent / "flood_tool.ui")  # path to .ui file
        uic.loadUi(self.UI_FILE, self)           # load QtDesigner .ui file
        
        self.label_layer = None                # stored label layer variable
        self.pushButton.clicked.connect(self._apply_delta)
    
    def _apply_delta(self):
        image = self.viewer.layers['napari_island'].data    # We use the layer name to find the correct image layer
        delta = self.doubleSpinBox.value()
        label, level = flood_qt(image, delta)
        if self.label_layer is None:
            self.label_layer = self.viewer.add_labels(label)
        else:
            self.label_layer.data = label
        self.horizontalSlider.setValue(level)
        
"""
magicgui version
"""
from magicgui import magicgui
from napari.types import ImageData, LabelsData
@magic_factory(delta={'label': 'Temperature Increase (Δ°C):', 
                                           'min': 0, 'max' : 3, 'step': 0.1},
               new_level={'label':'Sea Level (dm):', 'widget_type':'Slider',
                         'min': 0, 'max' : 255, "enabled": False},
               auto_call=True)
def flood_magic_factory(image: ImageData, delta: float=0, new_level: int=0) -> LabelsData: 
    new_level = delta*85
    label_image = image <= new_level
    label_image = label_image.astype(int)*13 # label 13 is blue in napari
    return(label_image)

"""
FunctionGui version
"""
from magicgui.widgets import FunctionGui
from napari.types import LayerDataTuple
def flood_fgui(image: ImageData, delta: float=0, new_level: int=0) -> LayerDataTuple: 
    new_level = delta*85
    label_image = image <= new_level
    label_image = label_image.astype(int)*13 # label 13 is blue in napari
    return((label_image, {'name': 'flood result','metadata': {'new_level':new_level}}))

class FunctionGui_flood(FunctionGui):
    def __init__(self):
        super().__init__(
          flood_fgui,
          call_button=False,
          auto_call=True,
          layout='vertical',
          param_options={'delta':
                             {'label': 'Temperature Increase (Δ°C):', 
                              'min': 0, 'max' : 3, 'step': 0.1},
                        'new_level':
                            {'label':'Sea Level (dm):', 'widget_type':'Slider',
                             'min': 0, 'max' : 255, 'enabled' : False}}
        )
        
    def __call__(self):
        label_image = super().__call__()
        new_level = round(label_image[1]['metadata']['new_level'])
        self.new_level.value = new_level

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    # you can return either a single widget, or a sequence of widgets
    return [ExampleQWidget, example_magic_widget]
```

Last thing is to replace `napari_experimental_provide_dock_widget` outputs by your own. In our case, it should look like this:

```Python
@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    # you can return either a single widget, or a sequence of widgets
    return [Qt_Designer_flood, flood_magic_factory, FunctionGui_flood]
```
If you now start `napari` from the terminal again, your plugin, along with each of the 3 sub-menu versions, should be available and working!

![](images/flood_plugin_v1.png)

Reminder: we wrote our qt_designer version to work with a specific layer name (`napari_island`). There are other ways of selecting the appropriated layer, like by order, type, etc, which will not be considered in this tutorial. You can have access to available layers through the viewer instance `viewer.layers`.

## Updating Github repository

You have your updates locally in your separate branch. Let's push them into your Github repository. If you open Github Desktop again now, you should see all the changes we made listed in the left of the screen. Write a description to these changes (step 1.), click on 'commit to 'branch name'' (step 2.), and then publish your new branch (step 3.):

![](images/flood_plugin_commit.png)

After that, click on the 'Create Pull Request' button, and you will be prompted to a browser tab with your github online repository. There, click on 'Create Pull Request'. 

![](images/flood_plugin_PR.png)

After the page updates itself, click on 'Merge Pull Request' and confirm it if required.

![](images/flood_plugin_merge.png)

At the end, you should see the image below, which means your online repository is now updated with your new code!

![merge_done](https://user-images.githubusercontent.com/26173597/145111544-dea73c05-a8a5-47bb-85c4-d9431ca0de0e.png)

## Publishing your plugin
After you developed your plugin to a point where you think it's ready to share it with the world, it's time so submit it to the python package index (PyPI).
Publishing the plugin on [PyPi](https://pypi.org/) may sound like a big ordeal, but is, in fact, very simple. To do so, first create an account on [PyPi](https://pypi.org/account/register/).

### Versioning

Let's report the package's version. We will update two files for that:
   1. Go to your project repository and open the `setup.cfg` file. On this file, at around the third line, you should find something like `version == 0.0.1`. If you are releasing a newer version, replace `0.0.1` by your new version number. To know more about versioning standards, check [this post](https://py-pkgs.org/07-releasing-versioning.html#version-numbering). 
   2. Open the `__inti__.py` located in the same folder where your plugin code resides - which in this example is flood-napari/src/flood_napari - update the version inside this file as well and save it. If you prefer, there are ways to [automate version bumping](https://py-pkgs.org/07-releasing-versioning.html#automatic-version-bumping).

Now, remember to [update your Github repository](#updating-github-repository) again (commit changes, push/publish branch, create Pull request, merge).

The last step of versioning is to provide a version tag. On the Github repository's main page, at the right side, on Releases, click on "Create a new release" and the following page should load.

![](images/github_release.png)

Fill the fields highlighted by green boxes and click on "Publish Release". 

### Create source files

After this is done, open an anaconda command prompt and `cd` into your project repository. 

Next, you need to create the necessary packaging information from your sourcefiles. You can do so by either creating a *source distribution* of your package with 
```bash
python setup.py sdist
```

or a *wheel* using
```bash
python setup.py bdist_wheel
```

The difference between both is, in short, that the source distribution provides, as the name suggests, the source files that can be downloaded and have to be compiled upon installation of the package. Python wheels, on the contrary, come pre-built, which leads to faster installation. This can be convenient for large packages. For a more in-depth on the advantages of either strategy, see [this blog](https://medium.com/ochrona/understanding-python-package-distribution-types-25d53308a9a). For simple projects, there is no damage in simply providing both, like ```python setup.py sdist bdist_wheel ```

A new folder should appear in your repository, called `dist`, with a couple files inside. Before uploading to PyPi, check if this folder contains only files related to the latest version. If files named after previous versions are present, you can manually delete them.
