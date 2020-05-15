import cv2

capture = cv2.VideoCapture('input.mp4')
background_subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

for i in range(0, length) :
    ret, frame = capture.read()

    # for first frame
    if first_iteration_indicator == 1 :
        first_frame = copy.deepcopy(frame)
        height, width = frame.shape[:2]
        accum_image = np.zeros((height,width), np.uint8)

    