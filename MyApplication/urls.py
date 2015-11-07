from django.conf.urls import url
from MyApplication import views,app_views,arduino_views

urlpatterns=[
     # url(r'^$', views.index, name='index'),
     url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
     url(r'^(?P<question_id>[0-9]+)/result/$',views.result,name='results'),
     url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),




     # From Web
     url(r'^$', views.index, name='index'),
     url(r'^register/$',views.user_register,name='register'),
     url(r'^register_done/$',views.register_submit,name='register_submit'),
     url(r'^login/$',views.user_login),

     # url's name should be declared in html files onClick event. when html form is called it look for
     # name in this url and then the url is controlled by views.request_home function
     url(r'^home/$',views.request_home,name='login_submit'),

     url(r'^networks/$', views.network, name='networks'),
     url(r'^base/$', views.base, name='base'),



     # ======================for minoavate===========================================================#####
     url(r'^index/$',arduino_views.send_binary_values,name='led_switch'),
     url(r'^my_login/$',views.login_minovate,name='login'),
     url(r'^my_signup/$',views.signup_minovate,name='signin'),
     url(r'^forget_password/$',views.forget_password,name="forgetpwd"),


     # From App
     url(r'^app/registration/$',app_views.register_success,name='register_success'),
     url(r'^app/login/$',app_views.login_success,name='login_success'),
     url(r'^app/topics/$',app_views.get_topic,name='get_topics'),
     url(r'^app/get_values/$',app_views.send_json_string,name='send_json_string'),



     #####################Arduino#########################################
     url(r'^send_binary_data/',arduino_views.send_binary_values,name='led_switch'),
     url(r'^send_data/$',arduino_views.send_data, name="send_data"),

     #App
     url(r'^app/app_data/$',arduino_views.app_data,name='get_topics'),
     url(r'^app/get_data/$',arduino_views.send_app_data,name='send_app_data'),
     url(r'^app/send_values/$',arduino_views.get_app_data,name='get_app_data'),
]
