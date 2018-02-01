from django.conf.urls import url, include
from . import views

app_name = 'newsletter'

urlpatterns = [
    url(r'^signup/newsletter?', views.NewsletterView.as_view(), name='signup'),
]
