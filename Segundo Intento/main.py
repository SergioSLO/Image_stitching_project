import cv2
import glob
import numpy as np


def fast_feature_detect(ima: np.ndarray, num: int):
    fast = cv2.FastFeatureDetector.create()
    keypoints = fast.detect(ima, None)
    img_with_keypoints = cv2.drawKeypoints(ima, keypoints, None, color=(0, 255, 0))
    path = "FastFeatures" + str(num) + ".jpg"
    cv2.imwrite(path, img_with_keypoints)
    cv2.waitKey(0)


def sift_feature_detect(ima: np.ndarray, num: int):
    sift = cv2.SIFT.create()
    keypoints = sift.detect(ima, None)
    img_with_keypoints = cv2.drawKeypoints(ima, keypoints, None, color=(0, 255, 0))
    path = "SiftFeatures" + str(num) + ".jpg"
    cv2.imwrite(path, img_with_keypoints)
    cv2.waitKey(0)


def orb_feature_detect(ima: np.ndarray, num: int):
    orb = cv2.ORB.create()
    kp = orb.detect(ima, None)
    img_with_keypoints = cv2.drawKeypoints(ima, kp, None, color=(0, 255, 0))
    path = "OrbFeatures" + str(num) + ".jpg"
    cv2.imwrite(path, img_with_keypoints)
    cv2.waitKey(0)


image_paths = glob.glob('tiger_cuts/*.jpg')
images = []

for image in image_paths:
    img = cv2.imread(image)
    images.append(img)

x = 1
y = 2

sift = cv2.SIFT.create()
kp1, des1 = sift.detectAndCompute(images[x], None)
kp2, des2 = sift.detectAndCompute(images[y], None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
matchesMask = mask.ravel().tolist()

h, w, _ = img1.shape
pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
dst = cv2.perspectiveTransform(pts, H)

img2 = cv2.polylines(images[y], [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                   singlePointColor=None,
                   matchesMask=matchesMask,  # draw only inliers
                   flags=2)

img3 = cv2.drawMatches(images[x], kp1, images[y], kp2, good, None, **draw_params)

cv2.imwrite('StitchMap.jpg', img3)

result = cv2.warpPerspective(images[x], H, (images[x].shape[1] + images[y].shape[1], images[y].shape[0]))

result[0:images[y].shape[0], 0:images[y].shape[1]] = images[y]

cv2.imwrite('PanoramicStitch.jpg', result)

#---------------------------------------------------------------------------------------------------

x = 0
y = 3
img1 = images[x]

kp1, des1 = sift.detectAndCompute(images[x], None)
kp2, des2 = sift.detectAndCompute(images[y], None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
matchesMask = mask.ravel().tolist()

h, w, _ = img1.shape
pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
dst = cv2.perspectiveTransform(pts, H)

img2 = cv2.polylines(images[y], [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                   singlePointColor=None,
                   matchesMask=matchesMask,  # draw only inliers
                   flags=2)

img3 = cv2.drawMatches(images[x], kp1, images[y], kp2, good, None, **draw_params)

cv2.imwrite('StitchMap2.jpg', img3)

result = cv2.warpPerspective(images[x], H, (images[x].shape[1] + images[y].shape[1], images[y].shape[0]))

result[0:images[y].shape[0], 0:images[y].shape[1]] = images[y]

cv2.imwrite('PanoramicStitch2.jpg', result)

