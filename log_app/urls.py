from django.conf.urls import url
from views import LogTestView

urlpatterns = [
    url(r'^log', LogTestView.as_view()),
]
