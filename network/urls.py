
from django.urls import path
from django.conf.urls.static import static


from project4 import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createPost", views.createPost, name="createPost"),
    path("newPost",views.newPost, name="newPost"),
    path("profile/<int:user_id>",views.profile, name="profile"),
    path("unfollow", views.unfollow, name="unfollow"),
    path("follow", views.follow, name="follow"),
    path("following",views.following,name="following"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("remove_like/<int:post_id>", views.remove_like, name="remove_like"),
    path("add_like/<int:post_id>", views.add_like, name="add_like"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
