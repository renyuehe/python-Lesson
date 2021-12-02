import PIL.ImageFilter as imgFilter
import PIL.Image as img

imgGirl = img.open("girl.jpg")
# imgGirlBlur = imgGirl.filter(imgFilter.BLUR()) # 模糊
imgGirlBlur = imgGirl.filter(imgFilter.CONTOUR()) # 线条

imgGirlBlur.show()
