from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreListView,
    GenreDetail,
    CinemaHallListview,
    MovieViewSet,
    ActorListView,
    ActorDetailView,
)

cinema_hall_list = CinemaHallListview.as_view(
    actions={
        "get": "list",
        "post": "create"}
)
cinema_hall_detail = CinemaHallListview.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreListView.as_view(),
         name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(),
         name="genre-detail"),
    path("actors/", ActorListView.as_view(),
         name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(),
         name="actor-detail"),
    path("cinema_halls/", cinema_hall_list,
         name="cinema-hall-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail,
         name="cinema-hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
