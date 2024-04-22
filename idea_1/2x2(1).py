import cv2

image_0_0 = cv2.imread("tiger_cuts/tiger_0_0.jpg")
image_0_1 = cv2.imread("tiger_cuts/tiger_0_1.jpg")
image_0_2 = cv2.imread("tiger_cuts/tiger_0_2.jpg")
image_1_0 = cv2.imread("tiger_cuts/tiger_1_0.jpg")
image_1_1 = cv2.imread("tiger_cuts/tiger_1_1.jpg")
image_1_2 = cv2.imread("tiger_cuts/tiger_1_2.jpg")

"""cv2.imshow("1", image_1_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

stitcher = cv2.Stitcher_create()

status0, image_0_0_0_1 = stitcher.stitch((image_0_0, image_0_1))
status1, image_1_0_1_1 = stitcher.stitch((image_1_0, image_1_1))

image_0_0_0_1 = cv2.rotate(image_0_0_0_1, cv2.ROTATE_90_COUNTERCLOCKWISE)
image_1_0_1_1 = cv2.rotate(image_1_0_1_1, cv2.ROTATE_90_COUNTERCLOCKWISE)

"""
cv2.imshow("1", image_0_0_0_1)
cv2.imshow("2", image_1_0_1_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
status2, image_0_0_1_1 = stitcher.stitch((image_0_0_0_1,image_1_0_1_1))
cv2.imshow("3", image_0_0_1_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
if status == cv2.Stitcher_OK:
    # Display the stitched image
    cv2.imshow('Stitched Image', stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif status == cv2.Stitcher_ERR_NEED_MORE_IMGS: 
    print("Need more images to perform stitching.")
elif status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
    print("Homography estimation failed.")
elif status == cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
    print("Camera parameter adjustment failed.")
elif status == cv2.Stitcher_ERR_UNKNOWN:
    print("Unknown error occurred during stitching.")
"""
