from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('Dashboard/', views.searchV, name="dashboard"),
    path('mrsearch/', views.mrsearchV, name="mrsearch"),
    path('sms/<int:id>', views.smsV, name="sms"),
    path('mr/number/<int:id>', views.CreportV, name="mrno"),
]