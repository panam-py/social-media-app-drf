from rest_framework import generics
from rest_framework.response import Response


from .models import Post, Media
from .serializers import PostSerializer
from .permissions import HasAccessToObject
from .utils import create_media

class PostCreateListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = []
    http_method_names = ['get', 'patch', 'delete']

    def get_permissions(self):
        if self.request.method != 'GET':
            self.permission_classes.append(HasAccessToObject)
        return super().get_permissions()

    def perform_update(self, serializer):
        post_instance = self.get_object()
        request_body = self.request.data

        if 'text_content' in request_body.keys():
            new_content = request_body['text_content']
            updated_instance = serializer.save(text_content=new_content)

        if 'remove_media' in request_body.keys():
            media = request_body['remove_media'].split(",")

            for id in media:
                med = Media.objects.filter(pk=id)

                if med:
                    med.delete()
                    new_media_list = post_instance.media
                    print(new_media_list)
                    new_media_list.remove(str(id))
                    updated_instance = serializer.save(media=new_media_list)

        if 'add_media' in request_body.keys():
            media_arr = request_body['add_media'].split(",")
            media_li = create_media(media_arr, Media)

            for media_id in post_instance.media:
                media_li.append(media_id)
            
            updated_instance = serializer.save(media=media_li)

        if 'add_media' not in request_body.keys() and 'remove_media' not in request_body.keys() and 'text_content' not in request_body.keys():
            return Response(data={'detail': 'No data found to update'}, status=400)


        return updated_instance
