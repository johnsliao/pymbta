import sys


def main(fname):
    routes = []
    with open(fname, 'r') as fs:
        for line in fs:
            line = line.split(',')
            route_id = line[0]
            route_short_name = line[2]
            routes.append([route_short_name, route_id])

    with open(r'./output.txt', 'w') as fo:
        for route in routes:
            print route
            text = str(route[0] + route[1])
            loc = text.index('"', 1)
            text = text[0:loc + 1] + ':' + text[loc + 1:] + ',\n'

            fo.write(text)

if __name__ == '__main__':
    main(sys.argv[1])
