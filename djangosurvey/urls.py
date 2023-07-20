from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path('', include('polls.urls', namespace='polls')),
    path('admin/', admin.site.urls),
]
