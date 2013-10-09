
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *
from django.shortcuts import render_to_response
import os

import shutil

def create_darfooplugin(request):
    form = DarfoopluginForm(request.POST or None)

    if form.is_valid():
        plugin = form.save()

        packageName = plugin.packageName
        className = plugin.className

        file_obj = request.FILES.get('darfoo_plugin', None)
        pic_obj = request.FILES.get('darfoo_pic', None)

        if file_obj == None:
            pass

        else:
            file_name = str(file_obj)
            file_full_path = str(os.path.join(os.path.dirname(__file__), '../plugins').replace('\\', '/')) + "/%s" % str(packageName)
            if os.path.exists(file_full_path):
                pass
            else:
                os.mkdir(file_full_path)
            dest = open(file_full_path + "/%s" % str(file_obj), 'wb+')
            dest.write(file_obj.read())
            dest.close()

        if pic_obj == None:
            pass
        else:
            file_name = str(pic_obj)
            file_full_path = str(os.path.join(os.path.dirname(__file__), '../plugins').replace('\\', '/')) + "/%s" % str(packageName)
            if os.path.exists(file_full_path):
                pass
            else:
                os.mkdir(file_full_path)

            des_origin_f = open(file_full_path + "/%s" % str(pic_obj), "ab")
            for chunk in pic_obj.chunks():
                des_origin_f.write(chunk)
            des_origin_f.close()



        plugin.packageUrl = "http://42.121.132.186:80/plugins/" + "%s/%s" % (str(packageName), str(file_obj))
        plugin.picUrl = "http://42.121.132.186:80/plugins/" + "%s/%s" % (str(packageName), str(pic_obj))

        plugin.save()
        form = DarfoopluginForm()

        return render_to_response("home.html", {})

    # parser = ImageFile.Parser()
    # for chunk in pic_obj.chunks():
    #     parser.feed(chunk)
    #     img = parser.close()
    #     name = file_full_path + "/%s" % str(pic_obj)
    #     img.save(name)

    # dest = open(file_full_path + "/%s" % str(pic_obj), 'wb+')
    # dest.write(file_obj.read())
    # dest.close()

    t = get_template('darfoo_depot/create_darfooplugin.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def list_darfooplugin(request):
  
    list_items = Darfooplugin.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('darfoo_depot/list_darfooplugin.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

import shutil

def delete_darfooplugin(request, id):
    try:
        snippet = Darfooplugin.objects.get(id=id)
    except Darfooplugin.DoesNotExist:
        return HttpResponse(status=404)

    packageName = snippet.packageName
    snippet.delete()

    file_full_path = str(os.path.join(os.path.dirname(__file__), '../plugins').replace('\\', '/')) + "/%s" % str(packageName)

    shutil.rmtree(file_full_path)

    return HttpResponseRedirect("/depot/darfooplugin/list")

def view_darfooplugin(request, id):
    darfooplugin_instance = Darfooplugin.objects.get(id = id)

    t=get_template('darfoo_depot/view_darfooplugin.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_darfooplugin(request, id):

    '''darfooplugin_instance = Darfooplugin.objects.get(id=id)

    form = DarfoopluginForm(request.POST or None, instance = darfooplugin_instance)

    if form.is_valid():
        form.save()

    t=get_template('darfoo_depot/edit_darfooplugin.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))'''

    darfooplugin_instance = Darfooplugin.objects.get(id=id)
    editobject_packageName = darfooplugin_instance.packageName

    # os.mkdir(file_full_path)

    '''form = DarfoopluginForm(request.POST or None, instance = darfooplugin_instance)

    if form.is_valid():
        form.save()

    t=get_template('darfoo_depot/edit_darfooplugin.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))'''
    form = DarfoopluginForm(request.POST or None, instance = darfooplugin_instance)

    if form.is_valid():
        file_full_path = str(os.path.join(os.path.dirname(__file__), '../plugins').replace('\\', '/')) + "/%s" % str(editobject_packageName)
        try:
            shutil.rmtree(file_full_path)
        except:
            pass

        plugin = form.save()

        packageName = plugin.packageName
        className = plugin.className

        file_obj = request.FILES.get('darfoo_plugin', None)
        pic_obj = request.FILES.get('darfoo_pic', None)

        if file_obj == None:
            pass

        else:
            file_name = str(file_obj)
            file_full_path = str(os.path.join(os.path.dirname(__file__), '../plugins').replace('\\', '/')) + "/%s" % str(packageName)
            if os.path.exists(file_full_path):
                pass
            else:
                os.mkdir(file_full_path)
            dest = open(file_full_path + "/%s" % str(file_obj), 'wb+')
            dest.write(file_obj.read())
            dest.close()

        if pic_obj == None:
            pass
        else:
            file_name = str(pic_obj)
            file_full_path = str(os.path.join(os.path.dirname(__file__), '../plugins').replace('\\', '/')) + "/%s" % str(packageName)
            if os.path.exists(file_full_path):
                pass
            else:
                os.mkdir(file_full_path)

            des_origin_f = open(file_full_path + "/%s" % str(pic_obj), "ab")
            for chunk in pic_obj.chunks():
                des_origin_f.write(chunk)
            des_origin_f.close()



        plugin.packageUrl = "http://42.121.132.186:80/plugins/" + "%s/%s" % (str(packageName), str(file_obj))
        plugin.picUrl = "http://42.121.132.186:80/plugins/" + "%s/%s" % (str(packageName), str(pic_obj))

        plugin.save()
        form = DarfoopluginForm()

        return render_to_response("home.html", {})

    # parser = ImageFile.Parser()
    # for chunk in pic_obj.chunks():
    #     parser.feed(chunk)
    #     img = parser.close()
    #     name = file_full_path + "/%s" % str(pic_obj)
    #     img.save(name)

    # dest = open(file_full_path + "/%s" % str(pic_obj), 'wb+')
    # dest.write(file_obj.read())
    # dest.close()

    t = get_template('darfoo_depot/create_darfooplugin.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from darfoo_depot.models import Darfooplugin
from darfoo_depot.serializers import PluginSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def plugin_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Darfooplugin.objects.all()
        serializer = PluginSerializer(snippets)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PluginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def plugin_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Darfooplugin.objects.get(id=id)
    except Darfooplugin.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PluginSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PluginSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

from darfoo_depot.serializers import customSerializer

@csrf_exempt
def custom_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Custom.objects.all()
        serializer = customSerializer(snippets)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = customSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def custom_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Custom.objects.get(id=id)
    except Custom.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = customSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = customSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@csrf_exempt
def postcustom(request):
    if request.method == 'GET':
        return HttpResponse('get cleantha')

    if request.method == 'POST':
        packageName = request.POST['packagename']
        width = request.POST['width']
        height = request.POST['height']
        leftMargin = request.POST['leftmargin']
        topMargin = request.POST['topmargin']

        custom = Custom(packageName=packageName, width=width, height=height, leftMargin=leftMargin, topMargin=topMargin)
        custom.save()

        print 'post data done'
        return HttpResponse("cleantha")

@csrf_exempt
def postsettings(request):
    if request.method == 'GET':
        return HttpResponse('new get cleantha')

    if request.method == 'POST':
        # packageName = request.POST['packagename']
        # width = request.POST['width']
        # height = request.POST['height']
        # leftMargin = request.POST['leftmargin']
        # topMargin = request.POST['topmargin']

        # custom = Custom(packageName=packageName, width=width, height=height, leftMargin=leftMargin, topMargin=topMargin)
        # custom.save()
        try:
            Settings.objects.all().delete()
        except:
            print 'delete exception'

        settings = request.POST['settings']

        settingsObject = Settings(settings=settings, flag='cleantha')
        settingsObject.save()

        print 'post data done'

        return HttpResponse("cleantha")

def getsettings(request):
    if request.method == 'GET':
        # pass
        SettingsObject = Settings.objects.get(flag='cleantha')
        return HttpResponse(SettingsObject.settings)

def home(request):
    return render_to_response('home.html', {})

def index(request):
    #return render_to_response('index.html', {})
    template = get_template('index.html')
    context = RequestContext(request, locals())
    return HttpResponse(template.render(context))

def phone(request):
    return render_to_response('phone.html', {})
