from django.urls import path

from apps.my_app.views import (
    indexView,
    postFriend,
    updateFriend,
    checkSlateID,
    FriendView
)

urlpatterns = [
    path('', indexView),
    path('post/ajax/friend', postFriend, name="post_friend"),
    path('put/ajax/update', updateFriend, name="update_friend"),
    path('get/ajax/validate/slate_id', checkSlateID, name="validate_slate_id"),
    path("cbv/", FriendView.as_view(), name="friend_cbv")
]
