import cv2

class Image:
    def __init__(self, file, img=None):
        self.name = file
        self.img = cv2.imread(self.name) if img is None else img

    def crop(self, x, y, w, h):
        return Image(self.name + " cropped", self.img[y:y+h, x:x+w])

    def show(self, wait=True):
        cv2.imshow(self.name, self.img)
        if wait:
            cv2.waitKey()

    def agumentation(self, params):
        pass
