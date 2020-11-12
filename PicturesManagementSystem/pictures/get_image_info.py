from PIL import Image
import exifread
import os
import cv2
def get_picture_info(img):

    f = open(img, 'rb')
    tags = exifread.process_file(f)
    img_time = tags['EXIF DateTimeOriginal']
    print("图片的拍摄时间为：",img_time)


    # # img.seek(0)
    # # 注意：image_PIL  获取的就是<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1024x768 at 0x105602FD0>     img.seek(0)  再img.read（）  等同于      image_PIL = Image.open(img)
    # image_PIL = Image.open(img)
    # # 获取图片的类型，宽和高
    # print("读取的内存图片为",image_PIL)
    #
    # image_PIL.seek(0)
    #
    #
    #
    #
    #
    # img_type=image_PIL.format
    # img_width=(image_PIL.size)[0]
    # img_height=(image_PIL.size)[1]
    # print("img_type, img_width, img_height, img_size",img_type,img_width,img_height)
    #
    #
    # #
    # # # 获取图片的大小
    # # imagePath = os.path.join(img)
    # # print(imagePath)
    # #
    # # imageSize = os.path.getsize(imagePath)
    # # imageSize /= 1024 * 1024
    # # img_size=round(imageSize,2)
    # # 获取图片的拍摄时间
    #
    # print("img_type, img_width, img_height, img_size",img_type,img_width,img_height)
    #
    # f = open(img, 'rb')
    # tags = exifread.process_file(f)
    # img_time = tags['EXIF DateTimeOriginal']
    # print("图片的拍摄时间为：",img_time)
    #
    # return   img_type,img_width,img_height,img_time

#
img='/Users/wangyuanyuan/Documents/wyy/01_code/PicturesManagementSystem/pictures/test_img/UNADJUSTEDNONRAW_thumb_1679.jpg'
a=get_picture_info(img)
# print(a)
# print(a[3])
