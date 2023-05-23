# import the required modules
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
# Get a reference to the webcam
video_capture = cv2.VideoCapture(0)

# Read a frame from the webcam
ret, frame = video_capture.read()

# Specify the path and filename for saving the screenshot
screenshot_path = "screenshot.png"

# Save the frame as a screenshot
cv2.imwrite(screenshot_path, frame)

# Release the webcam
video_capture.release()

# Display a message to indicate the screenshot has been saved
print("Screenshot saved as", screenshot_path)
# read image
img = cv2.imread(screenshot_path)

# call imshow() using plt object
plt.imshow(img[:,:,::-1])

# display that image
plt.show()

# storing the result
result = DeepFace.analyze(img,actions=['emotion'])

# print result
print(result)


