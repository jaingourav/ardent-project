from django.urls import path
from . import views

urlpatterns=[
    path('',views.test),
    path('home',views.home),
    path('second',views.second),
    path('third',views.third),
    path('forth',views.forth),
    path('demo',views.demo),
    path('form',views.form),
    path('insert',views.insert),
    path('customer1',views.customer1),
    path('ins',views.ins),
    path('display',views.display),
    path('del/<int:id>',views.dele),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>',views.edcode),
    
]