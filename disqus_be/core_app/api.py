"""This module contains API resource classes"""
from tastypie.resources import ModelResource
# from django.contrib.auth.models import User
from core_app.models import Comment
from tastypie.authorization import Authorization
# from tastypie import fields
from core_app import utils
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

# class UserResource(ModelResource):
#     class Meta:
#         queryset = User.objects.all()
#         resource_name = 'user'
#         excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
#         filtering = {
#         	'username': ALL,

#         }



class CommentResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        filtering = {
            # 'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }