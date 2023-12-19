from django.contrib import admin

# add include
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # add website urls
    path(
        "",
        include("website.urls"),
    ),
]
