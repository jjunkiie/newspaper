from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, ArticleCreate, ArticleUpdate, ArticleDelete


urlpatterns = [

   path('news/', PostsList.as_view(), name='posts'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/create/', ArticleCreate.as_view(), name='article_create'),
   path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('welcome/', Welcome.as_view(), name='welcome'),
   

]