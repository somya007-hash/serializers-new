from rest_framework import serializers
from home.models import Person

class PeopleSerializer(serializers.Serializer):

    class Meta:
        model = Person