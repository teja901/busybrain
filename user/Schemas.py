


from typing import List, Optional
from ninja import ModelSchema, Schema
from .models import *

class UserGetSchema(ModelSchema):
    class Config:
        model = Customer
        model_fields = ['name']
    
    

    

class ReviewGetSchema(ModelSchema):
    created_by: Optional[UserGetSchema] = None
    updated_by : Optional[UserGetSchema] = None
    rating: int
    class Config:
        model = Reviews
        model_fields = "__all__"
        
        
class ProductGetSchema(ModelSchema):
    reviews:Optional[List[ReviewGetSchema]] = None
    class Config:
        model = Product
        model_fields = "__all__"
        
    
        


