# From PyPI:
# pip install paralleldots
# Import
import paralleldots
# Setting your API key
class API:

    def __init__(self):
        paralleldots.set_api_key('ewILadbZ5uqVpPmBOMAhB3nV84OtPNWRFbHoKiO5eBo')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion_prediction(self,text):
        response = paralleldots.emotion(text)
        return response