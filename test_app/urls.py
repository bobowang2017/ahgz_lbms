from django.conf.urls import url
from views import UserView, RoleUrlView, TestUserView

urlpatterns = [
    url(r'^user$', UserView.as_view()),
    url(r'^user/url$', RoleUrlView.as_view()),
    url(r'^user/test$', TestUserView.as_view()),
]
