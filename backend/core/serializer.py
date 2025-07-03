from rest_framework import serializers
from . models import *

#=====================================================# This is for converting complex data from the browser to native python datatypes

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = '__all__'