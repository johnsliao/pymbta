# pymbta
pymbta is an intuitive pure python module to use the MBTA api to find bus and train locations.

If you encounter a bug, file an issue or email me: `john@johnliao.org`

### Installation
`$ pip install pymbta`

## Set your environment variable for MBTA API Key
1. Register a developer account with the MBTA [Dev Portal Link](http://realtime.mbta.com/Portal/Account/Register)
2. Set your env var: `MBTA_API_KEY = my_mbta_api_key`

## Usage

#### Purple Line
```
from pymbta import PurpleLine
p = PurpleLine(query_type='vehiclesbyroute', direction='outbound', route='Lowell')
p.return_locations()
```

`[[u'42.3678817749023', u'-71.0630187988281']]`

#### Red Line
```
from pymbta import RedLine
r = RedLine(query_type='vehiclesbyroute', direction='northbound', route='Red Line')
r.return_locations()
```
`[[u'42.37407', u'-71.11876'], [u'42.36554', u'-71.10401'], [u'42.36953', u'-71.11154'], [u'42.34832', u'-71.05348'], [u'42.36147', u'-71.07437'], [u'42.28579', u'-71.03854'], [u'42.33107', u'-71.057'], [u'42.20882', u'-71.00141']]`

#### Bus
```
from pymbta import Bus
b = Bus(query_type='vehiclesbyroute', direction='outbound', route='1')
b.return_locations()
```

`[[u'42.3579063415527', u'-71.0928802490234'], [u'42.3404960632324', u'-71.0815887451172']]`

### Routes List
Use route_short_name as `route` parameter from [routes.txt](extra/routes.txt). Input is case sensitive (sorry)

## Additional Info
MBTA GTFS files available [here](http://www.mbta.com/uploadedfiles/MBTA_GTFS.zip)
    
Read more about using the MBTA-realtime API v2 [here](http://www.mbta.com/rider_tools/)
