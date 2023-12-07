from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer

from rest_framework import generics


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'Returned: {len(books)} books',
            "books": serializer_data
        }
        return Response(data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
