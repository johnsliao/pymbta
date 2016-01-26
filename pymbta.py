import requests
import os
import json

"""

    pymbta is a library that takes the pain out of querying the MBTA api to find bus/train locations.

    For example code and documentation goto:
        https://github.com/johnsliao/pymbta

    The MBTA publishes its data via GTFS-realtime feeds, a standard developed by Google for delivering realtime data.
    MBTA GTFS files available here:
        http://www.mbta.com/uploadedfiles/MBTA_GTFS.zip

    Read more about using the MBTA-realtime API v2 here:
        http://www.mbta.com/rider_tools/

    If you encounter a bug, file an issue or email me:
        john@johnliao.org

"""


__author__ = 'John Liao <john@johnliao.org>'
__version__ = '1.0'


class Route(object):

    """
        Routes for all buses and trains
    """

    ROUTES = {"Fairmount": "CR-Fairmount",
              "Fitchburg": "CR-Fitchburg",
              "Framingham/Worcester": "CR-Worcester",
              "Franklin": "CR-Franklin",
              "Greenbush": "CR-Greenbush",
              "Haverhill": "CR-Haverhill",
              "Lowell": "CR-Lowell",
              "Needham": "CR-Needham",
              "Newburyport/Rockport": "CR-Newburyport",
              "Providence/Stoughton": "CR-Providence",
              "Kingston/Plymouth": "CR-Kingston",
              "Middleborough/Lakeville": "CR-Middleborough",
              }

    @staticmethod
    def is_valid_route(route):
        # Checks dict values for matching string
        return route in Route.ROUTES

    @staticmethod
    def return_route_id(route):
        return Route.ROUTES[route]


class MBTA(object):
    QUERY_TYPES = ['vehiclesbyroute', 'vehiclesbytrip']
    DIRECTIONS = ['inbound', 'outbound']
    FORMATS = ['json', 'xml']

    def __init__(self, format='json', direction=None, query_type=None, route=None):
        self.base_url = 'http://realtime.mbta.com/developer/api/v2/'
        self.key = os.environ.get('MBTA_API_KEY')
        self.format = format
        self.direction = direction
        self.query_type = query_type
        self.route = route
        self.url = ''
        self.response = ''

    def check_parameters(self):
        if self.format not in self.FORMATS:
            raise ValueError('[%s] is not a valid query format. Valid formats include %s' %
                             (self.format, self.FORMATS))

        if self.direction not in self.DIRECTIONS:
            raise ValueError('[%s] is not a valid direction. Valid directions include %s' %
                             (self.direction, self.DIRECTIONS))

        if self.query_type not in self.QUERY_TYPES:
            raise ValueError('[%s] is not a valid MBTA query type. Valid query types include %s' %
                             (self.query_type, self.QUERY_TYPES))

        if not Route.is_valid_route(self.route):
            raise ValueError('[%s] is not a valid MBTA route. Please read user guide for valid route' %
                             (self.route))

    def check_api_response(self):
        if 'error' in self.response:
            raise ValueError(
                'No MBTA available data for %s route' % self.route)


class PurpleLine(MBTA):
    LOCATIONS = []

    def __init__(self, query_type=None, direction=None, format='json', route=None):
        MBTA.__init__(
            self, query_type=query_type, direction=direction, format=format, route=route)

    def generate_url(self):
        self.check_parameters()

        self.route_id = Route.return_route_id(self.route)

        self.url = '%s%s?api_key=%s&route=%s&format=%s' % (
            self.base_url,
            self.query_type,
            self.key,
            self.route_id,
            self.format)

    def make_api_request(self):
        result = requests.get(self.url)
        #result = requests.get('http://realtime.mbta.com/developer/api/v2/predictionsbyroute?api_key=wX9NwuHnZU2ToO7GmGR9uw&route=CR-Providence&format=json')
        self.response = json.loads(result.text)

    def return_locations(self):
        self.LOCATIONS = []
        self.generate_url()
        self.make_api_request()
        self.check_api_response()

        directions = self.response['direction']

        for direction in directions:
            if direction['direction_name'].lower() == self.direction:
                lat = direction['trip'][0]['vehicle']['vehicle_lat']
                lon = direction['trip'][0]['vehicle']['vehicle_lon']

                self.LOCATIONS.append([lat, lon])

        return self.LOCATIONS


class RedLine(MBTA):
    pass


class GreenLine(MBTA):
    pass


class OrangeLine(MBTA):
    pass


class BlueLine(MBTA):
    pass

if __name__ == '__main__':
    p = PurpleLine(
        query_type='vehiclesbyroute', direction='outbound', route='Lowell')
    print p.return_locations()
