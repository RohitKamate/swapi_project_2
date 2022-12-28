from Resources.base import ResourceBase
from utils.fetch_data import hit_url


class Spaceships(ResourceBase):
    """
    Resource class (plural)
    """

    def __init__(self):
        super().__init__()
        self.relative_url = "api/starships"  # plural
        self.__character_range = [1, 82]

    @property
    def relative_url1(self):
        return self.relative_url

    @property
    def character_range(self):
        return self.__character_range

    @character_range.setter
    def character_range(self, new_range_):
        self.__character_range = new_range_

    def get_count(self):
        plural_character_url = self.home_url + self.relative_url
        response = hit_url(plural_character_url)
        result = response.json()
        return result

    def get_resource_urls(self):
        return self.home_url + self.relative_url

