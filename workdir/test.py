import cv2

image1 = cv2.imread("result_to_compare.jpg")
image2 = cv2.imread("result.jpg")

differences = cv2.subtract(image1, image2)

print("--------------------------------")
if differences.min() == 0 and differences.max() == 0:
    print("Test passed! Images are equal :)")
else:
    print("Test failed! Images aren't equal :(")
print("--------------------------------")
