import cv2

image_name = "tiger"
image_path = image_name+".jpg"

image = cv2.imread(image_path)
image_height, image_width, _ = image.shape

overlaping_percentage = 20

number_images_height = 2
number_images_width = 2

image_cut_width = image_width//number_images_width
image_cut_height = image_height//number_images_height

overlaping_width = image_cut_width * overlaping_percentage//100
overlaping_height = image_cut_height * overlaping_percentage//100


image_matrix = []
for i in range(number_images_height):
    row = []
    for j in range(number_images_width):
        coordinate_H = i*image_cut_height
        coordinate_W = j*image_cut_width        
        row.append(image[max(coordinate_H - overlaping_height,0):min(coordinate_H + overlaping_height +image_cut_height, image_height),
                         max(coordinate_W - overlaping_width,0):min(coordinate_W + overlaping_width +image_cut_width, image_width),
                         :])
    image_matrix.append(row)

#print(image_matrix)

image_output_path = image_name+"_cuts/"+image_name

for i in range(number_images_height):
    for j in range(number_images_width):
        cv2.imwrite(image_output_path+"_"+str(i)+"_"+str(j)+".jpg", image_matrix[i][j])
#cv2.imwrite(image_output_path+"_0_0.jpg", image_matrix[0])
#cv2.imwrite(image_output_path+"_0_1.jpg", image_matrix[1])
