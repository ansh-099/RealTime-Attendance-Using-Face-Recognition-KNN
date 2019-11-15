import os
import numpy as np
import cv2
from sklearn.neighbors import KNeighborsClassifier
import time

from datetime import datetime

# Current date time in local system
date = datetime.now().date()
date = str(date)
print(date)
currentAdds = []

fileName = str("presentPeople"+date+".txt")
# f = open(fileName, 'w')
# f.close

with open(fileName) as f:
    content = f.readlines()

content = [x.strip() for x in content]
if len(content) == 0:
	presenties = []
else:
	presenties = content[0].split()
	presenties = [x.lower() for x in presenties]
print("All people",presenties)


files = [f for f in os.listdir('dataset') if f.endswith('.npy')]
names = [f[:-4] for f in files]

face_data = []
present = []

for filename in files:
	data = np.load('dataset/'+filename)
#	print(data.shape)
	face_data.append(data)

face_data = np.concatenate(face_data, axis=0)

print(face_data.shape)
print(type(face_data))
names = np.repeat(names,10)
names = np.reshape(names,(-1,1))
dataset = np.hstack((face_data,names))
print("dataset shape" ,dataset.shape)

# train
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(dataset[:,:-1], dataset[:,-1])

capture = cv2.VideoCapture(0)

past = ""
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
	returned , image = capture.read()

	if not returned:
		continue
	
	faces = face_cascade.detectMultiScale(image , 1.3, 5)

	for face in faces:
		x,y,w,h = face

		onlyFace = image[y:y+h,x:x+w]
		onlyFace = cv2.resize(onlyFace,(100,100))
		
		# print(onlyFace.shape)
		onlyFace = onlyFace.reshape((1,-1))
		print("only face", onlyFace.shape)
	
		# print("After changing shape",onlyFace.shape)
		prediction = knn.predict(onlyFace)
		print(prediction)

		# Drawing rectangle and writing name on it
		cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),2)
		cv2.putText(image,prediction[0],(x,y),cv2.FONT_ITALIC,1,(0,255,0),2)
		if not past == prediction[0]:
			present.append(prediction[0])
		past = prediction[0]

	cv2.imshow("Attendence for "+date+" (Press q to Quit)",image)
	key = cv2.waitKey(1)
	if key & 0xFF == ord('q'):
		break
print("pres" ,present)

f=open(fileName, "a+")

for value in present:
	if not value.lower() in presenties:
		if not value.lower() in currentAdds:	
			f.write(value.lower()+ " ")
			currentAdds.append(value.lower())
f.close()



capture.release()

cv2.destroyAllWindows()





