import cv2
from cv2 import aruco
import matplotlib.pyplot as plt

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

def main():
	name = "Live Video Feed"
	cv2.namedWindow(name)
	videoCapture = cv2.VideoCapture(0)

	if videoCapture.isOpened():
		ret, frame = videoCapture.read()
	else:
		ret = False

	while ret:
		ret, frame = videoCapture.read()
		output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow(name, frame)

		parameters =  aruco.DetectorParameters_create()
		corners, ids, rejectedImgPoints = aruco.detectMarkers(
			frame, 
			aruco_dict, 
			parameters=parameters)

		if ids is not None:
			for i in range(len(ids)):
				c = corners[i][0]
				# place a circle over frame located in the center of the marker
				# radius = 5, color = red, thickness = 10 (to make it solid)
				circles_frame = cv2.circle(
					frame, 
					(int(c[:, 0].mean()), int(c[:, 1].mean())), 
					5, 
					(0, 0, 255), 
					10
				)
				cv2.imshow(name, circles_frame)


		if cv2.waitKey(1) == 27:
			break

	cv2.destroyWindow(name)
	videoCapture.release()

main()
