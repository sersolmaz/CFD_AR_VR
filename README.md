# CFD_AR_VR: Multiplatform processing of CFD simulations with AR/VR

The provided code processes CFD simulation data from multiple solver to integrate extract-based results in cross-platform development environments such as game engines. It is written in Python. The goal herewith is to provide a simple, easy-to-implement and free-to-use data processor to utilize CFD results in AR/VR environments.

Therefore, it can be easily modified to test techniques in the different steps of wireless transmission. The main folder contains two subfolders:

All the code files needed to simulate a wireless transmission using 802.11p are located in the folder code.

To execute the code, you must run the Selec_grap.m file that presents three options: Simulated PHY graph Graph of the theoretical models Graphic comparison of PHY and theoretical models

Necessary datasets are included so that Selec_grap.m runs without any inconvenience. If you want to re-simulate the physical layer, you must first run the file simulation_802_11_p.m and then proceed to run Selec_grap.m

This version includes a realistic channel model for vehicular communications

The folder html contains the user manual with the commented code. You must run the Selec_grap.html file that is the main one.

-----------------------------------------------------------------
One-way script includes following parts in  a sequence:
1# Post-processing of CFD dataset with ParaView
2# Data processing with Blender
3# Data import & update to Unity 3D
4# Data processing analytics for assessment
-----------------------------------------------------------------
Input(s):
# CFD dataset (for example .foam)
# Python state of the post-processing from Paraview (paraview_state_example.py)
# Number of timesteps to be processed starting from 0.

Output(s):
# 3D metadata of processed CFD datasets (steady-state & transient)
# Graph & scientific data in multimedia format (image, colormap, video, etc.)
# Database storage of data before and after processing (text-based, CSV)
# Data process analytics to assess processing approach (data size, period, format)
-----------------------------------------------------------------
# Brief on coupling strategy: A bridge was developed to enable one-way
coupled data processing between CFD postprocessor and game engine.
The script written in Python can be found in Supplementary information.
Whilst owe-way coupling reduced number of steps be taken manually,
it also provided further insight to develop both autonomous and
two-way coupling strategies.
-----------------------------------------------------------------

*********************Prerequisities*********************

Installation of third channel software and packages are required to enable autonomous processig:
1# Install Anaconda Navigator from official repository: https://www.anaconda.com/distribution/#download-section
2# Compile Paraview package for Python in Anaconda environment from https://anaconda.org/conda-forge/paraview
3# Compile Blender package for Python in Anaconda environment from https://anaconda.org/kitsune.one/python-blender
4# (optional) Install Unity game engine to transfer final metadata to relevant directory and execute the program
5# Launch Spider 4.0. inside Anaconda Navigator with Phyton 
6# Genera a python state of post-processing using ParaView (paraview_state_example.py)
7# Open main script with Spider and complete necessary changes (mainly directories)
8# Run main script (run_oneway_coupling.py)

*********************What does the script execute*********************

The script mainly postprocesses CFD dataset as follows:
1# Post-processing of CFD dataset available in a specified directory as native .FOAM file
2# Save 3D data file of streamlines in X3D format together with preferred savings including dataset, screenshot, etc.
3# Transformation of X3D to FBX with Blender
4# Save 3D data file of streamlines in FBX format in a specified directory of game engine
5# (optional & game engine should be installed in advance) Execute game engine and update the game objects
6# Assess the throughputs with data processing analytics

# A multiplatform DATA CFD dataset to Unity 3D.
# Developer: Serkan Solmaz, KU Leuven, Belgium
# Contanct: serkan.solmaz@kuleuven.be
# 17/04/2020
