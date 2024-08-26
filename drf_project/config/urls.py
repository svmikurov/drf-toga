"""URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please
see: https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples
--------
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include,
       path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from drf_app.views import drf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/words/', drf_views.WordListCreateAPIView.as_view()),
    path('api/v1/words/<int:pk>/', drf_views.WordRetrieveUpdateDestroyAPIView.as_view()),  # noqa: E501
    # To quickly add authentication to the browesable api ...
    # https://www.django-rest-framework.org/topics/browsable-api/#authentication
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # End To quickly ...
    # Simple JWT
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#project-configuration
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # End Simple JWT
]
