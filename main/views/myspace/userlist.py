from rest_framework.permissions import IsAuthenticated

from main.models.player.player import Player
from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        # players = Player.objects.all().exclude(photo="https://img2.baidu.com/it/u=2161949891,656888789&fm=26&fmt=auto").order_by('id')[:10]
        players = Player.objects.all().order_by('id')[:10]
        users = []
        for player in players:
            users.append({
                'id': player.user.id,
                'username': player.user.username,
                'photo': player.photo,
                'followerCount': player.followerCount
            })
        return Response(users)