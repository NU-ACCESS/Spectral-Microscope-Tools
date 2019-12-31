from ij import IJ, ImagePlus, ImageStack
from ij.process import ImageProcessor, FloatProcessor
from fiji.util.gui  import GenericDialogPlus

gd = GenericDialogPlus("Input Parameters")  
gd.addNumericField("Number of Angles", 10, 0)  # show 3 decimals
gd.showDialog() 

ang = 360/int(gd.getNextNumber())  


imp = IJ.getImage()

n_slices = imp.getStack().getSize()


for i in range(1, n_slices+1):
	imp.setSlice(i) 
	s = ((i*ang)-ang)*-1
	IJ.run("Rotate... ", "angle="+str(s) + " grid=1 interpolation=Bilinear slice")

