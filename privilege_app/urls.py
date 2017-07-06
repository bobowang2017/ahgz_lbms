from django.conf.urls import url
from views import PrivilegeView

urlpatterns = [
    url(r'^privilege$', PrivilegeView.as_view()),
]
