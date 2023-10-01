from .models import Book
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status



class BooksList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['genre', 'condition', 'available']
    search_fields  = ['title']
    
class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]
    

@api_view(['post'])
@permission_classes([IsAuthenticated])
def request_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    if not request.user in book.is_interested.all():
        book.is_interested.add(request.user)
        return Response({"message": "Your request has been received"}, status=status.HTTP_200_OK)
    return Response({"message": "You can not request twice"}, status=status.HTTP_400_BAD_REQUEST)