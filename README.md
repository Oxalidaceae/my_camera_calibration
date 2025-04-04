# my_camera_calibration
My camera calibration using OpenCV

## Overview
This project corrects geometric distortions in video using camera calibration techniques.  
It consists of two main scripts:
- `camera_calibration.py`: Estimates intrinsic and distortion parameters from chessboard images.
- `distortion_correction.py`: Applies undistortion to videos using the calibration results.

## Calibration Setup
- **Camera**: iPhone 16 Pro (0.5x ultra-wide camera)
- **Chessboard**: 9x7 blocks (each square is 3 cm wide)
- **Number of inner corners**: 8 (columns) × 6 (rows)
- **Video resolution**: 1280 × 720

## Original Video
![before.gif](/data/before.gif)

## Corner Detection Example
![picture1.png](/data/picture1.png)

## Camera Calibration Results
* The number of selected images = 20
* RMS error = 1.2178005946152135
* Camera matrix (K) =
[[590.46512818   0.         641.58986121]
 [  0.         590.38915726 365.10676819]
 [  0.           0.           1.        ]]
* Distortion coefficient (k1, k2, p1, p2, k3, ...) = [ 0.00304039 -0.00735964  0.00019495  0.00068062  0.00116275]

> The principal point (cx, cy) ≈ (641.6, 365.1) is close to the center of the 1280×720 frame.  
> The tangential distortion coefficients (p1, p2) are very close to zero, indicating minimal tangential distortion.

## Undistorted Result
![after.gif](/data/after.gif)

## How to Run

### Step 1: Run calibration from a video
python camera_calibration.py

### Step 2: Apply distortion correction
python distortion_correction.py

Reference: https://github.com/mint-lab/3dv_tutorial