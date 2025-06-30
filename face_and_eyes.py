import cv2

# Correct classifier assignments
face_classifier = cv2.CascadeClassifier('/Users/prishasarna/PycharmProjects/open_cv/haarcascade_frontalface_default (1).xml')
eye_classifier = cv2.CascadeClassifier('/Users/prishasarna/PycharmProjects/open_cv/haarcascade_eye.xml')

def face_detector(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    #scale factor : how much size reduced, lower value more accuracy 1.1 by default
    #min neighbours: quality of detected faces, lower value  more accuracy 3-6 is default vale
    #slicing for face in rectagles and eyes
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_classifier.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    return img

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Face Detector', face_detector(frame))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
