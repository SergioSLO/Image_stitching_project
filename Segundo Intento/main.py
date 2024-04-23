import cv2
import glob

image_paths = glob.glob('Images/*.jpg')
images = []


for image in image_paths:
    img = cv2.imread(image)
    images.append(img)


imageStitcher = cv2.Stitcher_create()

error, stitched_img = imageStitcher.stitch(images[0:3])

if not error:

    cv2.imwrite("stitchedOutput.png", stitched_img)
    cv2.imshow("Stitched Img", stitched_img)
    cv2.waitKey(0)
else:
    print("ERROR", error)



# primera_fase = []
# n = 2
# for i in range(2):
#     print(len([fotitos[i * n], fotitos[(i * n) + 1]]))
#     error, stitcher_img = stitcher.stitch([fotitos[i * n], fotitos[(i * n) + 1]])
#     if not error:
#         primera_fase.append(stitcher_img)
#         path = "Panoramica" + str(i) + ".jpg"
#         cv2.imwrite(path, stitcher_img)
#     else:
#         print("ERROR", error)
