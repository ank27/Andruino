from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import django.views.decorators.csrf
from MyApplication.models import *
import json
import simplejson
from django.http import HttpResponse


@django.views.decorators.csrf.csrf_exempt
def register_success(request):
    if request.POST:
        if (request.POST.get("username"))=="" or (request.POST.get("email"))=="" or (request.POST.get("contact"))=="" or (request.POST.get("password"))=="":
            return HttpResponse(json.dump({"status":"401", }),content_type='application/json')
        else:
            userName=request.POST.get("username")
            userEmail=request.POST.get("email")
            userContact=request.POST.get("contact")
            userPassword=request.POST.get("password")
            UserInfo.objects.create(user_name=userName,user_email=userEmail,user_contact=userContact,user_password=userPassword)
        # return HttpResponse(json.dumps({"status":"200",},{"result":"done"}),content_type='application/json')
            return HttpResponse("200",content_type='application/json')
        # data ={"status":"200","encodin"}
        # return HttpResponse("test", content_type='application/json')


def login_success(request):
     if (request.POST.get("email"))=="" or (request.POST.get("password"))=="":
         return HttpResponse(json.dump({"status":"401"}),content_type='application/json')
     else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=UserInfo.objects.get(user_email=email)
        if(user.user_password_detail()==password):
            return HttpResponse("200",content_type='application/json')


# topic_data={} is tuple, a tuple is written as key value pair
# like topic_data["key"]= value and it shown in json as jsonObject
# to send jsonArray use arraylist  like subtopic_data=[]
# and append values in arraylist like subtopic_data.append(t) or topic_data.append('topicname':topicname)
# see below function


def get_topic(request):
    data3={}
    topic_data=[]
    subtopic=[]
    topic=TopicInfo.objects.all()
    for t in topic:
        name=t.topic_name
        active=t.is_active
        if active:
            data2=SubTopic.objects.filter(topic__topic_name = name)
            for da in data2:
                subtopic.append({'name':da.subTopic_name, 'is_active':da.subTopic_isactive, 'theory':da.isTheory_active,'question':da.isQuestion_active, 'formula':da.isFormula_active})
            topic_data.append({'id':t.id,'topic_name':name,'is_active':active,'image':str(t.topic_image), 'sub_topic': subtopic})
            subtopic=[]
            data3["topic"]=topic_data
    serial_json=simplejson.dumps(data3)
    return HttpResponse(serial_json, content_type='application/json')




