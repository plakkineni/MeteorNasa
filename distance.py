import requests
import math

mylat=-121.9898103
mylong=37.5517184

resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

if resp.status_code == 200:
  meteorlist=resp.json()
  for meteor in meteorlist:
     try:
      lat=meteor['reclat']
      long=meteor['reclong']
      name=meteor['name']
      distancehome=calc_dist(float(lat),float(long),mylat,mylong)
      print ("Meteor Name: %s Distance from Home: %d"%(name,distancehome)) 
     except:
      print("Something went wrong")
      continue
  else:
   print("Invalid response code")

