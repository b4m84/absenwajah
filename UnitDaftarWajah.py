# =========================== USES =============================================
import os, cv2, easygui, time, numpy as np
# ============================ END USES ========================================

# function pendaftaran Wajah
def FormDaftarWajah(a):
    wajahDir = 'DataWajah'
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 660)  # ubah lebar cam
    cam.set(4, 488)  # ubah tinggi cam
    faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eyeDetector = cv2.CascadeClassifier('haarcascade_eye.xml')

    # tampilkan wajah ke layar
    while True:
        retV, frame2 = cam.read()
        abuAbu = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        cv2.putText(frame2, 'Tekan q utk melanjutkan Simpan', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.imshow('Webcam', frame2)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 or k == ord('q'):
            break
    # end tampilkan wajah

    faceID = a
    # easygui.msgbox("Tatap Wajah Ke Webcam tunggu 30 detik hingga proses selesai", title="Info")
    # print ('Tatap Wajah Ke Webcam tunggu 30 detik hingga proses selesai')

    # faceID = input('Masukkan Face ID kemudian enter : ')
    ambilData = 1
    while True:
        retV, frame = cam.read()
        abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)
        for (x, y, m, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + m, y + h), (0, 255, 255), 2)
            namaFile = 'wajah.' + str(faceID) + '.' + str(ambilData) + '.jpg'
            cv2.imwrite(wajahDir + '/' + namaFile, frame)
            ambilData += 1
            roiAbuAbu = abuAbu[y:y + h, x:x + m]
            roiWarna = frame[y:y + h, x:x + m]
            eyes = eyeDetector.detectMultiScale(roiAbuAbu)
            for (xe, ye, me, he) in eyes:
                cv2.rectangle(roiWarna, (xe, ye), (xe + me, ye + he), (0, 20, 255), 1)

        cv2.imshow('Webcam', frame)
        # cv2.imshow('Webcam - Grey',abuAbu)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 or k == ord('q'):
            break
        elif ambilData > 30:
            break

    # print('Pengambilan Data Sukses')
    messagebox.showinfo("Information", "Pengambilan Data Sukses")
    cam.release()
    cv2.destroyAllWindows()
