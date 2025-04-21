
import json
from typing import List
from django.http import JsonResponse
from django.shortcuts import render
from ninja import File, NinjaAPI

from user.Schemas import ProductGetSchema, ReviewGetSchema
from .models import *




api = NinjaAPI(urls_namespace='api-v1')
import jwt
from django.conf import settings
from datetime import datetime, timedelta ,timezone
# from datetime import datetime, timedelta, timezone
SECRET_KEY = "django-insecure-*(@t@qvt7eg$k^yw(8i-wchu2s%v%(u=yo5rgf3+*c$ad7&z8t"

ALGORITHM = "HS256"

def create_jwt_token(data: dict, expires_in: int = 1):
    payload = data.copy() if isinstance(data, dict) else {"user": data}
    payload["exp"] = datetime.now(timezone.utc) + timedelta(days=expires_in)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def give_raw_data(request):
    return request.body.decode('utf-8')

@api.post('createUser')
def createUser(request):
    try:
        raw_body=give_raw_data(request)
        if not raw_body:
            return JsonResponse({"error": "Empty body"}, status=400)

        data = json.loads(raw_body)
        username = data.get('username')
        if not username:
            return JsonResponse({"error": "Missing 'username'"}, status=400)

        Customer.objects.create(name=username)
        return JsonResponse({"message":"Successfully created"},status=201)
        # token = create_jwt_token({'username': username})
        # return {"token": token}
        
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

@api.post("login_customer")
def login_customer(request):
    raw_body=give_raw_data(request)
    data = json.loads(raw_body)
    
    username=data['username']
    try:
     user=Customer.objects.get(name=username)
     token = create_jwt_token({'username': username})
     return {"token": token}
    except Customer.DoesNotExist:
        raise HttpError(404,"NO Customer Found")
    
    


    

def decode_jwt_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
from ninja.security import HttpBearer
class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        payload = decode_jwt_token(token)
        if payload:
            return payload
        return None

auth = JWTAuth()

from ninja.errors import HttpError

@api.post('add_customer_review',auth=auth)
def add_customer_review(request):
    raw_body=give_raw_data(request)
    raw_body=json.loads(raw_body)
    rating=raw_body['rating']
    review=raw_body['review']
    userid=raw_body['userid']
    pro_id=raw_body['pro_id']
    try:
        product=Product.objects.get(id=int(pro_id))
        user=Customer.objects.get(id=int(userid))
    except Product.DoesNotExist:
        raise HttpError(404,"NO Product Found")
    except Customer.DoesNotExist:
        raise HttpError(404,"NO Customer Found")
    Reviews.objects.create(product=product,rating=int(rating),review=review,created_by=user)
    return "SucessFully Review Added"
    
    
@api.get('get_all_user_reviews/{user_id}',response=List[ReviewGetSchema],auth=auth)
def get_all_user_reviews(request,user_id):
     return Reviews.objects.filter(created_by__id=user_id)
 
@api.put('edit_user_rating',response=ReviewGetSchema,auth=auth)
def edit_user_rating(request):
    raw_body=give_raw_data(request)
    raw_body=json.loads(raw_body)
    print(raw_body)
    user_id=raw_body['user_id']
    review_id=raw_body['review_id']
    rating=raw_body['rating']
    reviews=raw_body['review']
    try:
        user=Customer.objects.get(id=user_id)
        review=Reviews.objects.get(id=review_id)
    except Customer.DoesNotExist:
        raise HttpError(404,"User Not Found")
    except Reviews.DoesNotExist:
        raise HttpError(404,"No Review Found")
    review.updated_by=user
    review.rating=int(rating)
    review.review=reviews
    review.updated_at=datetime.now()
    review.save()
    return review
    
@api.delete("delete_user_rating/{review_id}")
def delete_user_rating(request,review_id):
    try:
        rev=Reviews.objects.get(id=review_id)
    except Reviews.DoesNotExist:
        raise HttpError(404,"No Review Found")
    rev.delete()
    return "SucessFully Deleted"
    
    
@api.get("get_product_along_reviews/{prod_id}",response=ProductGetSchema)
def get_product_along_reviews(request,prod_id):
    try:
     return Product.objects.prefetch_related('reviews').get(id=prod_id)
    except Product.DoesNotExist:
        raise HttpError(404,"Product Not Found")
    

# import openai
# from openai import OpenAI
import os

# @api.get("openAi/{message}")
# def open_ai(request,message):
# #  openai.api_key = settings.OPENAI_API_KEY
#  client = OpenAI(api_key=settings.OPENAI_API_KEY)
#  response = client.chat.completions.create(
#     model="gpt-3.5-turbo", 
#     messages=[
#         {"role": "user", "content": message}
#     ]
# )

#  print(response.choices[0].message["content"])

    
    
    


    