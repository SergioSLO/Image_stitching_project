import cv2

# fotitos = [
#     cv2.imread("Images/Foto 1.jpg"),
#     cv2.imread("Images/Foto 2.jpg"),
# ]
fotitos = [
    cv2.imread("Images/Imagen 1.jpg"),
    cv2.imread("Images/Imagen 2.jpg"),
]


# cv2.imshow("Image",fotitos[0])
# cv2.waitKey(0)
# cv2.imshow("Image",fotitos[1])
# cv2.waitKey(0)


ElStisher = cv2.Stitcher.create()

error, stitcher_img = ElStisher.stitch(fotitos)

if not error:
    cv2.imwrite("Panoramica.jpg",stitcher_img)
    cv2.imshow("La Panoramica",stitcher_img,)
    cv2.waitKey(0)