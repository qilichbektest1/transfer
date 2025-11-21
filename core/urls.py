from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name = 'home'),
    path('clubs/', ClubsView.as_view(),name = 'clubs'),
    path('clubs/<int:pk>/details/', ClubDetailsView.as_view(),name = 'club-details'),
    path('about/', AboutView.as_view(),name = 'about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
