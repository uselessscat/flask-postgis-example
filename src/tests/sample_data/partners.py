from shapely.geometry import Point, MultiPolygon, Polygon
from geoalchemy2.shape import from_shape

from app.utils import camelcase


def get_snake() -> dict:
    return {
        'id': 1,
        'trading_name': 'Test partner',
        'owner_name': 'Test owner',
        'document': '123456789/1234',
        'coverage_area': {
            'type': 'MultiPolygon',
            'coordinates': [[[[0, 0], [1, 0], [0, 1], [0, 0]]]]
        },
        'address': {
            'type': 'Point',
            'coordinates': [0.25, 0.25]
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
