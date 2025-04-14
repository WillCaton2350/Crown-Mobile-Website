from django.urls import path
from .views import index_view

urlpatterns = [
    path('',index_view.index,name='index'),
    path('index.html',index_view.index,name='index'),
    path('about.html',index_view.about,name='about'),
    path('contact.html', index_view.contact, name='contact'),
    path('subscribe.html',index_view.subscribe,name='subscribe'),
    path('unsubscribe.html',index_view.unsubscribe,name='unsubscribe'),
    path('socials.html',index_view.socials,name='socials'),
    path('careers.html',index_view.careers,name='careers'),

]
