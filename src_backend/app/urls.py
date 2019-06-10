from django.urls import re_path
from .views import NumericAPIView


urlpatterns = [
    re_path(r'^$', NumericAPIView.as_view())
]