def send_json_string(request):
    string_json={"meta": {"offset": 0, "limit": 12, "previous": "null", "total_count": 2, "next": "null"}, 
                 "objects": [{"image": "/static/no_image.jpg", 
                              "variations": [{"variations": 
                                                  [{"sellers": [{"discount": 0.0, "price_per_piece": 58.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 63, "show_percentage": "false", "seller_id": 3, "price": 580.0}, 
                                                                {"discount": 0.0, "price_per_piece": 58.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 107, "show_percentage": "false", "seller_id": 5, "price": 580.0}, 
                                                                {"discount": 0.0, "price_per_piece": 58.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 154, "show_percentage": "false", "seller_id": 4, "price": 580.0}], 
                                                    "max_price_per_piece": 58.0, "size": "10 x 1.0 Ltr", "quantity": 10, "min_price_per_piece": 58.0, "flag": 1, "size_only": "1.0 Ltr", "price_range": "Rs. 580.0 - Rs.580.0", "psiid": 65}, 
                                                   {"sellers": [{"discount": 0.0, "price_per_piece": 60.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 64, "show_percentage": "false", "seller_id": 3, "price": 60.0}, 
                                                                {"discount": 0.0, "price_per_piece": 60.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 108, "show_percentage": "false", "seller_id": 5, "price": 60.0}, 
                                                                {"discount": 0.0, "price_per_piece": 60.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 155, "show_percentage": "false", "seller_id": 4, "price": 60.0}], 
                                                    "max_price_per_piece": 60.0, "size": "1.0 Ltr", "quantity": 1, "min_price_per_piece": 60.0, "flag": 0, "size_only": "1.0 Ltr", "price_range": "Rs. 60.0 - Rs.60.0", "psiid": 66}], "size": "1.0 Ltr", "price_range": "58.0-60.0"}, 
                                             {"variations": [{"sellers": [{"discount": 0.0, "price_per_piece": 840.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 65, "show_percentage": "false", "seller_id": 3, "price": 8400.0},
                                                                          {"discount": 0.0, "price_per_piece": 58.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 107, "show_percentage": "false", "seller_id": 5, "price": 580.0},
                                                                          {"discount": 0.0, "price_per_piece": 840.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 109, "show_percentage": "false", "seller_id": 5, "price": 8400.0},
                                                                          {"discount": 0.0, "price_per_piece": 840.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 156, "show_percentage": "false", "seller_id": 4, "price": 8400.0}],
                                                              "max_price_per_piece": 840.0, "size": "10 x 15.0 Ltr", "quantity": 10, "min_price_per_piece": 840.0, "flag": 1, "size_only": "15.0 Ltr", "price_range": "Rs. 8400.0 - Rs.8400.0", "psiid": 67},
                                                             {"sellers": [{"discount": 0.0, "price_per_piece": 860.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 66, "show_percentage": "false", "seller_id": 3, "price": 860.0},
                                                                          {"discount": 0.0, "price_per_piece": 60.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 108, "show_percentage": "false", "seller_id": 5, "price": 60.0}, {"discount": 0.0, "price_per_piece": 860.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 110, "show_percentage": "false", "seller_id": 5, "price": 860.0}, {"discount": 0.0, "price_per_piece": 860.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 157, "show_percentage": "false", "seller_id": 4, "price": 860.0}], "max_price_per_piece": 860.0, "size": "15.0 Ltr", "quantity": 1, "min_price_per_piece": 860.0, "flag": 0, "size_only": "15.0 Ltr", "price_range": "Rs. 860.0 - Rs.860.0", "psiid": 68}], "size": "15.0 Ltr", "price_range": "840.0-860.0"}, {"variations": [{"sellers": [{"discount": 0.0, "price_per_piece": 800.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 112, "show_percentage": "false", "seller_id": 5, "price": 8000.0}, {"discount": 0.0, "price_per_piece": 58.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 154, "show_percentage": "false", "seller_id": 4, "price": 580.0}, {"discount": 0.0, "price_per_piece": 840.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 156, "show_percentage": "false", "seller_id": 4, "price": 8400.0}, {"discount": 0.0, "price_per_piece": 800.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 159, "show_percentage": "false", "seller_id": 4, "price": 8000.0}], "max_price_per_piece": 800.0, "size": "10 x 15.0 Kg", "quantity": 10, "min_price_per_piece": 800.0, "flag": 1, "size_only": "15.0 Kg", "price_range": "Rs. 8000.0 - Rs.8000.0", "psiid": 99}, {"sellers": [{"discount": 0.0, "price_per_piece": 825.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 111, "show_percentage": "false", "seller_id": 5, "price": 825.0}, {"discount": 0.0, "price_per_piece": 60.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 155, "show_percentage": "false", "seller_id": 4, "price": 60.0}, {"discount": 0.0, "price_per_piece": 860.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 157, "show_percentage": "false", "seller_id": 4, "price": 860.0}, {"discount": 0.0, "price_per_piece": 825.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 158, "show_percentage": "false", "seller_id": 4, "price": 825.0}], "max_price_per_piece": 825.0, "size": "15.0 Kg", "quantity": 1, "min_price_per_piece": 825.0, "flag": 0, "size_only": "15.0 Kg", "price_range": "Rs. 825.0 - Rs.825.0", "psiid": 98}], "size": "15.0 Kg", "price_range": "800.0-825.0"}], "category": 41, "vat": 0, "name": "Regular Palm Oil", "product_id": 59}, {"image": "/static/no_image.jpg", "variations": [{"variations": [{"sellers": [{"discount": 0.0, "price_per_piece": 870.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 113, "show_percentage": "false", "seller_id": 5, "price": 870.0}], "size": "15.0 Ltr", "quantity": 1, "flag": 0, "size_only": "15.0 Ltr", "price_range": "Rs. 870.0", "psiid": 100}], "size": "15.0 Ltr", "price_range": "Rs. 870.0"}, {"variations": [{"sellers": [{"discount": 0.0, "price_per_piece": 68.0, "show_saving": "false", "savings": 0.0, "max_buy": 100, "spid": 114, "show_percentage": "false", "seller_id": 5, "price": 68.0}], "size": "1.0 Ltr", "quantity": 1, "flag": 0, "size_only": "1.0 Ltr", "price_range": "Rs. 68.0", "psiid": 101}], "size": "1.0 Ltr", "price_range": "Rs. 68.0"}], "category": 41, "vat": 0, "name": "Yog Palm Oil", "product_id": 87}]}
    n=simplejson.dumps(string_json)
    return HttpResponse(n, content_type='application/json')

# def send_topic_old(request):
#     topic_data={}
#     subtopic_data=[]
#     str1 = ''
#     t={}
#     data=TopicInfo.objects.all()
#     for d in data:
#         topicname=d.topic_name
#         active=d.is_active
#         if active:
#             print active
#             data2=SubTopic.objects.filter(topic__topic_name = topicname)
#             for da in data2:
#             str1 = str1 + da.subTopic_name + ', '
                # subtopicname=da.subTopic_name
                # subtopicactive=da.subTopic_isactive
                # theory=da.isTheory_active
                # question=da.isQuestion_active
                # formula=da.isFormula_active
                # t["name"]=subtopicname
                # t["is_active"]=subtopicactive
                # t["theory"]=theory
                # t["question"]=question
                # t["formula"]=formula
                # subtopic_data.append(t)
                # t={}
            # topic_data["topic_name"]=topicname
            # topic_data["is_active"]=active
            # topic_data["sub_topic"]=subtopic_data
            # topic_data.append({'topic_name':topicname,'is_active':active, 'sub_topic': subtopic_data})
            # subtopic_data=[]
    # serial_json=simplejson.dumps(topic_data)
    # return HttpResponse(serial_json, content_type='application/json')