from unittest.util import _MAX_LENGTH
from django.forms import DateField
from dotrez.v1.booking_management.utils.dataclass_classmethods import FromDictMixin
from rest_framework import serializers

class InfantSerializer(serializers.Serializer):
    first = serializers.CharField()
    last = serializers.CharField()
    dateOfBirth = serializers.DateField()
    middle = serializers.CharField(allow_null = True, allow_blank=True, required=False)
    document = serializers.CharField()
    documentTypeCode = serializers.CharField(allow_null=True, allow_blank=True, required=False)

class PassengerInfoSerializer(serializers.Serializer):
    id = serializers.CharField(max_length = 10)
    last = serializers.CharField(max_length = 100)
    type_document: serializers.CharField(max_length = 10)
    person_type: serializers.CharField(max_length = 5)
    document_number: serializers.CharField(max_length = 20)
    gender: serializers.CharField(max_length = 10)
    country: serializers.CharField(max_length = 30)
    expiration_date: DateField()
    email: serializers.EmailField()
    nacionality: serializers.CharField(max_length = 20)
    phone: serializers.CharField(max_length = 30)
    seat: serializers.CharField(max_length = 5)
    child: serializers.CharField(max_length = 5)
    infant = InfantSerializer(required=False, allow_null = True)

class PassengersSerializer(serializers.Serializer):
    passengers = serializers.ListField(child=PassengerInfoSerializer())