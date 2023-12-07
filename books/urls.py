from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView, BookListCreateApiView, BookUpdateDeleteView, BookDetailView, BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    # path('books/', BookListApiView.as_view(), ),
    # path('book_create/', BookListCreateApiView.as_view(), ),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteView.as_view(), ),
    # path('books/<int:pk>/', BookDetailView.as_view(), )
]

urlpatterns = urlpatterns+router.urls
