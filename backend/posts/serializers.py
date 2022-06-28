from django.http import JsonResponse
from rest_framework import serializers
from django.forms import model_to_dict


from .models import Post, Media
from .utils import create_media
from comments.models import Comment

class PostSerializer(serializers.ModelSerializer):
    text_content = serializers.CharField(max_length=500000)
    media = serializers.CharField(max_length=3000)
    comments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('reactions', 'date_posted', 'owner')

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj.pk)
        comments_li = [model_to_dict(comment) for comment in comments]
        return comments_li

    def create(self, validated_data):
        user = None
        media = validated_data['media']
        media_arr = media.split(',')
        media_li = create_media(media_arr, Media)

        request = self.context.get("request")
        
        if request and hasattr(request, 'user'):
            user = request.user
            print("USER PK!!!!", user.pk)
        else:
            return JsonResponse(data={'detail': 'No user is logged in'})


        post = Post.objects.create(owner=user, reactions=[''], text_content=validated_data['text_content'], media=[media for media in media_li])
        
        post.save()

        return post
