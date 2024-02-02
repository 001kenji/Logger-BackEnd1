from django.shortcuts import render,HttpResponse
from django.template import loader
from .sterializer import UserSterializer
from .models import User

import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.

@api_view(['GET'])
def viewUser (request):


    userdata = User.objects.all()
    dataview = UserSterializer(userdata, many=True)

    return Response(dataview.data)

@api_view(['GET', 'POST', 'PUT'])
def Write(request):
 
    if request.method == 'POST':
        print('called in POST method')
        data = json.loads(request.body.decode("utf-8"))
        #print('data is', data)
        #print(data)
        mydata = User.objects.filter(name=data['name'],password=data['password']).values()
        
        datadisp = UserSterializer(mydata, many=True)
        print(datadisp.data)
        if mydata :
            content = {
                'found' : True,
                'profile' : datadisp.data,
                'position': mydata[0]['id']
            }
            
            return JsonResponse(json.dumps(content), safe=False)
            
        content = {
                'found' : False
            }
        return JsonResponse(json.dumps(content), safe=False)

    if request.method == 'PUT':
        print('called in PUT method')
        data = json.loads(request.body.decode("utf-8"))
        #print(data)
        mydata = User.objects.filter(name=data['name'],password=data['password']).values()
        
        if len(mydata) > 0 :
            print(len(mydata))
            content = {
                'exists' : True,
            }
            return JsonResponse(json.dumps(content), safe=False)
        
        elif len(mydata) == 0:
            newUser = User(name= data['name'],password= data['password'], email = data['email'])
            newUser.save()
            print('written')
            content = {
                'exists': False,
                'response' : 'success'
            }
            return JsonResponse(json.dumps(content), safe=False)




@api_view(['POST'])
def Board(request) :

    userposition = User.objects.all().values()
    print(userposition)
    homepage = loader.get_template('homepage.html')
    print('in dash board now')
    return HttpResponse(homepage.render())
