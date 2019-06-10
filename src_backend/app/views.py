from django.shortcuts import render
from rest_framework import (
    generics, response, permissions, status)
from .serializers import NumericSerializer
from .models import Numeric
# from numbers import int2roman
from roman import (
    toRoman, fromRoman, OutOfRangeError, NotIntegerError, InvalidRomanNumeralError)


class NumericAPIView(generics.GenericAPIView):

    serializer_class = NumericSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request, *a, **kw):
        numeric_objects = Numeric.objects.all()
        serializer_data = NumericSerializer(
            numeric_objects, many=True
        ).data

        return response.Response({
            'data': serializer_data
        }, status.HTTP_200_OK)

    def error(self, text="User error!"):
        return response.Response({
            'data': {},
            'errors':[
                text
            ]
        }, status.HTTP_403_FORBIDDEN)

    def post(self, request, *a, **kw):
        value = request.data.get('value', None)

        if value or value == 0:
            try:
                try:
                    converted = toRoman(int(value))
                except ValueError as err:
                    converted = fromRoman(value)

                return response.Response({
                    'data': converted,
                }, status.HTTP_200_OK)
            except OutOfRangeError as err:
                return self.error(str(err))
            except NotIntegerError as err:
                return self.error(str(err))
            except InvalidRomanNumeralError as err:
                return self.error(str(err))
        return self.error("For converting need value!")
