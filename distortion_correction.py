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
width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
writer = cv.VideoWriter(output_file, fourcc, fps, (width, height))

# Run distortion correction
show_rectify = True
map1, map2 = None, None
while True:
    valid, img = video.read()
    if not valid:
        break

    display_img = img.copy()
    info = "Original"
    if show_rectify:
        if map1 is None or map2 is None:
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
        display_img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
        info = "Rectified"

    # Overlay text and show
    cv.putText(display_img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
    cv.imshow("Geometric Distortion Correction", display_img)

    # Save the current frame to output
    writer.write(display_img)

    key = cv.waitKey(10)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27:
        break
    elif key == ord('\t'):
        show_rectify = not show_rectify

video.release()
writer.release()
cv.destroyAllWindows()