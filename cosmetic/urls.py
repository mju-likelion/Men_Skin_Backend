from django.urls import path, include
from . import views
from .views import BoardViewSet , CommentViewSet , RankViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import urls

router = DefaultRouter()
router.register('board', BoardViewSet , basename='board')
router.register('comment', CommentViewSet, basename='comment') # (댓글)
router.register('rank', RankViewSet, basename='rank')      

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('',include(router.urls))
 ]
 
