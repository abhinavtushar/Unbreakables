import lib
import cv2

vc = cv2.VideoCapture(0)
ret, frame = vc.read()
prevLowerPos = (0, 0)

while ret:
	cv2.imshow('preview', frame)

	hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	fingerImages = lib.fingerImages(hsvframe)
	fingerPositions = lib.getPositions(fingerImages)
	mode = lib.getMode(fingerPositions)

	#Add mode text

	lowerPos = lib.getLowerBlob(hsvframe)
	if prevLowerPos != (0,0):
		# Check for up or down strum
		if down == 1:
			lib.strum(mode, 'down')
		else:
			if up == 1:
				lib.strum(mode, 'up')

	key = cv2.waitKey(20)
	ret, frame = vc.read()
	if key == 27:
		break

cv2.destroyAllWindows()