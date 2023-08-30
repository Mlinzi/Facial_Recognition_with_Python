import cv2

def detect_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image

choice = input("Choose an option (1: Image, 2: Video, 3: Camera): ")

if choice == '1':
    image_path = input("Enter the path to the image: ")
    image = cv2.imread(image_path)
    result = detect_faces(image)
    cv2.imshow('Detected Faces', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == '2':
    video_path = input("Enter the path to the video: ")
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        result = detect_faces(frame)
        cv2.imshow('Detected Faces', result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

elif choice == '3':
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        result = detect_faces(frame)
        cv2.imshow('Detected Faces', result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

else:
    print("Invalid choice.")
