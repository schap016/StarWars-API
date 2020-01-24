import requests
def get_Response():
    response = requests.get("https://swapi.co/api/people/110/")
    if response.ok:
        json_response = response.json()
        return json_response
    else:
        return "Response not 200"



print(get_Response())

