import io
import os
from PIL import Image, ImageEnhance, ImageFilter
import base64
from paddleocr.paddleocr import PaddleOCR
import cv2
import re
from common.read_write_yaml import YamlUtil


def paddleocr_Image_recognition():
    extract_data = YamlUtil().read_testcase_yaml('extract.yml', 'Base64')
    # for extract_key, extract_value in extract_data:
    # 转换bytes格式数据
    image_data = base64.b64decode(extract_data)
    image = Image.open(io.BytesIO(image_data))
    # 转换黑白图片
    # gray_image = image.convert('L')
    # width, height = image.size
    YamlUtil().create_dir("image")
    img_path = os.getcwd() + '/image/' + 'code_image.jpg'
    image.save(img_path)
    if 'code_image.jpg' in img_path:
        #  初始化 PaddleOCR
        ocr = PaddleOCR(
            lang='ch',
            show_log=False,
            enable_mkldnn=True,
            # det_model_dir='./inference_model/det/',  # 如果需要文本检测，可以取消注释
            rec_model_dir='./paddleocr/inference_model/rec/',
            rec_char_dict_path='./paddleocr/ppocr/utils/EN_symbol_dict.txt'
        )
        img = cv2.imread(img_path)
        enlarged_image = cv2.resize(img, (0, 0), fx=3, fy=3)
        result = ocr.ocr(enlarged_image)  # 识别图像
        # 打印识别结果
        # for line in result[0]:
        #     text = line[1][0]
        #     print("识别到的文本：", text)
        results = []
        for line in result:
            # line 是一个包含检测结果的列表，每个元素包括文本框坐标和识别出的文本
            for box, (text, confidence) in line:
                print(f"识别出的文本: {text}, 置信度: {confidence}")
                match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', text)
                if not match:
                    print("未能识别有效的运算表达式")
                    continue
                num1 = int(match.group(1))
                operator = match.group(2)
                num2 = int(match.group(3))
                # 计算结果
                if operator == '+':
                    calc_result = num1 + num2
                elif operator == '-':
                    calc_result = num1 - num2
                elif operator == '*':
                    calc_result = num1 * num2
                elif operator == '/':
                    calc_result = num1 / num2
                else:
                    print("无法识别的运算符")
                    continue

                results.append((text, calc_result))

        # 打印所有计算结果
        for expression, calc_result in results:
            print(f"{expression} 等于 {calc_result}")
            YamlUtil().write_extract_yaml({'ht_code': calc_result})
    else:
        print('图片不存在')
