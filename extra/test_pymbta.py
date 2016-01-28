import unittest
from pymbta import PurpleLine, RedLine, GreenLine, OrangeLine, BlueLine, Bus


def main():
    p = PurpleLine(
        query_type='vehiclesbyroute', direction='outbound', route='Lowell')
    r = RedLine(
        query_type='vehiclesbyroute', direction='northbound', route='Red Line')
    g = GreenLine(
        query_type='vehiclesbyroute', direction='westbound', route='Green Line E')
    o = OrangeLine(
        query_type='vehiclesbyroute', direction='northbound', route='Orange Line')
    b = BlueLine(
        query_type='vehiclesbyroute', direction='westbound', route='Blue Line')
    bus = Bus(
        query_type='vehiclesbyroute', direction='outbound', route='1')

if __name__ == '__main__':
    main()
