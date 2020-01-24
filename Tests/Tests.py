import requests
import Utils.buildURL
import Utils.get_Entities


url = ""
getResponse = Utils.get_Entities.GetEntities(url)
#getResponse.get_Response("foo")

#test to get names of planets in films
def get_planets_in_films(films,film_id):
    url = Utils.buildURL.BuildUrl.build_get_URL(films,film_id)
    json_response = getResponse.get_Response(url)
    print(type(json_response))
    if not json_response == "Response not 200":
        planet_names = []
        for item in json_response["planets"]:
            planet_response = getResponse.get_Response(item)
            planet = planet_response["name"]
            planet_names.append(planet)
        return planet_names
    else:
        return "Invalid parameter"


#test to name of film in which two persons acted
def get_nameOfFilms_byStars(star1_id,star2_id):
    #get films in which stars acted
    ids = [star1_id,star2_id]
    stars_films = []
    for i in range(len(ids)):
        star_id = ids[i]
        #star_film=[]
        url_star = Utils.buildURL.BuildUrl.build_get_URL("people",star_id)
        star_film_response = Utils.get_Entities.GetEntities.get_Response(url_star)
        if not star_film_response == "Response not 200":
            film_urls = star_film_response["films"]
            stars_films.append(film_urls)
        else:
            return "Invalid parameter"



    #get common films
    common_films = []
    for i in range(0,len(stars_films[0])):
        for j in range(0,len(stars_films[1])):
            if stars_films[0][i] == stars_films[1][j]:
                json_response = Utils.get_Entities.GetEntities.get_Response(stars_films[0][i])
                film_name = json_response["title"]
                common_films.append(film_name)
    return common_films

# sort and print spaceships by passenger capacity

def sort_Spaceships(resource):
    url = Utils.buildURL.BuildUrl.build_get_URL1(resource)
    starShips_response = Utils.get_Entities.GetEntities.get_Response(url)
    starships_passengerCapacity = {}

    for i in range(0,len(starShips_response["results"])):
        starships_passengerCapacity[starShips_response["results"][i]["name"]] =  int(starShips_response["results"][i]["passengers"])
    #print(starships_passengerCapacity)
    return sorted(starships_passengerCapacity, key = starships_passengerCapacity.__getitem__)

#people that piloted Imperial Shuttle(the starship)?
def pilot_starship(starship,resource):
    url = Utils.buildURL.BuildUrl.build_get_URL1(resource)
    starShips_response = Utils.get_Entities.GetEntities.get_Response(url)
    for i in starShips_response["results"]:
        if i["name"] == starship:
            pilotNames_forStarship = i["pilots"]
            break
    pilotNames = []
    for j in pilotNames_forStarship:
        people_response = Utils.get_Entities.GetEntities.get_Response(j)
        pilotNames.append(people_response["name"])
    return pilotNames

#Which people(including robots) appeared in all Star war movies ?

def people_in_all_films():
    url = Utils.buildURL.BuildUrl.build_get_URL1("films")
    films_response = Utils.get_Entities.GetEntities.get_Response(url)
    people_reponse = Utils.get_Entities.GetEntities.get_Response(Utils.buildURL.BuildUrl.build_get_URL1("people"))
    people_inAllFilms = []
    for item in people_reponse["results"]:
        if len(item["films"]) == len(films_response["results"]):
            people_inAllFilms.append(item["name"])
    return people_inAllFilms


#What is the second biggest planet ?
def get_second_biggest_planet():
    planets_response = Utils.get_Entities.GetEntities.get_Response(Utils.buildURL.BuildUrl.build_get_URL1("planets"))
    diameter_planet={}
    for item in planets_response["results"]:
        #print(item["name"])
        #print(item["diameter"])
        diameter_planet[item["name"]] = int(item["diameter"])
        import operator
    highest = max(diameter_planet.items(), key=operator.itemgetter(1))[0]
    diameter_planet.pop(highest)
    return max(diameter_planet.items(),key=operator.itemgetter(1))[0]




















def main():
    print(get_planets_in_films(films="films",film_id="3"))
    #print(get_nameOfFilms_byStars(star1_id="4",star2_id="8"))
    #print(sort_Spaceships(resource="starships"))
    #print(pilot_starship(starship= "Imperial shuttle",resource = "starships"))
    #print(people_in_all_films())
    #print(get_second_biggest_planet())


if __name__ == '__main__':
    main()






