# Spectral-Microscope-Tools

The scripts here were written in Python for use in ImageJ (Fiji) and are based on algorithms detailed in the forthcoming paper:
Oakley et. al. "Oblique Illumination Spectral Imaging Microscopy".

## Getting Started with the Scripts

Download the latest version of [Fiji](https://fiji.sc) and place the scripts into the plugins folder. Launch Fiji or "refresh menus" if already running.

## What do each of the scripts do?

**LambdaStack to XYZ:** Script converts a stack of monochromatic wavelength images collected by the NU-ACCESS spectral microscope and converts them into an XYZ tristumulus space. This is accomplished by multiplying each wavelength image by the CIE 1931 Standard Observer matching function thus producing X, Y, and Z tristimulus value images. The input parameters are the spacing between wavelengths (typically 5 nm) as well as the starting (default = 430 nm) and ending (default = 750 nm).

**XYZ to RGB:** Script converts the XYZ stack into adobe RGB color space assuming a standard D65 Illuminant.

**rotation:** Rotates images of a single wavelngth to the polar orientation of the fist image collected (angle 0). Input parameter is the number of angles collected in the given experiment. 

**manual shift:** Before launching this script, use the rotation script (described above). Then use the ImageJ point tool to hand select a single feature in each illumination angle image and save each point in the ROI manager. This script will use these selected points to compute the X-Y translation of each image to complete registration. Note: use this script only if the built-in ImageJ SIFT functions fail to find a precise and accurate registration (which can happen with gradient images).
