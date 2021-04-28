import os, cv2, easygui, time, numpy as np
import sqlite3

# funtion deteksi wajah
def FormDeteksiWajah():
    wajahDir = 'DataWajah'
    latihDir = 'latihwajah'

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 660)  # ubah lebar cam
    cam.set(4, 488)  # ubah tinggi cam
    faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

    faceRecognizer.read(latihDir + '/training.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0

    # Create a database or connect to one
    conn = sqlite3.connect('database.db')

    # Create Cursor
    c = conn.cursor()

    # Query The Database
    c.execute("SELECT nama_pegawai FROM m_pegawai")
    names = c.fetchall()

    print (names)
    # commit changes
    conn.commit

    # Close connection
    conn.close


    minWidth = 0.1 * cam.get(3)
    minHeight = 0.1 * cam.get(4)

    while True:
        retV, frame = cam.read()
        frame = cv2.flip(frame, 1)  # vertical flip

        abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(abuAbu, 1.2, 5, minSize=(round(minWidth), round(minHeight)), )
        for (x, y, m, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + m, y + h), (0, 255, 8), 2)
            id, confidence = faceRecognizer.predict(abuAbu[y:y + h, x:x + m])
            if round(100 - confidence) >= 55:
                nameID = names[id]
                confidenceTxt = "{0}%".format(round(100 - confidence))
            else:
                nameID = names[0]
                confidenceTxt = "{0}%".format(round(100 - confidence))

            cv2.putText(frame, str(nameID), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(frame, str(confidenceTxt), (x + 5, y + h - 5), font, 1, (255, 255, 0), 2)

        cv2.putText(frame, 'Tekan q utk   Keluar', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.imshow('Webcam', frame)
        # cv2.imshow('Webcam - Grey',abuAbu)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 or k == ord('q'):
            break
    # print ('Exit')
    cam.release()
    cv2.destroyAllWindows()
