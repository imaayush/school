from django.conf.urls import url
from class_room.views import (UserList,
                              RegisterUser,
                              UserLogin,
                              SubjectList,
                              SubjectDetail,
                              ClassList,
                              ClassDetail)

urlpatterns = [
    url(r"^api/v1/user/login/", UserLogin.as_view(), name="user-login"),
    url(r"^api/v1/users/", UserList.as_view(), name="users"),
    url(r"^api/v1/user/", RegisterUser.as_view(), name="register-user"),
    url(r"api/v1/subjects/(?P<pk>\d+)/", SubjectList.as_view(), name="subject-details"),
    url(r"api/v1/subjects/", SubjectList.as_view(), name="subjects"),
    url(r"api/v1/classes/(?P<pk>\d+)/", ClassDetail.as_view(), name="class-details"),
    url(r"api/v1/classes/", ClassList.as_view(), name="classes"),

]