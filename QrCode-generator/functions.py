import qrcode
import cv2

def createQR(text,location):
    img = qrcode.make(text)
    img.save(location)

# d = cv2.QRCodeDetector()
# val, _, _ = d.detectAndDecode(cv2.imread("youtubeQR.jpg"))
# print("Decoded text is: ", val)
