from PIL import Image

#fro text to speech and make audio file
from gtts import gTTS

#image to text in compiler
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def imagetosound(image):


    try:
        open_image=Image.open(image)
        text=pytesseract.image_to_string(open_image)
        text_file=" ".join(text.split("\n"))
        print(text_file)

        sound=gTTS(text_file,lang='en')
        sound.save("voice.mp3")
        os.system("voice.mp3")
        return True


    except Exception as bug:
        print("the error while excuting the code \n",bug)
        return 


if __name__=='__main__':
    imagetosound('sample .png')
    input()
