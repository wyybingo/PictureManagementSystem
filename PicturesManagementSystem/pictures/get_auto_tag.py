import base64
import cv2
import imutils
import numpy as np

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))


def imageToStr():
    image = "./cv2img.jpg"
    with open(image, 'rb') as f:
        image_byte = base64.b64encode(f.read())
    image_str = image_byte.decode('ascii')  # byte类型转换为str
    return image_str


def process(frame, detections, w, h):
    for i in np.arange(0, detections.shape[0]):
        confidence = detections[i, 2]
        if confidence > 0.5:
            idx = int(detections[i, 1])
            box = detections[i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx],
                                         confidence * 100)

            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          COLORS[idx], 2)

            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    cv2.imwrite("./cv2img.jpg", frame)


def detection(img):
    prototxt_path = "mobilenet_/MobileNetSSD_deploy.prototxt"
    model_path = "mobilenet_/MobileNetSSD_deploy.caffemodel"

    # vs = cv2.VideoCapture(0)
    # _,frame = vs.read()
    # vs.release()
    # 获取图片用到--原有的
    # img = cv2.imdecode(img,flags=None)
    img = cv2.imread(img)
    print("图片类型为：",type(img))
    print("图片为：",img)
    frame = img
    label = ""
    frame = imutils.resize(frame, width=800)
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5, False)
    #process方法用到
    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

    net.setInput(blob)
    detections = net.forward()
    # print("detections is :\n",detections)
    rezp = detections.reshape(detections.shape[2], 7)
    data_cs = rezp[(-(rezp[:, 2])).argsort()]
    # print("detections reverse is ：\n",data_cs)
    detections = data_cs
    max_cls = detections[0, 1]
    process(frame, detections, w, h)  # 算法可视化预留函数
    # image1=imageToStr(image) #图片字节预留函数
    print("最终分类为：",int(max_cls))
    return int(max_cls)

img= "/Users/wangyuanyuan/Documents/wyy/01_code/PictureManagementSystem/PicturesManagementSystem/uploads/IMG_2256.jpeg"
a=detection(img)
print(a)







# prototxt_path = "mobilenet_/MobileNetSSD_deploy.prototxt"
# model_path = "mobilenet_/MobileNetSSD_deploy.caffemodel"
# CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
#            "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
#            "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
#            "sofa", "train", "tvmonitor"]
# img_path = "/Users/wangyuanyuan/Documents/wyy/01_code/PictureManagementSystem/PicturesManagementSystem/uploads/IMG_2256.jpeg"
# img = cv2.imread(img_path)
# COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
# net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
# res = detection(img)
# print(res)