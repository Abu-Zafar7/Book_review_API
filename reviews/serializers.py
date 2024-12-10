from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, Review


class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email= validated_data['email'],
            password = validated_data['password']
        )

        return user
    

class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id','title','author','isbn','genre','cover_image_url','date_added','average_rating']

    def get_average_rating(self, obj):
        return obj.calculate_average_rating()    
    

class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = Review
        fields = ['id','user','book','rating','comment','created_at']
        read_only_fields = ['user']


