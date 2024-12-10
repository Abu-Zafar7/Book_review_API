from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique= True)
    genre = models.CharField(max_length=50)
    cover_image_url = models.URLField(max_length=500, null= True, blank= True)
    date_added = models.DateTimeField(auto_now_add= True)

    def calculate_average_rating(self):
        reviews = self.reviews.all( )
        if reviews.exists():
            return sum(review.rating for review in reviews) / reviews.count()
        return 0    

    def __str__(self):
        return self.title
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(choices=[(i,i) for i in range(1,6)])
    comment = models.TextField(null= True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.rating} stars"

