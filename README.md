# Spectral-Microscope-Tools

The scripts here were written in Python for use in ImageJ (Fiji) and are based on algorithms detailed in Oakley et. al. "Improved Spectral Imaging Microscopy for Cultural Heritage through Oblique Illumination", *Heritage Science*, 8:1. [download](https://heritagesciencejournal.springeropen.com/articles/10.1186/s40494-020-00369-0)

## Getting Started with the Scripts

Download the latest version of [Fiji](https://fiji.sc) and place the scripts into the plugins folder. Launch Fiji or "refresh menus" if already running.

## What do each of the scripts do?

**LambdaStack to XYZ:** Script converts a stack of monochromatic wavelength images (collected by the NU-ACCESS spectral microscope) into an XYZ tristimulus space. This is accomplished by multiplying each wavelength image by the CIE 1931 Standard Observer matching function, thus producing X, Y, and Z tristimulus value images. The input parameters are the spacing between wavelengths (typically 5 nm) as well as the starting (default = 430 nm) and ending (default = 750 nm) wavelengths.

**XYZ to RGB:** Script converts the XYZ stack into adobe RGB color space assuming a standard D65 Illuminant.

**rotation:** Rotates images of a single wavelength to the polar orientation of the first image collected (angle 0). Input parameter is the number of angles collected in the given experiment.

**manual shift:** Before launching this script, use the rotation script (described above). Then use the ImageJ point tool to hand select a single feature in each illumination angle image, saving each point in the ROI manager. This script will use these selected points to compute the X-Y translation of each image to complete registration. Note: use this script only if the built-in ImageJ SIFT functions fail to find a precise and accurate registration (which can happen with gradient images).
