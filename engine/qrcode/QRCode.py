import zbar

from PIL import Image
import cv2


def main():
    capture = cv2.VideoCapture(0)
    ret, ibagem = capture.read()
    gray = cv2.cvtColor(ibagem, cv2.COLOR_BGR2GRAY)
    image = Image.fromarray(gray)
    width, height = image.size
    zbar_image = zbar.Image(width, height, 'Y800', image.tostring())
    scanner = zbar.ImageScanner()
    scanner.scan(zbar_image)
    cv2.imshow('Detect QRCODE', ibagem) #DESCOMENTE SE QUISER MODAFOKA
#        cv2.imshow('gray', gray)
    for decoded in zbar_image:
            text = decoded.data


if __name__ == "__main__":
    main()
