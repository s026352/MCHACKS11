from cvzone.HandTrackingModule import HandDetector
import cv2
import socket

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
success, img = cap.read()
h, w, _ = img.shape
detector = HandDetector(detectionCon=0.8, maxHands=2)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)


def compare_lists(list1, list2):
    # Check if the lists are of the same length
    if len(list1) != len(list2):
        return False
    
    # Iterate through the lists
    for val1, val2 in zip(list1, list2):
        # Check if the difference is greater than 30% of the value from the first list
        if abs(val1 - val2) / max(abs(val1), abs(val2), 1) > 0.7:
            return True
    
    # If no difference greater than 30% was found
    return False


data = []
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

    old_d = data
    data = []

    if hands:
        # Hand 1
        hand = hands[0]
        lmList = hand["lmList"]  # List of 21 Landmark points
        for lm in lmList:
            data.extend([lm[0], h - lm[1], lm[2]])

        sock.sendto(str.encode(str(data)), serverAddressPort)
        print(compare_lists(data,old_d))
    # print(data)
    # Display
    img = cv2.resize(img,(0,0),None,0.5,0.5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
