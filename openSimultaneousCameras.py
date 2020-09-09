import cv2
import threading

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print "Starting " + self.previewName
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)

cameraIDs = ['rtsp://192.168.1.64/1', 'rtsp://192.168.1.65/1']
# Create two threads as follows
threadPool = []
for i in range(len(cameraIDs)):
    thread = camThread(f"Camera {i+1}", cameraIDs[i])
    threadPool.append(thread)
    thread.start()