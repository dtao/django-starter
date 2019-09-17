"""Common decorators used throughout the project."""

from collections.abc import Iterable
from functools import wraps

from django.http import JsonResponse

serializers = {}


def serializes(data_type):
    """Register a serializer for the given data type."""
    def serializes_decorator(f):
        serializers[data_type] = f
        return f
    return serializes_decorator


def serialize(data):
    """Serialize data using the serializer(s) registered for its type."""
    serializer = serializers.get(type(data))
    if serializer is None:
        if isinstance(data, Iterable):
            return [serialize(val) for val in data]
        raise ValueError('Unable to serialize type {}'.format(type(data)))
    return serializer(data)


def serialized(f):
    """Decorate a view function to serialize the result as a JsonResponse."""
    @wraps(f)
    def serialized_wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return JsonResponse(serialize(result), safe=False)
    return serialized_wrapper
