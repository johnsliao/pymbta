import requests, os, re

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

    ROUTES = {"CR-Fairmount":"Fairmount",
              "CR-Fitchburg":"Fitchburg",
              "CR-Worcester":"Framingham/Worcester",
              "CR-Franklin":"Franklin",
              "CR-Greenbush":"Greenbush",
              "CR-Haverhill":"Haverhill",
              "CR-Lowell":"Lowell",
              "CR-Needham":"Needham",
              "CR-Newburyport":"Newburyport/Rockport",
              "CR-Providence":"Providence/Stoughton",
              "CR-Kingston":"Kingston/Plymouth",
              "CR-Middleborough":"Middleborough/Lakeville",
              }

    def is_valid_route(route):
        return route.lower() in Route.ROUTES.items()

class MBTA(object):
    QUERY_TYPE = ['vehiclesbyroute', 'vehiclesbytrip']
    DIRECTIONS = ['inbound', 'outbound']

    def __init__(self, format='json', direction=None, query_type=None):
        self.base_url = 'http://realtime.mbta.com/developer/api/v2/'
        self.key = os.environ.get('MBTA_API_KEY')
        self.format = format
        self.direction = direction
        self.query_type = query_type

class PurpleLine(MBTA):
    def __init__(self, query_type=None, direction=None, format='json'):
        MBTA.__init__(query_type=query_type, direction=direction, format=format)

    def check_parameters(self):
        pass

    def generate_url(self):
        pass


class RedLine(MBTA):
    pass

class GreenLine(MBTA):
    pass

class OrangeLine(MBTA):
    pass

class BlueLine(MBTA):
    pass

