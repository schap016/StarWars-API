
import requests
class GetEntities:

    def __init__(self,url):
        self.url = url

    def get_Response(self,url):
        response = requests.get(url)
        if response.ok:
            json_response = response.json()
            return json_response
        else:
            return "Response not 200"









