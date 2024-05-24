from rest_framework import serializers
from polls_app.models import Poll, Option, Response

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    responses = ResponseSerializer(many=True ,read_only=True)
    class Meta:
        model = Option
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True,read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
