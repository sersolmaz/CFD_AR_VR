# CFD with AR/VR 
**Multiplatform processing of CFD simulations with AR/VR**


----------------
**UPDATE (02.08.2023): [CFD_AR_VR](https://github.com/sersolmaz/CFD_AR_VR/tree/master) is an exploratory tool to examine different data processing pipelines between CFD solvers and game engines. It fundamentally focuses on data formats, processing performance and interoperability. Based on this preliminary work, a toolkit is developed and now available providing robust modules to integrate CFD data into game engines at [Acrossim](https://github.com/sersolmaz/Acrossim).**
----------------


The provided code processes steady-state and transient CFD simulation data from multiple solvers (e.g. OpenFOAM, Ansys Fluent and COMSOL) to integrate extract-based CFD results in cross-platform development environments such as game engines. It creates a bridge among multiple platforms to enable one-way coupled data processing between CFD dataset and game engine. It is written in Python using ParaView and Blender APIs. The main script comprises the following part in sequence:
- Post- and data processing of CFD dataset with ParaView
- Data processing with Blender
- Data import & update in Unity game engine
- Data processing performance for assessment

The goal herewith is to provide a simple, modular, easy-to-implement and free-to-use data processor to utilize CFD results in AR/VR environments. The code provides samples of existing CFD datasets from OpenFOAM (state M1) and COMSOL (state M2). Minor customizations might be required.

## Prerequisites and execution

To execute the code, an Anaconda application with Spyder must be compiled with ParaView and Blender packages.

Input(s): 
- CFD dataset either in native format (OpenFOAM) or extracts (COMSOL)
- Python state of the post-processing
- Number of timesteps
- Input and output directories

Output(s):
- Visual representations of CFD results
- Supporting multimedia files; colormap and graphs (image, video, etc.)
- Analytic data
- Data processing performance

## License
Please see the file ./LICENSE for details.

## Contact
Serkan Solmaz (https://www.kuleuven.be/wieiswie/en/person/00127798)
* Department of Chemical Engineering, KU Leuven, Celestijnenlaan 200F, B-3001 Leuven, Belgium

