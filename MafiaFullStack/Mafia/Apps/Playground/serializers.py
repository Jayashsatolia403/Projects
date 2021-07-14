from requests.models import Response
from rest_framework import serializers

from .models import Room


class PlaygroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['roomId']
    
    def save(self):
        newRoomId = self.validated_data['roomId']

        # try:
        #     Room.objects.get(roomId=newRoomId)
        #     return "Room Already Exists"
            
        # except:
        newRoom = Room(
            roomId = newRoomId
        )

        user = self.context['request'].user

        newRoom.owner = user

        newRoom.save()

        user.isActive = True

        newRoom.players.add(self.context['request'].user)
        newRoom.noOfPlayers = 1
        
        
        newRoom.save()
        return newRoom


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'