# ase-weas-widget

[![PyPI - Version](https://img.shields.io/pypi/v/ase-weas-widget.svg)](https://pypi.org/project/ase-weas-widget)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ase-weas-widget.svg)](https://pypi.org/project/ase-weas-widget)

-----

## Table of Contents

- [ase-weas-widget](#ase-weas-widget)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [How it works](#how-it-works)
  - [License](#license)

## Installation

```console
pip install ase-weas-widget
```

This should install `weas-widget` as the dependency if it is not installed. 
Please refer to the [weas-widget repository](https://github.com/superstar54/weas-widget) for examples in order to verifying its correct installation.

## Usage

This plugin allows viewing `ase.Atoms` object using `ase.visualize.view` via the [weas-widget](https://github.com/superstar54/weas-widget) in a notebook environment:

```python
from ase.build import bulk
from ase.visualize import view
atoms = bulk('Si', 'diamond', 5.4)
view(atoms.repeat((2,2,2)), viewer='weas')
```

Output example:

![example output](example.gif)


The appearance of the resulting plot can be customized with a callback function that modifies the underlying `WeasWidget` object:


```python
def apply_vesta(viewer):
    """Callback to customize the WeasWidget object"""
    viewer.avr.model_style = 1
    viewer.avr.show_bonded_atoms = True
    viewer.avr.color_type = "VESTA"
    
atoms = bulk('Si', 'diamond', 5.4)
view(atoms.repeat((2,2,2)), viewer='weas', mods=apply_vesta)
```

Output example:

![example output](example2.gif)

or equivalently using a pre-defined modifier function (callback) (see [here](https://github.com/bonan-group/ase-weas-widget/blob/main/src/ase_weas_widget/viewer.py) for available options):

```python
atoms = bulk('Si', 'diamond', 5.4)
view(atoms.repeat((2,2,2)), viewer='weas', presets='vesta,ball')
```

Please refer to the documentation of [weas-widget](https://github.com/superstar54/weas-widget) for details about how to control and modify the output.

## How it works

This plugin simply interfaces the `WeasWidget` object with the `ase.visualize` module. The `view` function returns the `WeasWidget` which is constructed from the
`ase.Atoms` object as the output. The latter is then displayed by Jupyter.


## License

`ase-weas-widget` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
