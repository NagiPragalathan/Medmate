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
from base.Views.doctor import *
from base.Views.HeartRate import *
from base.Views.Ecommerce import *




urlpatterns = []

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
    path('documents', documents, name='documents'),

]

CareTakerUrl = [
    path('add_caretaker', add_caretaker, name='add_caretaker'),
    path('caretaker_list', caretaker_list, name='caretaker_list'),
    path('caretaker_edit/<uuid:caretaker_id>', caretaker_edit, name='caretaker_edit'),
    path('caretaker_delete/<uuid:caretaker_id>', caretaker_delete, name='caretaker_delete'),
]

e_commerse = [
        path('dash', dash, name='dash'),
        path('prescription/', prescription, name='prescription'),
        path('report/', report, name='report'),
        path('reportview/',viewreport,name='viewreport'),
        path('viewpres/', viewprescription, name='viewprescription'),
        path('Addpres/', Addprescription, name='Addprescription'),
        path('Addreport/', Addreport, name='Addreport'),
        path('profile/', profile, name='profile'),
        path('calendar/', calendar, name='calendar'),
        path('create_or_update_user_profile', create_or_update_user_profile, name='create_or_update_user_profile'),

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

doctorUrl = [
    path('doctor-list',DoctorList,name='DoctorList'),
    path('show_data',show_data,name='show_data'),
]

heart_rate = [
    path('rate',get_rate,name='get_rate'),
    path('heat_sen',sensor_data_stream,name='sensor_data_stream'),
]
ratingurl =[
    path('rating',rating,name='rating'),
]
Messages=[
        path('messages',messages,name='messages'),
        path('consultmsg',consultmsg,name='consultmsg'),
]
EProducts = [
    path('add_product', add_product, name='add_product'),
    path('list_product', list_products, name='list_products'),
    path('edit_product<uuid:id>/', edit_product, name='edit_product'),
    path('delete_product<uuid:id>/', delete_product, name='delete_product'),
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
urlpatterns.extend(doctorUrl)
urlpatterns.extend(CareTakerUrl)
urlpatterns.extend(ratingurl)
urlpatterns.extend(Messages)
urlpatterns.extend(heart_rate)
urlpatterns.extend(EProducts)

