"""M1 for data processing from native CFD files (OpenFOAM, Ansys Fluent)"""
# an example of post-processing state file from ParaView

# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
davincifoam = OpenFOAMReader(FileName='D:\\Engineering\\PhD\\Charming\\Charming_Prototypes_AR\\davinci\\davinci\\davinci.foam')
davincifoam.MeshRegions = ['internalMesh']
davincifoam.CellArrays = ['U', 'p']

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [972, 755]

# get layout
layout1 = GetLayout()

# show data in view
davincifoamDisplay = Show(davincifoam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.RGBPoints = [-0.5069754719734192, 0.231373, 0.298039, 0.752941, -0.21636215969920158, 0.865003, 0.865003, 0.865003, 0.07425115257501602, 0.705882, 0.0156863, 0.14902]
pLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [-0.5069754719734192, 0.0, 0.5, 0.0, 0.07425115257501602, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
davincifoamDisplay.Representation = 'Surface'
davincifoamDisplay.ColorArrayName = ['POINTS', 'p']
davincifoamDisplay.LookupTable = pLUT
davincifoamDisplay.OSPRayScaleArray = 'p'
davincifoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
davincifoamDisplay.SelectOrientationVectors = 'U'
davincifoamDisplay.ScaleFactor = 0.0620999988168478
davincifoamDisplay.SelectScaleArray = 'p'
davincifoamDisplay.GlyphType = 'Arrow'
davincifoamDisplay.GlyphTableIndexArray = 'p'
davincifoamDisplay.GaussianRadius = 0.0031049999408423903
davincifoamDisplay.SetScaleArray = ['POINTS', 'p']
davincifoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
davincifoamDisplay.OpacityArray = ['POINTS', 'p']
davincifoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
davincifoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
davincifoamDisplay.PolarAxes = 'PolarAxesRepresentation'
davincifoamDisplay.ScalarOpacityFunction = pPWF
davincifoamDisplay.ScalarOpacityUnitDistance = 0.013615136748910905
davincifoamDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
davincifoamDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
davincifoamDisplay.ScaleTransferFunction.Points = [-0.5069754719734192, 0.0, 0.5, 0.0, 0.07425115257501602, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
davincifoamDisplay.OpacityTransferFunction.Points = [-0.5069754719734192, 0.0, 0.5, 0.0, 0.07425115257501602, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
davincifoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on animationScene1
animationScene1.AnimationTime = 1.5

# Properties modified on timeKeeper1
timeKeeper1.Time = 1.5

# set scalar coloring
ColorBy(davincifoamDisplay, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
davincifoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
davincifoamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.6065344050780321, 0.865003, 0.865003, 0.865003, 1.2130688101560643, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.2130688101560643, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.27849999256432056, -0.110999999451451, 1.2717076584814735]
renderView1.CameraFocalPoint = [0.27849999256432056, -0.110999999451451, 0.0]
renderView1.CameraParallelScale = 0.32914216181773753

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).