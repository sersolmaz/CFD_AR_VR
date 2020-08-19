"""M2 for data processing from extracts (COMSOL)"""
# an example of post-processing state file from ParaView

# state file generated using paraview version 5.8.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [972, 755]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.7071057629520495
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
velocityc51vtu = XMLUnstructuredGridReader(FileName="""'D:\\Engineering\\PhD\\Charming\\Publishing\\1_MANUSCRIPT_framework\\A_Manuscript\\5_revision_3\
ew_submit\\A_submission\\Supporting_information\\sample_comsol_v.vtu'""")
velocityc51vtu.PointArrayStatus = ['IsoLevel']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from velocityc51vtu
velocityc51vtuDisplay = Show(velocityc51vtu, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'IsoLevel'
isoLevelLUT = GetColorTransferFunction('IsoLevel')
isoLevelLUT.RGBPoints = [2.5612799973882074e-05, 0.231373, 0.298039, 0.752941, 1.04736280639947, 0.865003, 0.865003, 0.865003, 2.094699999998966, 0.705882, 0.0156863, 0.14902]
isoLevelLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'IsoLevel'
isoLevelPWF = GetOpacityTransferFunction('IsoLevel')
isoLevelPWF.Points = [2.5612799973882074e-05, 0.0, 0.5, 0.0, 2.094699999998966, 1.0, 0.5, 0.0]
isoLevelPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
velocityc51vtuDisplay.Representation = 'Surface'
velocityc51vtuDisplay.ColorArrayName = ['POINTS', 'IsoLevel']
velocityc51vtuDisplay.LookupTable = isoLevelLUT
velocityc51vtuDisplay.OSPRayScaleArray = 'IsoLevel'
velocityc51vtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
velocityc51vtuDisplay.SelectOrientationVectors = 'IsoLevel'
velocityc51vtuDisplay.ScaleFactor = 0.1
velocityc51vtuDisplay.SelectScaleArray = 'IsoLevel'
velocityc51vtuDisplay.GlyphType = 'Arrow'
velocityc51vtuDisplay.GlyphTableIndexArray = 'IsoLevel'
velocityc51vtuDisplay.GaussianRadius = 0.005
velocityc51vtuDisplay.SetScaleArray = ['POINTS', 'IsoLevel']
velocityc51vtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
velocityc51vtuDisplay.OpacityArray = ['POINTS', 'IsoLevel']
velocityc51vtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
velocityc51vtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
velocityc51vtuDisplay.PolarAxes = 'PolarAxesRepresentation'
velocityc51vtuDisplay.ScalarOpacityFunction = isoLevelPWF
velocityc51vtuDisplay.ScalarOpacityUnitDistance = 0.03261513739238651

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
velocityc51vtuDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
velocityc51vtuDisplay.ScaleTransferFunction.Points = [2.5612799973882074e-05, 0.0, 0.5, 0.0, 2.094699999998966, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
velocityc51vtuDisplay.OpacityTransferFunction.Points = [2.5612799973882074e-05, 0.0, 0.5, 0.0, 2.094699999998966, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for isoLevelLUT in view renderView1
isoLevelLUTColorBar = GetScalarBar(isoLevelLUT, renderView1)
isoLevelLUTColorBar.WindowLocation = 'AnyLocation'
isoLevelLUTColorBar.Title = 'IsoLevel'
isoLevelLUTColorBar.ComponentTitle = ''
isoLevelLUTColorBar.ScalarBarLength = 0.7008439897698198

# set color bar visibility
isoLevelLUTColorBar.Visibility = 1

# show color legend
velocityc51vtuDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(velocityc51vtu)
# ----------------------------------------------------------------
