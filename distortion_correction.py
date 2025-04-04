import numpy as np
import cv2 as cv

# The given video and calibration data
video_file = 'data/video.mp4'
output_file = 'data/rectified_output.mp4'
K = np.array([[590.46512818, 0., 641.58986121],
              [0., 590.38915726, 365.10676819],
              [0., 0., 1.]])
dist_coeff = np.array([0.00304039, -0.00735964,  0.00019495,  0.00068062,  0.00116275])

# Open a video
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given input, ' + video_file

# Get video properties
fps = video.get(cv.CAP_PROP_FPS)
if fps == 0 or np.isnan(fps):
    fps = 30  # fallback if FPS is invalid
width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
writer = cv.VideoWriter(output_file, fourcc, fps, (width, height))

# Prepare remap once
map1, map2 = None, None
frame_count = 0

while True:
    valid, img = video.read()
    if not valid:
        break

    # Initialize remap maps
    if map1 is None or map2 is None:
        map1, map2 = cv.initUndistortRectifyMap(
            K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)

    # Apply distortion correction
    rectified = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)

    # (Optional) Overlay info text
    cv.putText(rectified, "Rectified", (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    # Write to output video
    writer.write(rectified)
    frame_count += 1

    # (Optional) Show in real-time
    cv.imshow("Geometric Distortion Correction", rectified)
    if cv.waitKey(1) == 27:  # Press ESC to exit early (optional)
        break

print(f"Total frames processed: {frame_count}")
video.release()
writer.release()
cv.destroyAllWindows()