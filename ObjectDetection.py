import json
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import AnalyzeEnums, FileWithMetadata
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('A0PkONyuT7bhto6799xIf0cgQavRCzED6spcpAvxBjJr')
visual_recognition = VisualRecognitionV4(
    version='2019-02-11',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/1300d008-0fcf-40ab-8af2-e0424443db31')

with open('womenw.jpg', 'rb') as bikeride, open('man.jpg', 'rb') as cycleride, open('cyclegirl.jpg', 'rb') as cyclegirl:
    result = visual_recognition.analyze(
        collection_ids=["c65394e4-6b89-40bf-8d03-7c231985db00"],
        features=[AnalyzeEnums.Features.OBJECTS.value],
        images_file=[
            FileWithMetadata(bikeride),
            FileWithMetadata(cycleride),
            FileWithMetadata(cyclegirl)
        ]).get_result()
    print(json.dumps(result, indent=2))
