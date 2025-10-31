from rest_framework import serializers
from models import Board

class BoardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Board
        fields = ["id", "title", "member_count", "ticket_count", "tasks_to_do_count", "tasks_high_priority_count", "owner_id", "members"]
        read_only_fields = ["id"]