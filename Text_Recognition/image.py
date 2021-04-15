import cv2
import numpy as np
import math
from tensorflow.keras.models import load_model
import time

# loading pre trained model
model = load_model('cnn_model/digit_classifier.h5')


def prediction(img):
    test_image = img.reshape(-1, 28, 28, 1)
    return np.argmax(model.predict(test_image))


# pitting label
def labelling(t_img, label, x, y):
    font = cv2.FONT_HERSHEY_SIMPLEX
    l_x = int(x) - 10
    l_y = int(y) + 10
    cv2.rectangle(t_img, (l_x, l_y + 5), (l_x + 35, l_y - 35), (0, 255, 0), -1)
    cv2.putText(t_img, str(label), (l_x, l_y), font, 1.5, (255, 0, 0), 1, cv2.LINE_AA)
    return t_img


# refining each digit
def image_refiner(gray):
    org_size = 22
    img_size = 28
    rows, cols = gray.shape

    if rows > cols:
        factor = org_size / rows
        rows = org_size
        cols = int(round(cols * factor))
    else:
        factor = org_size / cols
        cols = org_size
        rows = int(round(rows * factor))
    gray = cv2.resize(gray, (cols, rows))

    # get padding
    colsPadding = (int(math.ceil((img_size - cols) / 2.0)), int(math.floor((img_size - cols) / 2.0)))
    rowsPadding = (int(math.ceil((img_size - rows) / 2.0)), int(math.floor((img_size - rows) / 2.0)))

    # apply padding
    gray = np.lib.pad(gray, (rowsPadding, colsPadding), 'constant')
    return gray


def get_output_image(path):
    img = cv2.imread(path, 2)
    img_org = cv2.imread(path)

    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    # im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    for j, cnt in enumerate(contours):
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        hull = cv2.convexHull(cnt)
        k = cv2.isContourConvex(cnt)
        x, y, w, h = cv2.boundingRect(cnt)

        if (hierarchy[0][j][3] != -1 and w > 10 and h > 10):
            # putting boundary on each digit
            cv2.rectangle(img_org, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # cropping each image and process
            roi = img[y:y + h, x:x + w]
            roi = cv2.bitwise_not(roi)
            roi = image_refiner(roi)
            th, fnl = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY)

            # getting prediction of cropped image
            pred = prediction(roi)
            print(pred)
            out = ''
            out = out + str(pred)

            # placing label on each digit
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            img_org = labelling(img_org, pred, x, y)


    timestr=time.strftime("%Y%m%d-%H%M%S")
    timestr= 'texts/'+str(timestr)+'.txt'

    f = open(timestr, 'w+')
    f.write(out)
    f.close()
    return img_org
