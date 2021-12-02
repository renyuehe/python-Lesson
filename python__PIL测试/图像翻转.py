from PIL import Image

imgGirl = Image.open("girl.jpg")
img2 = imgGirl.transpose(Image.FLIP_LEFT_RIGHT)

img2.show()
