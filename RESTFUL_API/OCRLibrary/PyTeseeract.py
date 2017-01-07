import pytesseract
from PIL import Image


class TextTranslation:

    def translateImageToTextUsingTesseract(self,location_image):
        return pytesseract.image_to_string(Image.open(location_image))


