from rest_framework import serializers

def create_media(media_arr, media_model):
    media_li = []
    for media in media_arr:
        media_type = media.split("|")[0].lower()
        source = media.split("|")[1]
        media_types = ["picture", "video", "gif"]

        if media_type not in media_types:
            raise serializers.ValidationError(detail="Invalid media type", code=400)

        new_media = media_model.objects.create(type=media_type, source=source)
        new_media.save()
        media_li.append(str(new_media.pk))
    return media_li
