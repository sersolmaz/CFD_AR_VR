import os
import subprocess
from paraview.simple import *
import bpy
import timeit
import shutil



"""Processing in ParaView via state file"""
# timer for data processing performance
start1 = timeit.default_timer()

# import user-defined paraview_state 
# M1 for data processing from native CFD files (OpenFOAM, Ansys Fluent)
# M2 for data processing from extracts (COMSOL)
exec(open('paraview_state_M1.py').read())
renderView1.Update()
stop1 = timeit.default_timer()
"""Processing in ParaView via state file"""



"""Data processing: ParaView and Blender"""
start2 = timeit.default_timer()
# export data format ParaView
export_format_paraview = '.x3d'
# directory to save export of ParaView (example)
path_paraview='C:/Users/Desktop/processing/'
# import data format Blender
import_format_blender = '.x3d'
# export data format Blender
export_format_blender = '.fbx'
# directory to save export of Blender (example)
path_blender='C:/Users/Desktop/processing/'
# define total number of timesteps
timestep_sim = 2;
for x in range(0, timestep_sim):
    # paraview supporting data export
    ExportView(path_paraview + str(x) + export_format_paraview, view=renderView1, ExportColorLegends=1)
    SaveData(path_paraview + str(x) + '.csv')
    SaveScreenshot(path_paraview + str(x) + '.png', renderView1, ImageResolution=[1025, 782])
    animationScene1 = GetAnimationScene()
    animationScene1.GoToNext()
    # blender starts metadata import & export
    path_to_obj_dir = os.path.join(path_blender)
    # get list of all files in directory
    file_list = sorted(os.listdir(path_to_obj_dir))
    # get a list of files
    obj_list = [item for item in file_list if item.endswith(import_format_blender)]
    # loop through the strings in obj_list and add the files to the scene
    for item in obj_list:
        path_to_file = os.path.join(path_to_obj_dir, item)
        bpy.ops.import_scene.x3d(filepath = path_to_file)
    # get the current path and make a new folder for the exported meshes
    path_blender = bpy.path.abspath(path_blender)
    for object in bpy.context.selected_objects:
        # deselect all meshes
        bpy.ops.object.select_all(action='DESELECT')
        # select the object
        object.select = True
        # export object with its name as file name
        bpy.ops.export_scene.fbx(filepath=path_blender + object.name + export_format_blender,use_selection=True,)
stop2 = timeit.default_timer()
"""Data processing: ParaView and Blender"""



"""Unity"""
# Deactivate this -Unity- part if files transferred manually.
start3 = timeit.default_timer()

# asset directory of the Unity project
path_unity='C:/Users/Documents/Unityproject/Assets/CFD'
 
# update the Unity project directory with        
shutil.copytree(path_blender, path_unity)

# execture the Unity game engine        
path_to_gameengine= 'C:/Program Files/Unity/Hub/Editor/2019.1.0f2/Editor/Unity.exe'
subprocess.call([path_to_gameengine])
stop3 = timeit.default_timer()
"""Unity"""



"""Data processing performance"""
b_x3d = os.path.getsize(path_blender + '0.x3d')
print('*****Data processing performance*****')
print('Time_ParaView: ', stop1 - start1)
print('X3D file size in bytes:',b_x3d)
print('Time_ParaView_Blender: ', stop2 - start2)
path_to_obj_dir = os.path.join(path_blender)
file_list = sorted(os.listdir(path_to_obj_dir))
obj_list = [item for item in file_list if item.endswith('.fbx')]
size_file_blender = []
for item in obj_list:
    path_to_file = os.path.join(path_to_obj_dir, item)
    size_processing_blender=os.path.getsize(path_to_file)
    print('FBX file sizes in bytes:',size_processing_blender)
    size_file_blender.append(size_processing_blender)
#print("The maximum is {:.1f}".format(max(size_file_blender)))
print('Time_Unity (sec): ', stop3 - start3)
print('Time_Integration (sec): ', stop3 - start3 + stop2 - start2 + stop1 - start1)
print('Data size compression ratio X3D/FBX:', b_x3d/max(size_file_blender))
"""END"""