from shapely.geometry import Point, MultiPolygon, Polygon
from geoalchemy2.shape import from_shape

from app.utils import camelcase


def get_snake() -> dict:
    return {
        'id': 1,
        'trading_name': 'Adega da Cerveja - Pinheiros',
        'owner_name': 'Zé da Silva',
        'document': '1432132123891/0001',
        'coverage_area': {
            'type': 'MultiPolygon',
            'coordinates': [[[[30, 20], [45, 40], [10, 40], [30, 20]]]]
        },
        'address': {
            'type': 'Point',
            'coordinates': [30, 20]
        }
    }


def get_w_geoobjects() -> dict:
    data = get_snake()

    polygon = Polygon([
        Point(30, 20),
        Point(45, 40),
        Point(10, 40),
        Point(30, 20)
    ])

    multipolygon = MultiPolygon([polygon])

    # to WKBElement
    data['coverage_area'] = from_shape(multipolygon, srid=4326)
    data['address'] = from_shape(Point(30, 20), srid=4326)

    return data


def get_camel() -> dict:
    return {
        camelcase(key): value
        for key, value in get_snake().items()
    }
