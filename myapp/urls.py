from django.urls import path
from myapp import views
app_name="myapp"
urlpatterns=[
    path('sample1/<data>',views.sample2,name="sample1"),
    path('sample3/',views.sample2,name="sample3"),
]