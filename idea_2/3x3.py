import cv2

image_name = "utec"

number_images_width = 3 
number_images_height = 3

image = []
for i in range(number_images_height):
    image_row = []
    for j in range(number_images_width):
        image_row.append(cv2.imread(image_name+"_cuts/"+image_name+"_"+str(i)+"_"+str(j)+".jpg"))
    image.append(image_row)


stitcher = cv2.Stitcher_create()


# por lineas hacer stitching
stitch_by_rows = []

for i in range(number_images_height):
    image_stitch_row = image[i][0]
    for j in range(1,number_images_width):
        status, image_stitch_row = stitcher.stitch((image_stitch_row, image[i][j]))
    stitch_by_rows.append(image_stitch_row)
    """
    cv2.imshow("row_"+str(i), image_stitch_row)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

#Rotar los rows
for i in range(0,number_images_height):
    stitch_by_rows[i] = cv2.rotate(stitch_by_rows[i], cv2.ROTATE_90_COUNTERCLOCKWISE)

#Hacer stitching con las giradas
image_stitched = stitch_by_rows[0]
for i in range(1,number_images_height):
    status, image_stitched = stitcher.stitch((image_stitched, stitch_by_rows[i]))
    cv2.imshow("image", image_stitched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#No une las el 2x3 con el 1x3 :c
    
image_stitched = cv2.rotate(image_stitched, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("image", image_stitched)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
image_0_0_0_1 = cv2.rotate(image_0_0_0_1, cv2.ROTATE_90_COUNTERCLOCKWISE)
image_1_0_1_1 = cv2.rotate(image_1_0_1_1, cv2.ROTATE_90_COUNTERCLOCKWISE)
"""
"""
cv2.imshow("1", image_0_0_0_1)
cv2.imshow("2", image_1_0_1_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
status2, image_0_0_1_1 = stitcher.stitch((image_0_0_0_1,image_1_0_1_1))
cv2.imshow("3", image_0_0_1_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

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
#asd