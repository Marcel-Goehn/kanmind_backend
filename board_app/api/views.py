from rest_framework.viewsets import ModelViewSet
from models import Board
from rest_framework.permissions import IsAuthenticated
from .serializers import BoardSerializer

class BoardView(ModelViewSet):
    queryset = Board
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]