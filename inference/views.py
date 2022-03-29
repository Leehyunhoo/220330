from .config import Config
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from google.cloud import storage
import os

# Create your views here.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            file = request.data["image"]
            storage_client = storage.Client.from_service_account_json(Config.JSON)
            bucket = storage_client.get_bucket(Config.BUCKET_NAME)
            blob = bucket.blob(file.name)
            save_dir=os.path.join(Config.SAVE_FILE_DIR,file.name)
            with open(save_dir, "rb") as my_file:
              blob.upload_from_file(my_file)
            if os.path.isfile(save_dir):
                os.remove(save_dir)
            url = blob.public_url
            print(url)
            return Response(url, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)