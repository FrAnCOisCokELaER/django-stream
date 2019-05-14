# Create your views here.

# schema view request

import datetime
import base64
import logging
import time
from functools import reduce

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from myapp.serializer import *
from template.comments import Comment
from template.mongoconnector import insertdocument
from template.transaction import Transaction

serviceName = __name__.split('.')[1]

logger = logging.getLogger('basiclogger')


def encode(message):
    return base64.b64encode(message.encode('utf-8')).decode('utf-8)')


class Base64View(generics.GenericAPIView):
    """
        Base64 encoding
    """
    serializer_class = myappInputSerializer

    def post(self, request, format=None):
        start = time.time()
        logger.info("Calling base64 encoding view")

        inputserializer = myappInputSerializer(data=request.data)
        inputserializer.is_valid(raise_exception=True)

        # processing
        message = request.data['message']
        encoding = encode(message)

        end = time.time()

        # saving transation
        comment = Comment('Everything is OK', 201, 'INFO')
        transaction = Transaction(userId=str(request.user), datetime=datetime.datetime.now(), comments=comment.__dict__, \
                                  duration=(end - start), serviceName='encoder64', serviceVersion='v1.0')
        insertdocument(transaction.__dict__, "Transaction")

        return Response({"encoding": encoding}, status=status.HTTP_200_OK)


class VectorOperation(generics.GenericAPIView):
    """
        Example of operations on vector
    """
    serializer_class = myappInputVectorSerializer

    @swagger_auto_schema(operation_description="Compute the cumulated distance",
                         responses={200: myappOutputVectorSerializer()})
    def post(self, request, *args, **kwargs):
        inputserializer = myappInputVectorSerializer(data=request.data)
        if inputserializer.is_valid(raise_exception=True):
            start = time.time()
            logger.info("Calling Vector operation view")
            route = inputserializer.validated_data
            timeinput = route['time']
            speed = route['speed']

            difftime = []
            for x, y in zip(timeinput, timeinput[1:]):
                difftime.append(y - x)

            difftime.insert(0, 0)
            difftime.insert(1, timeinput[0])
            speed.insert(0, 0)
            distance = list(map(lambda x, y: x * y, difftime, speed))
            cumulated_distance = reduce(lambda x, y: x + y, distance, 0)

            end = time.time()
            results = dict()
            results['cumulated_distance'] = cumulated_distance
            # saving transation
            comment = Comment('Cumulated distance computation is OK', 201, 'INFO')
            transaction = Transaction(userId=str(request.user), datetime=datetime.datetime.now(),
                                      comments=comment.__dict__, duration=(end - start),
                                      serviceName='vectorOperation',
                                      serviceVersion='v1.0')
            insertdocument(transaction.__dict__, 'Transaction')
            return Response(results, status=status.HTTP_200_OK)
        else:
            data = {"Error": {"status": 400,
                              "message": "Output data was not valid - please correct the below errors",
                              "error_details": [{"field": key, "message": inputserializer.errors[key][0]} for key in
                                                inputserializer.errors.keys()]}}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
