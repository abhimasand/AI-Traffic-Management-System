from openSimultaneousCameras import camThread
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import time
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('model/keras_model.h5')

busyArr = [0,0,0,0]

class camera(camThread):
	def camPreview(previewName, camID, index):
	    cv2.namedWindow(previewName)
	    cam = cv2.VideoCapture(camID)
	    if cam.isOpened():  # try to get the first frame
	        rval, frame = cam.read()
	    else:
	        rval = False

	    while rval:
	    	frame = cv2.resize(frame, (224, 224))

	    	image = ImageOps.fit(image, size, Image.ANTIALIAS)
	    	image_array = np.asarray(image)
	    	normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
	    	data[0] = normalized_image_array
	    	prediction = model.predict(data)[0]
	    	predClass = np.argmax(prediction)
	    	if predClass == 0:
	    		busyArr[index] = 1
	    	else:
	    		busyArr[index] = 0
	        #cv2.imshow(previewName, frame)
	        rval, frame = cam.read()
	        key = cv2.waitKey(20)
	        if key == 27:  # exit on ESC
	            break
	    cv2.destroyWindow(previewName)




cameraIDs = [0]#,1,2,3]
# Create two threads as follows
threadPool = []
for i in range(len(cameraIDs)):
    thread = camera(f"Camera {i+1}", cameraIDs[i], i)
    threadPool.append(thread)
    thread.start()

start = 0
end = 3
maxDuration = 60
intervalDuration = 30 
minDuration = 15
visited = [0,0,0,0]
while True:
	if busyArr[np.argmax(busyArr)] == busyArr[start]:
		if visited[start] == 2:
			print (f"Green on light {start}")
			time.sleep(intervalDuration)
			if busyArr[start] == 0: 
				visited[start] = 1 
		elif visited[start] == 0:
			print (f"Green on light {start}")
			time.sleep(maxDuration)
		else:
			if min(visted) == 1:
				visited = [0,0,0,0]
			elif min(visited) == 2:
				start = visited.index(2)
				continue

	elif busyArr[np.argmax(busyArr)] != busyArr[start] and visited[start] != 1:
		if visited[np.argmax(busyArr)] == 0:
			start = np.argmax(busyArr)
			continue
		elif visited[start] == 0:
			print (f"Green on light {start}")
			time.sleep(minDuration)
		elif visited[start] == 2:
			print (f"Green on light {start}")
			time.sleep(intervalDuration)
			if busyArr[start] == 0: 
				visited[start] = 1 
		
	elif busyArr[np.argmax(busyArr)] != busyArr[start] and visited[start] == 1:
		start = np.argmax(busyArr)
		continue





