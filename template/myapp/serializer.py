from rest_framework import serializers
from .models import *


class myappInputSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=250)


class myappOutputSerializer(serializers.Serializer):
    encoding = serializers.CharField(max_length=250)


class myappInputVectorSerializer(serializers.Serializer):
    time = serializers.ListField(child=serializers.FloatField(), allow_empty=False, default=[0.4, 1.2, 2.4, 3.6])
    speed = serializers.ListField(child=serializers.FloatField(), allow_empty=False, default=[0.5, 4.6, 5.8, 6.7])

    class Meta:
        fields = {'time', 'speed'}


class myappOutputVectorSerializer(serializers.Serializer):
    cumulated_distance = serializers.FloatField()

    class Meta:
        fields = {'cumulated_distance'}
