import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Todo


# class TodoModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.date = validated_data.get("date", instance.date)
        instance.not_done = validated_data.get("not_done", instance.not_done)
        instance.in_process = validated_data.get("in_process", instance.in_process)
        instance.done = validated_data.get("done", instance.done)
        instance.save()
        return instance
# def encode():
#     model = TodoModel("Пойти на тренировку", "Бокс")
#     model_sr = TodoSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Пойти на тренировку", "content":"Бокс"}')
#     data = JSONParser().parse(stream)
#     serializer = TodoSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)