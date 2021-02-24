from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from .views import article_list, article_detail
# from .views import ArticleList, ArticleDetail
from .views import ArticleViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    # path('articles/<int:pk>', article_detail),
    # path('articles', article_list),
    # path('articles/<int:id>/', ArticleDetail.as_view()),
    # path('articles/', ArticleList.as_view()),
    path('', include(router.urls))
]
