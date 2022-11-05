from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from main.models.myspace.post import Post


class LogoutView(APIView):

    def get(self, request):
        user = request.user
        user_id = int(request.GET.get('user_id', 1))
        posts = Post.objects.filter(user_id=user_id).order_by('-pk')
        data = []
        for post in posts:
            data.append({
                'id': post.id,
                'content': post.content,
            })
        return Response(data)