from django.urls import path
import api_basic
from .views import article_list, article_detail
from .class_views import ArticleView,ArticleDetail

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', article_detail),
    path ('article_class/',ArticleView.as_view()),
    path('details_class/<int:pk>',ArticleDetail.as_view())
]
