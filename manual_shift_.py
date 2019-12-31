from ij import IJ, ImagePlus, ImageStack
from ij.process import ImageProcessor, FloatProcessor

from ij.plugin.frame import RoiManager
 
# Initialize some variables
#img = ds.getImgPlus()
rois = RoiManager.getInstance().getRoisAsArray()
#print(rois)


xt = []
yt = []

for i in range (0, len(rois)):
	x = rois[i].getXBase() 
	y = rois[i].getYBase() 
	xt.append(x)
	yt.append(y)




ex =[]
why=[]
imp = IJ.getImage()
n_slices = imp.getStack().getSize()

for i in range(0,len(xt)):
	c = (xt[i]-xt[0])*-1
	d = (yt[i]-yt[0])*-1
	ex.append(c)
	why.append(d)
	
for i in range(1, n_slices+1):	
	imp.setSlice(i)
	IJ.run("Translate...", "x="+str(ex[i-1]) + "  y="+str(why[i-1]) + "  interpolation=None slice")


#print(why)
		
