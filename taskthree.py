# 1. TODO import all resource classes here
# 2. TODO get count of each resource
# 3. TODO get "singular" resource urls of each resource
# 4. TODO pull data from random 3 "singular" resource URLs
# 5. TODO convert swapi project into CLI application

# task1 task2 task3


import argparse
from Resources.characters import Characters
from Resources.planets import Planets
from Resources.spaceships import Spaceships
from Resources.vehicles import Vehicles
from utils.randgen import ProduceChars
from utils.fetch_data import hit_url
from pprint import pprint

developer44 = {}
# Character
people = Characters()
developer = people.get_count()
developer44.update({"People": people.get_resource_urls()})

# Planets
planets = Planets()
developer11 = planets.get_count()
developer44.update({"Planets": planets.get_resource_urls()})

# Spaceships
spaceships = Spaceships()
developer21 = spaceships.get_count()
developer44.update({"Spaceships": spaceships.get_resource_urls()})

# Vehicles
vehicles = Vehicles()
developer31 = vehicles.get_count()
developer44.update({"Vehicles": vehicles.get_resource_urls()})


# random 3 urls data

random_url = ProduceChars(0, 4, 2)
list1 = random_url.randrange()
urls = list(developer44.keys())
url = {}
urldetails = {}

for num in list1:
    c = developer44[urls[num]]
    hit = hit_url(c)
    url.update({urls[num]: c})
    urldetails.update({urls[num]: hit.json()})


parser = argparse.ArgumentParser(description="command line ")
parser.add_argument("developer1", type=str)
args = parser.parse_args()

if args.developer1 == "count":
    print("People:", developer.get(args.developer1))
    print("Planets:", developer11.get(args.developer1))
    print("Spaceships:", developer21.get(args.developer1))
    print("Vehicles:", developer31.get(args.developer1))
    print("singular resource urls of each resource: ")
    pprint(developer44)
    print("random 3 singular resource URLs : ")
    pprint(url)
    print("pull data from random 3 singular resource URLs :")
    pprint(urldetails)
