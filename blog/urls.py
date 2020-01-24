from django.urls import path
from .views import home,rules,admn,DealListView,DealDetailView


urlpatterns=[

path('',home,name='home'),
path('rules/',rules,name='rules'),
path('admn/',admn,name='admn'),
path('deal/',DealListView.as_view(),name='deal-all'),
path('deal/<int:pk>',DealDetailView.as_view(),name='deal-single'),


]
