from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, MyList, RespondDelete, RespondDetail, accept_respond, RespondCreate, send_mailing


urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('my/', MyList.as_view(), name='my'),
    path('my/<int:pk>/', RespondDetail.as_view(), name='respond_detail'),
    path('my/<int:pk>/delete/', RespondDelete.as_view(), name='respond_delete'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('accept_respond/<int:pk>/<str:user>/', accept_respond, name='accept_respond'),
    path('add_respond/<int:pk>/<str:user>/', RespondCreate.as_view(), name='respond_create'),
    path('send_mailing/', send_mailing, name='send_mailing')
    ]
