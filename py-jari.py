import cv2
import mediapipe as mp
import serial
import time

try:
    ser = serial.Serial(port='COM5', baudrate=9600, timeout=1)
    print("Serial Terhubung")
except:
    print("Gagal terhubung ke Serial")
    ser = None

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.75)
mp_draw = mp.solutions.drawing_utils

wCam, hCam = 900, 506
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

tipIds = [4, 8, 12, 16, 20]
lastFingers = -1

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            if lmList:
                fingers = []

                if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1) 
                    else:
                        fingers.append(0) 

                totalFingers = fingers.count(1)

                if totalFingers != lastFingers:
                    lastFingers = totalFingers

                    if ser:
                        ser.write(str(totalFingers).encode())
                        print(f"Jumlah jari: {totalFingers}")

                cv2.putText(img, f"Jari: {totalFingers}", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if ser:
    ser.close()
cv2.destroyAllWindows()
