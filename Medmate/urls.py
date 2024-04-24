"""
URL configuration for Medmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from base.Views.Auth import *
from base.Views.Common import *
from base.Views.Notify import *
from base.Views.CareTaker import *
# from base.Views.VideoConf import *
from base.Views.Documents import *
from base.Views.Dashboard import *
from base.Views.Shopping import *
# from base.Views.LlmAi import *
from django.views.static import serve
from Medmate import settings
from base.Views.Ocr import *




urlpatterns = [
    path("admin/", admin.site.urls),
]

NotifyUrls = [
    path('add_notify', add_notification, name='add_notify'),
    path('delete_notify/<uuid:notification_id>', delete_notification, name='delete_notify'),
    path('edit_notify/<uuid:notification_id>', edit_notification, name='edit_notify'),
    path('notification', notification, name='notification'),
]

Auth = [
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
]

Home = [
    path('home', home, name='home'),
    path('', home, name='home'),
]

Ocr = [
    path('ocr', extract_text, name='ocr'),
]

admin_ = [
    path('admin/', admin.site.urls),    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

VideoConsult = [
    # path('video_feed', video_feed, name='video_feed'),
    # path('MeetRoom', MeetRoom, name='MeetRoom'),
    path('meeting/', meeting, name='meeting'),
]

DocumetsUrls = [
    # path('chatbot_res', chat, name='chatbot_res'),
    path('add_document', add_document, name='add_document'),
    path('document_list', document_list, name='document_list'),
    path('edit_document/<uuid:document_id>', edit_document, name='edit_document'),
    path('delete_document/<uuid:document_id>', delete_document, name='delete_document'),
]

DocumetsUrls = [
    path('add_document', add_document, name='add_document'),
    path('document_list', document_list, name='document_list'),
    path('edit_document/<uuid:document_id>', edit_document, name='edit_document'),
    path('delete_document/<uuid:document_id>', delete_document, name='delete_document'),
]

medical = [
    path('Shoppingview', Shoppingview, name='Shoppingview'),

]

CareTakerUrl = [
    path('add_caretaker', add_caretaker, name='add_caretaker'),
    path('caretaker_list', caretaker_list, name='caretaker_list'),
    path('caretaker_edit/<uuid:caretaker_id>', caretaker_edit, name='caretaker_edit'),
    path('caretaker_delete/<uuid:caretaker_id>', caretaker_delete, name='caretaker_delete'),
]

e_commerse = [
        path('dash', dash, name='dash'),

]

buy_medicine =[
    path('buymed',buymed,name='buymed'),
    path('medicine',medicine,name='medicine'),
    path('cart',cart,name='cart'),
    path('testimonial',testimonial,name='testimonial'),
    path('chackout',chackout,name='chackout'),
    path('error',error,name='error'),
    path('contact',contact,name='contact'),
]

urlpatterns.extend(Auth)
urlpatterns.extend(Ocr)
urlpatterns.extend(NotifyUrls)
urlpatterns.extend(admin_)
urlpatterns.extend(Home)
urlpatterns.extend(VideoConsult)
urlpatterns.extend(DocumetsUrls)
urlpatterns.extend(medical)
urlpatterns.extend(e_commerse)
urlpatterns.extend(buy_medicine)
urlpatterns.extend(CareTakerUrl)

