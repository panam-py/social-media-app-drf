from django.urls import path


from .views import PostCreateListView
from .views import PostDetail

urlpatterns = [
    path('', view=PostCreateListView.as_view(), name='Create_and_list_posts'),
    path('<str:pk>', view=PostDetail.as_view(), name='Update_delete_and_retrieve_post')
]