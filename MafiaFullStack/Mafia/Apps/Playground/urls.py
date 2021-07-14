from django.db.models.query import ValuesIterable
from django.urls import path

from .views import playerType, playersInRoom, joinRoom, RoomListView, createRoom, leaveRoom, noOfPlayersInRoom, noOfMafiasInRoom, noOfCityInRoom, hasGameEnded, isDetectiveAlive, isDoctorAlive, killSomeone, saveSomeone, startGame, voteOut


urlpatterns = [
    path('', RoomListView.as_view()),
    path('playerType/', playerType, name='playerType'),
    path('createRoom/', createRoom, name='createRoom'),
    path('<roomId>/joinRoom/', joinRoom, name='joinRoom'),
    path('<roomId>/leaveRoom/', leaveRoom, name='leaveRoom'),
    path('<roomId>/playersInRoom/', playersInRoom, name='playersInRoom'),
    path('<roomId>/noOfPlayersInRoom/', noOfPlayersInRoom, name='noOfPlayersInRoom'),
    path('<roomId>/noOfMafiasInRoom/', noOfMafiasInRoom, name='noOfMafiasInRoom'),
    path('<roomId>/noOfCityInRoom/', noOfCityInRoom, name='noOfCityInRoom'),
    path('<roomId>/hasGameEnded/', hasGameEnded, name='hasGameEnded'),
    path('<roomId>/isDoctorAlive/', isDoctorAlive, name='isDoctorAlive'),
    path('<roomId>/isDetectiveAlive/', isDetectiveAlive, name='isDetectiveAlive'),
    path('<userId>/<roomId>/killSomeone/', killSomeone, name='killSomeone'),
    path('<userId>/<roomId>/saveSomeone/', saveSomeone, name='saveSomeone'),
    path('<userId>/<roomId>/voteOut/', voteOut, name='voteOut'),
    path('<roomId>/startGame/', startGame, name='startGame'),
]