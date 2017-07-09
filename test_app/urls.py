from django.conf.urls import url
from views import  RoleUrlView, TestUserView

urlpatterns = [
    url(r'^user/url$', RoleUrlView.as_view()),
    url(r'^user/test$', TestUserView.as_view()),
]
