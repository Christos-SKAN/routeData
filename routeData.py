import requests

def obtainRouteData(origin: str, destination: str, unit: str):
    api_key = "FlrbBgX5FzyNjJsR6IibS1210qgmdVej"
    url = f"https://www.mapquestapi.com/directions/v2/route?key={api_key}&from={origin}&to={destination}&unit={unit}"

    data = requests.get(url).json()

    if data["info"]["statuscode"] == 0:
        duration = data["route"]["formattedTime"]
        distance = str(data["route"]["distance"]) + unit
        tolls = data["route"]["hasTollRoad"]
        ferry = data["route"]["hasFerry"]
        return {"duration": duration, "distance": distance, "tolls": tolls, "ferry": ferry}
    else:
        return False
