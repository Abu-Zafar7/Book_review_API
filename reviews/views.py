from django.shortcuts import render
from .serializers import RegisterUserSerializer, BookSerializer, ReviewSerializer
from .models import Book, Review
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from django.db.models import Avg
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action



class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterUserSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message":"User registered successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.annotate(average_rating= Avg('reviews__rating'))
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'genre']
    ordering_fields = ['title','author','average_rating','date_added']

    def get_permissions(self):
        
        if self.action in ['list','retrieve']:
            permission_classes = [AllowAny]
        
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]    



class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
  

    def get_permissions(self):
       
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can create/update/delete reviews
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
       
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        
        review = self.get_object()
        if review.user != request.user:
            return Response({'error': 'You are not authorized to update this review.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        
        review = self.get_object()
        if review.user != request.user:
            return Response({'error': 'You are not authorized to update this review.'}, status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
       
        review = self.get_object()
        if review.user != request.user:
            return Response({'error': 'You are not authorized to delete this review.'}, status=status.HTTP_403_FORBIDDEN)
        super().destroy(request, *args, **kwargs)

        return Response(
        {
            'message': 'Your review was successfully deleted.'
            
        },
        status=status.HTTP_200_OK
    )



class BookRecommendationView(APIView):
    """
    View for recommending books based on genre, author, or user rating.
    """

    def get(self, request):
    
        genre = request.query_params.get('genre', None)
        author = request.query_params.get('author', None)
        user_rating = request.query_params.get('user_rating', None) 

        books = Book.objects.all()

        
        if genre:
            books = books.filter(genre__icontains=genre)

        
        if author:
            books = books.filter(author__icontains=author)

        
        if user_rating:
            try:
                rating = float(user_rating)
                if rating < 1 or rating > 5:
                    return Response({"error": "Rating must be between 1 and 5"}, status=status.HTTP_400_BAD_REQUEST)
                
                books = books.annotate(average_rating=Avg('reviews__rating'))
                books = books.filter(average_rating__gte=rating)  
            except ValueError:
                return Response({"error": "Invalid user rating value"}, status=status.HTTP_400_BAD_REQUEST)

        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)