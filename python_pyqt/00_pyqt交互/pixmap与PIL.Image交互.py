from PIL import ImageQt

# PIL格式转QPixmap格式
def pil_2_pixmap( pil_img):
    '''
    :param pil_img: 注意 PIL Image 传入参数，必须是 RGBA 格式, 如果不是, 使用 pil_img.convert("RGBA")
    :return:
    '''
    print("PIL格式转QPixmap格式")
    pixmap = ImageQt.toqpixmap(pil_img)
    return pixmap


# QPixmap格式转PIL格式
def pixmap_2_pil(pixmap):
    print("QPixmap格式转PIL格式")
    img_obj = ImageQt.fromqpixmap(pixmap)
    return img_obj