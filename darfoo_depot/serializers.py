# __author__ = 'cleantha'
from django.core.urlresolvers import reverse
from rest_framework.views import View
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer
from rest_framework import serializers
from models import *

class PluginSerializer(ModelSerializer):
    class Meta:
        model = Darfooplugin
        fields = ('id', 'packageName', 'className', 'packageUrl', 'picUrl')

class customSerializer(ModelSerializer):
    class Meta:
        model = Custom
        fields = ('id', 'packageName', 'width', 'height', 'leftMargin', 'topMargin')
