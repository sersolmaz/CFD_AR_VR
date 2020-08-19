# CFD with AR/VR 
**Multiplatform processing of CFD simulations with AR/VR**

The provided code processes steady-state and transient CFD simulation data from multiple solver (e.g. OpenFOAM, Ansys Fluent and COMSOL) to integrate extract-based CFD results in cross-platform development environments such as game engines. It creates a bridge among multiple platforms to enable one-way coupled data processing between CFD dataset and game engine. It is written in Python using ParaView and Blender APIs. The main script comprises following part in sequance:

- Post- and data-processing of CFD dataset with ParaView
- Data processing with Blender
- Data import & update in Unity game engine
- Data processing processing for assessment

The goal herewith is to provide a simple, easy-to-implement and free-to-use data processor to utilize CFD results in AR/VR environments. The code mostly provides a sample of existing CFD datasets. Minor costumizations might be required.

## Prerequisities

To execute the code, an Anaconda application must be built with ParaView and Blender packages.

## License
Please see the file ./LICENSE for details

## Contact
Serkan Solmaz (https://www.kuleuven.be/wieiswie/en/person/00127798)
* Department of Chemical Engineering, KU Leuven, Celestijnenlaan 200F, B-3001 Leuven, Belgium

