import zbar

from PIL import Image
import cv2


def main():
    
    capture = cv2.VideoCapture(0)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ret, ibagem = capture.read()
        gray = cv2.cvtColor(ibagem, cv2.COLOR_BGR2GRAY)
        image = Image.fromarray(gray)
        width, height = image.size
        zbar_image = zbar.Image(width, height, 'Y800', image.tostring())
        scanner = zbar.ImageScanner()
        scanner.scan(zbar_image)
#        cv2.imshow('Detect QRCODE', frame) DESCOMENTE SE QUISER MODAFOKA
#        cv2.imshow('gray', gray)

        for decoded in zbar_image:
            print(decoded.data)


if __name__ == "__main__":
    main()
