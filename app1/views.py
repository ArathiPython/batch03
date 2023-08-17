from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes
from rest_framework import *

import json

# Create your views here.
def index(request):
    return render(request,'index.html')

def success_response(response, status_code=None):
        json_obj = {
        "hasError": False,
        "errorCode": -1,
        "message": "Success",
        }
        json_obj["response"] = response
        if status_code is None:
            return Response(json_obj, status=status.HTTP_200_OK)
        return Response(json_obj, status=status_code)
def failure_response(response, status_code=None, error_code=1001, message="can't insert teacher details"):
    json_obj = {
        "hasError": True,
        "errorCode": error_code,
        "message": message,
    }
    json_obj["response"] = response
    if status_code is None:
        return Response(json_obj, status=status.HTTP_200_OK)
    return Response(json_obj, status_code)
class createAccount(APIView): 
    def post(self,request):
            print("helooooooooooooo test1")
            # permission_classes = (permissions.AllowAny,)
            
            datas={}
            response={}
            try:
                user=User()
            
                user.first_name= request.data['fname']
                user.last_name = request.data['lname']
                user.email = request.data['email']
                user.username = request.data['username']
                password = request.data['password']
                user.set_password(password)
               
                user.save() 
                datas={ "NAME": user.first_name,
                        "Email" :  user.email,
                       "Username": user.username,
                        "Password": user.password,
                        
                        }
            except Exception as e:
                return failure_response(response)
        
            response={}
            response['isSuccess'] = True
            response["statusMessage"]='successfully done'
            response["DATA"]=datas
            return success_response(response)    
    
class authlog(APIView):
     def post(self,request):
          data={}  
          response={}
         
          try:
            username=request.data['username']
            password=request.data['password']
            d=authenticate(username=username,password=password)
            print(d,"test1")  
               
            if d is not None:
                    print("hello",d.usernsme)
                    data={
                         "username":d.username,
                         "firstname":d.fist_name,
                         "last name":d.last_name,
                         "email":d.email,
                         "password":d.password,
                    }
                    print(data,"test2")
            else:
                    response['message']='user doesnot exist'
                    return failure_response(response)
          except Exception as e:
                response['message']='message'
                return failure_response(response)
          response={}
          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=d
          return success_response(response)    
def newpage(request):
          return render(request,'newpage.html')