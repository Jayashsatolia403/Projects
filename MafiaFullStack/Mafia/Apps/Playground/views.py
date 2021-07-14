from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import Room
from Apps.User.models import User
from .serializers import PlaygroundSerializer, RoomSerializer

import random

avilableRoles = ['Detective', 'Doctor', 'Mafia', 'Mafia', 'Citizen', 'Citizen', 'Citizen', 'Mafia', 'Mafia', 'Citizen', 'Citizen', 'Citizen', 'SuicideBomber']
minLimitPlayers = 7

@permission_classes((AllowAny,))
class RoomListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer



@api_view(['POST',])
def createRoom(request):
    if request.user.isActive:
        return Response("Please Close Your First Game Before Starting New Game")
    serializer = PlaygroundSerializer(data=request.data, context={'request':request})
    if serializer.is_valid():
        result = serializer.save()
        if result == "Room Already Exists":
            return Response(result)
    else:
        return Response(serializer.errors)
    return Response("Room Created Successfully")

@api_view(['GET',])
def joinRoom(request, roomId):
    try:
        user = request.user
        room = Room.objects.get(roomId=roomId)

        if user in room.players.all():
            return Response("You are Already in!")
        room.players.add(user)
        room.noOfPlayers += 1
        room.save()
        user.save()
        return Response("Joined")
    except:
        return Response("Room Does Not Exists")

@api_view(['GET',])
def leaveRoom(request, roomId):
    try:
        user = request.user
        room = Room.objects.get(roomId=roomId)
        if user not in room.players.all():
            return "You are not in Room!"
        user.isActive = False
        user.role = ""
        room.players.noOfPlayers += 1
        room.players.remove(user)
        room.save()
        user.save()
        return Response("Left")
    except:
        return Response("Room Does Not Exists")

# Number of Something

@api_view(['GET',])
def noOfPlayersInRoom(request, roomId):
    try:
        room = Room.objects.get(roomId=roomId)
        return Response(len(room.players))
    except:
        return Response("Room Does Not Exists")

@api_view(['GET',])
def playerType(request):
    print(request.user.role)
    return Response(request.user.role)


@api_view(['GET',])
def noOfMafiasInRoom(request, roomId):
    try:
        room = Room.objects.get(roomId=roomId)
        return Response(len(room.mafias))
    except:
        return Response("Room Does Not Exists")

@api_view(['GET',])
def noOfCityInRoom(request, roomId):
    try:
        room = Room.objects.get(roomId=roomId)
        return Response(len(room.city))
    except:
        return Response("Room Does Not Exists")

# Players in Room

@api_view(['GET',])
def playersInRoom(request, roomId):
    try:
        print(roomId)
        room = Room.objects.get(roomId=roomId)
        return Response([player.username for player in room.players.all()])
    except:
        return Response("Room Does Not Exists")

@api_view(['GET',])
def hasGameEnded(request, roomId):
    try:
        room = Room.objects.get(roomId=roomId)
        return Response(len(room.city)-len(room.mafias) < 1)
    except:
        return Response("Room Does Not Exists")

@api_view(['GET',])
def isDoctorAlive(request, roomId):
    try:
        room = Room.objects.get(roomId=roomId)
        if room.doctor != None:
            return Response(True)
        return Response(False)
    except:
        return Response("Room Does Not Exists")

@api_view(['GET',])
def isDetectiveAlive(request, roomId):
    try:
        room = Room.objects.get(roomId=roomId)
        if room.detective != None:
            return Response(True)
        return Response(False)
    except:
        return Response("Room Does Not Exists")


@api_view(['GET',])
def killSomeone(request, userId, roomId):
    try:
        room = Room.objects.get(roomId=roomId)
        user = User.objects.get(username=userId)
        user.isKilled = True
        room.save()
        user.save()
        return Response("{} Killed".format(userId))
    except:
        return Response("Room Does Not Exists")

@api_view(['GET',])
def saveSomeone(request, userId, roomId):
    try:
        room = Room.objects.get(roomId=roomId)
        user = User.objects.get(username=userId)

        # print(" >>> Is There Any Issue??")
        
        if user.isKilled == True:
            print(" >>> Is There Any Issue??")
            user.isKilled = False
            user.save()
        else:
            for player in room.players.all():
                print(" >>> Is There Any Issue??")
                if player.isKilled == True:
                    room.noOfPlayers -= 1
                    room.players.remove(player)
                    print(" >>> Is There Any Issue??")
                    
                    if player.role == "Mafia":
                        room.mafias.remove(player)
                    elif player.role == "Detective":
                        room.detective = None
                        room.city.remove(player)
                    elif player.role == "Doctor":
                        room.doctor = None
                        room.city.remove(player)
                    else:
                        room.city.remove(player)
                    
                    player.role = ""
                    player.isActive = False
                    player.isKilled = False
                    player.save()
                    break
        
        room.save()
        user.save()

        return Response("{} Saved".format(user.username))
    except:
        return Response("Room Does Not Exists")



@api_view(['GET',])
def voteOut(request, userId, roomID):
    try:
        room = Room.objects.get(roomId=roomID)
        user = User.objects.get(username=userId)
        room.players.remove(user)

        if user.role == "Mafia":
            room.mafias.remove(user)
        elif user.role == "Detective":
            room.detective = None
            room.city.remove(user)
        elif user.role == "Doctor":
            room.doctor = None
            room.city.remove(user)
        else:
            room.city.remove(user)
        
        user.role = ""
        user.isActive = False

        room.save()
        user.save()

        return Response("User {} Removed".format(user.username))
    except:
        return Response("Room Does Not Exists")




@api_view(['GET',])
def startGame(request, roomId):
    global minLimitPlayers
    try:
        global avilableRoles
        user = request.user
        room = Room.objects.get(roomId=roomId)


        if user == room.owner:
            players = [player for player in room.players.all()]
            room.isFilled = True
            room.isStarted = True

            # if len(players) < 6:
            #     return Response("Can not Start Game For less than 7 Players")

            # print("Yo")

            random.shuffle(players)

            print(players)

            room.detective = players[0]
            room.doctor = players[1]

            for i in range(len(players)):
                players[i].role = avilableRoles[i]
                players[i].isActive = True
                players[i].save()

                if players[i].role == 'Mafia':
                    room.mafias.add(players[i])
                else:
                    room.city.add(players[i])
            
            room.save()
            user.save()
            return Response("Game Started")

        else:
            return Response("Only Owner Can Start Game")
        
    except:
        return Response("Room Does Not Exists")