from django.urls import path
from .views import home, store_detail


app_name = 'stores'
urlpatterns = [
    path('', home, name='home'),
    path('<slug:store_name>/', store_detail, name='store_detail')
]