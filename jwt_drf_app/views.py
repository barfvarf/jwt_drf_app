from jwt_drf_app.serializers import UserSerializer
from jwt_drf_app.serializers import PostSerializer
from jwt_drf_app.models import Post
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SignupUser(APIView):
    """
    Creates a new user via a POST request
    """

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": ("A user has been created; send POST "
                                         "api/token/  with 'username' and "
                                         "'password' to get access token.")},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatePost(APIView):
    """
    Creates a new post via a POST request.
    Requires user authentication.
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePost(APIView):
    """
    Updates likes count of a post via a POST request.
    Requires user authentication.
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, post_action, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"message": "Post id %s does not exist." % pk},
                            status=status.HTTP_404_NOT_FOUND)
        if post_action in (PostActions.Like, PostActions.Dislike):
            if post_action == PostActions.Like:
                data = {"likes_count": post.likes_count + 1}
            elif post_action == PostActions.Dislike:
                data = {"likes_count": post.likes_count - 1}
            serializer = PostSerializer(post, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Invalid post action."},
                        status=status.HTTP_400_BAD_REQUEST)


class PostActions(object):
    Like = "like"
    Dislike = "dislike"
