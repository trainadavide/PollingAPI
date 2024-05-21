from rest_framework import serializers
from polls_app.models import Poll, Question, Response

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    responses = ResponseSerializer(many=True ,read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True,read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
