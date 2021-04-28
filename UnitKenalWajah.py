import os, cv2, easygui, time, numpy as np

# funtion pengenalan wajah
def FormKenalWajah():
    wajahDir = 'DataWajah'
    latihDir = 'latihwajah'

    def getImageLabel(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        faceIDs = []
        for imagePath in imagePaths:
            PILImg = Image.open(imagePath).convert('L')
            imgNum = np.array(PILImg, 'uint8')
            faceID = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = faceDetector.detectMultiScale(imgNum)
            for (x, y, m, h) in faces:
                faceSamples.append(imgNum[y:y + h, x:x + m])
                faceIDs.append(faceID)
        return faceSamples, faceIDs

    faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
    faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # print('Mesin sedang melakukan training wajah, tunggu beberapa saat')
    easygui.msgbox("Mesin sedang melakukan training wajah, tunggu beberapa saat ", title="Info")
    faces, IDs = getImageLabel(wajahDir)
    faceRecognizer.train(faces, np.array(IDs))

    faceRecognizer.write(latihDir + '/training.xml')
    # print('Sebanyak {0} data wajah telah ditrainingkan ke mesin.',format(len(np.unique(IDs))) )
    easygui.msgbox(' Jumlah data wajah telah ditrainingkan ke mesin : ' + format(len(np.unique(IDs))), title="Info")

