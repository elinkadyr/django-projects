"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from account.views import RegisterUserAPIView
from post.views import (create_post, delete_post, post_details, posts_list,
                        posts_list_api_view, update_post)
from review.views import (CreateCommentAPIView, DeleteCommentAPIView,
                          UpdateCommentAPIView, toggle_like)

schema_view = get_schema_view(
    openapi.Info(
        title="Python 27 API",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing/', posts_list),
    path('api/listing/', posts_list_api_view),
    path('api/details/<int:id>/', post_details),
    path('api/create/', create_post),
    path('api/delete/<int:id>/', delete_post),
    path('api/update/<int:id>/', update_post),
    path('api/like/<int:id>/', toggle_like),
    path('api/register/', RegisterUserAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/comment/create/', CreateCommentAPIView.as_view()),
    path('api/comment/update/<int:pk>/', UpdateCommentAPIView.as_view()),
    path('api/comment/delete/<int:pk>/', DeleteCommentAPIView.as_view()),
    path('docs/', schema_view.with_ui('swagger')),
]

