# Spectral-Microscope-Tools

The scripts here were written in Python for use in ImageJ(FIJI) and are based on algorithms detailed in the forthcoming paper:
Oakley et. al. "Oblique Illumination Spectral Imaging Microscopy".

## Getting Started with the Scripts

Download the latest version of [Fiji](https://fiji.sc) and place the scripts into the plugins folder. Launch Fiji or "refresh menus" if already running.

## What do each of the scripts do?

**LambdaStack to XYZ** This script converts a stack of monochromatic wavelength images collected by the NU-ACCESS spectral microscope and converts them into an XYZ tristumulus space. This is accomplished by multiplying each wavelength image by the CIE 1931 Standard Observer matching function thus producing X, Y, and Z tristimulus value images.

**XYZ to RGB** The script converts the XYZ stack into adobe RGB color space assuming a standard D65 Illuminant.



