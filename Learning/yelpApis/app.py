import requests

key = "AIzaSyDo5Zir4vHjx0LFDJbm7Q6QvA3BZdRwkus"

header = {
"Content-Type": "application/json",
"X-Goog-Api-Key": key,
"X-Goog-FieldMask": "places.displayName"
}

params = {
  "includedTypes": ["restaurant"],
  "maxResultCount": 10,
  "locationRestriction": {
    "circle": {
      "center": {
        "latitude": 37.7937,
        "longitude": -122.3965},
      "radius": 50.0
    }
  }
}

response = requests.post("https://places.googleapis.com/v1/places:searchNearby",headers=header,json=params)

# Now instead of seeing json object, we will store the data in the dictionary
print(response.text)

result = response.json()["places"]

# print(result)

# for businesses in result:
#     # for business in businesses["displayName"]:
#     print(businesses["displayName"]["text"])

list_comprehnsion_places = [placesName["displayName"]["text"] for placesName in result]

print(list_comprehnsion_places)