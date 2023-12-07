from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitobning sarlavhasi harflardan tashkil topishi kerak!"
                }
            )

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {'status': False,
                 'message': "Kitobning sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz!"
                 }
            )
        return data

    def validate_price(self, price):
        if price < 0 or price > 9999999999:
            raise ValidationError(
                {'status': False,
                 'message': "Kitobning narxi noto'g'ri kiritilgan!"
                 }
            )
        return price
