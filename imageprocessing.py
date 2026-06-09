import cv2
from PIL import Image, ImageEnhance

# IMAGE PROCESSING
# pip install opencv-python
# pip install pillow

def openCV_example():
    image = cv2.imread("./img/cat.jpg")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(image, (200, 200))
    cv2.imwrite("./img/cat_gray.png", gray_image)
    cv2.imwrite("./ima/cat_resized.png", resized_image)

def pillow_example():
    image = Image.open("./ima/cat.jpg")
    gray_image = Image.convert('L')
    resized_image = image.resize((200, 200))
    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(1.5)
    gray_image.save("./ima/cat_grey.png")
    resized_image.save("./img/cat_resized.png")
    bright_image.save("./img/cat_bright.png")

def object_detection_in_video_feed():
    # load pretrainedmodel :https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
    face_cascade = cv2.CascadeClassifier('./resources/datasets/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # convert frame to grayscale for performance
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
        # draw rectangles around faces
        for (x,y,w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow("Video Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()