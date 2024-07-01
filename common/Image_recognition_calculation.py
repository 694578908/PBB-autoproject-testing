import io
import os
from PIL import Image, ImageEnhance, ImageFilter
from common.read_write_yaml import YamlUtil
import base64
from paddleocr import PaddleOCR


def login_Image_recognition():
    extract_data = YamlUtil().read_testcase_yaml('extract.yml')
    for extract_key, extract_value in extract_data.items():
        # 转换bytes格式数据
        image_data = base64.b64decode(extract_value)
        image = Image.open(io.BytesIO(image_data))
        # 转换黑白图片
        gray_image = image.convert('L')
        width, height = gray_image.size
        enlarged_image = gray_image.resize((width * 2, height * 2))
        image_path = os.getcwd() + '/data/' + 'code_image.png'
        enlarged_image.save(image_path)
        # 初始化 PaddleOCR
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 初始化OCR模型
        result = ocr.ocr(image_path, cls=True)  # 识别图像
        # 打印识别结果
        for line in result:
            # line 是一个包含检测结果的列表，每个元素包括文本框坐标和识别出的文本
            for box, (text, confidence) in line:
                print(f"识别出的文本: {text}, 置信度: {confidence}")


# def login_Image_recognition():
#     extract_data = YamlUtil().read_testcase_yaml('extract.yml')
#     for extract_key, extract_value in extract_data.items():
#         # 转换 bytes 格式数据
#         image_data = base64.b64decode(extract_value)
#         images = Image.open(io.BytesIO(image_data))
#
#         # 转换为黑白图片
#         gray_image = images.convert('L')
#
#         # 放大图片，例如放大2倍
#         width, height = gray_image.size
#         enlarged_image = gray_image.resize((width * 2, height * 2), Image.LANCZOS)
#
#         # 图像预处理：锐化和去噪
#         # 锐化图像
#         sharpness_enhancer = ImageEnhance.Sharpness(enlarged_image)
#         sharpened_image = sharpness_enhancer.enhance(2.0)  # 可以调整锐化程度
#
#         # 去噪处理
#         denoised_image = sharpened_image.filter(ImageFilter.MedianFilter(size=3))
#
#         # 保存处理后的灰度图像到文件
#         image_path = os.path.join(os.getcwd(), 'data', 'code_image.png')
#         denoised_image.save(image_path)
#
#         # 读取图像并进行 OCR 识别
#         ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 初始化OCR模型
#         result = ocr.ocr(image_path, cls=True)  # 识别图像
#         # 打印识别结果
#         for line in result:
#             # line 是一个包含检测结果的列表，每个元素包括文本框坐标和识别出的文本
#             for box, (text, confidence) in line:
#                 print(f"识别出的文本: {text}, 置信度: {confidence}")