from __future__ import print_function
from google.cloud import vision
from google.cloud.vision_v1 import types
import os
import io

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'eastern-stock-414319-6b9b8a2e7124.json'
client = vision.ImageAnnotatorClient()

filenames = os.path.join(os.path.dirname(__file__), 'KakaoTalk_20240215_043021193.jpg')

with io.open(filenames, 'rb') as image_file:
    content = image_file.read()

image = types.Image()
image = vision.Image(content=content)
response = client.text_detection(image=image)



if response.text_annotations:
    print("감지된 텍스트:")


    print(response.text_annotations[0].description)



else:
    print("이미지에서 텍스트를 찾을 수 없습니다.")



