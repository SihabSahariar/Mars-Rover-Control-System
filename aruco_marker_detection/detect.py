# detect ArUco Marker using OpenCV
# source: https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/aruco_basics.html

import cv2
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl

def generate_markers():
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

    fig = plt.figure()
    nx = 4
    ny = 3
    for i in range(1, nx*ny+1):
        ax = fig.add_subplot(ny,nx, i)
        img = aruco.drawMarker(aruco_dict, i, 700)
        plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
        ax.axis("off")

    plt.show()

def identify_markers():
    frame = cv2.imread("imgs/img_1.jpg")
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray_frame, aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(rgb_frame.copy(), corners, ids)

    plt.figure()
    plt.imshow(frame_markers)
    for i in range(len(ids)):
        c = corners[i][0]
        plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    generate_markers()
    identify_markers()
