import io
import os

from PIL import Image
from common.read_write_yaml import YamlUtil
import base64
import pytesseract

def login_Image_recognition():
    extract_data = YamlUtil().read_testcase_yaml('extract.yml')
    for extract_key, extract_value in extract_data.items():
        image_data = base64.b64decode(extract_value)
        image = Image.open(io.BytesIO(image_data))
        gray_image = image.convert('L')
        image_path = os.getcwd() + '/data/'+'code_image.png'
        gray_image.save(image_path)
        recognized_text = pytesseract.image_to_string(image_path)

        print(recognized_text)
