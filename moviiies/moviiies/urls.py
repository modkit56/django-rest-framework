from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('moviiies_app.api.urls'))
]
