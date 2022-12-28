# native modules (built in modules)
from pprint import pprint
from typing import Dict, List

# third party libs
import requests

# user-defined libs
from utils.fetch_data import fetch_data
from utils.timing1 import timeit


@timeit
def get_all_character_names(result: Dict) -> List:
    """
    pick only names from film data.

    :param result: data fetched from first film
    :return: names of chars in movie 1
    """

    char_urls = result.get("characters")
    char_data = fetch_data(char_urls) if char_urls else []  # ternary operator
    char_names = [char.get("name") for char in char_data if char_data]
    return char_names


@timeit
def get_all_vehicle_names(result_: Dict) -> List:
    """
    pick all vehicle names
    :param result_: data from first film
    :return: names of vehicles
    """

    v_urls = result_.get("vehicles")
    v_data = fetch_data(v_urls) if v_urls else []
    v_names = [vehicle.get("name") for vehicle in v_data if v_data]
    return v_names


if __name__ == "__main__":
    url = "https://swapi.dev/api/films/1/"
    response = requests.request("GET", url)
    response1 = requests.get(url)
    result1 = response1.json()

    char1_names = get_all_character_names(result1)
    v1_names = get_all_vehicle_names(result1)

    print(char1_names)
    print("****" * 20)
    pprint(v1_names)
