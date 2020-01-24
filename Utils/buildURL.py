# This file is for building URL from base URL https://swapi.co/api/
# Can be used for building URLs for GET,POST,PUT,DELETE and so on and so forth
class BuildUrl:

    def __init__(self, resource,resource_id):
        self.resource = resource
        self.resource_id = resource_id


    def build_get_URL1(resource):
        url = "https://swapi.co/api/" + resource
        return url

    def build_get_URL(resource,resource_id):
        #base_url = "https://swapi.co/api/"
        url = "https://swapi.co/api/"+resource+"/"+resource_id
        return url