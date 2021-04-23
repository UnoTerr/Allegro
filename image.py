from cv2 import cv2
import numpy as np

template_h = np.zeros((1, 6, 3), np.uint8)
template_h[0, 0:3] = (255, 255, 255)
template_h[0, 3:6] = (0, 0, 255)
template_v = np.zeros((6, 1, 3), np.uint8)
template_v[0:3, 0] = (0, 0, 255)
template_v[3:6, 0] = (255, 255, 255)
a_list = [template_h, template_v]

def rotation(post_img):
    img_rgb = cv2.imdecode(np.fromstring(post_img.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    j = 0
    for i in a_list:
        res = cv2.matchTemplate(img_rgb, i, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 1)
        if loc[0].any() and j == 0:
            fin = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)
            break
        if loc[0].any() and j == 1:
            fin = cv2.rotate(img_rgb, cv2.ROTATE_180)
            break
        if not loc[0].any() and j == 1:
            print('204 No content')
            break
        j = j + 1

    cv2.imwrite('fin.png', fin)