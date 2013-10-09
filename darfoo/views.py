#This Python file uses the following encoding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt
import hashlib
import xml.etree.ElementTree as ET
import os

def check(request):
    token = 'cleantha'
    signature = request.GET.get('signature', '')
    timestamp = request.GET.get('timestamp', '')
    nonce = request.GET.get('nonce', '')
    echostr = request.GET.get('echostr', '')

    infostr = ''.join(sorted([token, timestamp, nonce]))
    if infostr:
        hashstr = hashlib.sha1(infostr).hexdigest()
        if hashstr is signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('haststr is not signature')
    else:
        return HttpResponse('infostr does not existing')


def checkSignature(request):
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    token = 'cleantha'

    tmplist = [token, timestamp,nonce]
    tmplist.sort()
    tmpstr = "%s%s%s"%tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return echostr
    else:
        return None

@csrf_exempt
def weichatindex(request):
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request))
        return response
    elif request.method == 'POST':
	postMenu()
        response = HttpResponse(responseMsg(request), content_type="application/xml")
        # response = HttpResponse(originMsg(request), content_type="application/xml")
        return response
    else:
        return HttpResponse('Hello World')

def originMsg(request):
    post_data = request.body
    msg = paraseMsgXml(post_data)
    return replyXml(msg, post_data)

def paraseMsgXml(raw_msg):
    root = ET.fromstring(raw_msg)
    msg = {}
    if root.tag == 'xml':
        for child in root:
            msg[child.tag] = (child.text)
    return msg

import urllib  
import urllib2  
   
def post(url, data):  
    req = urllib2.Request(url)  
    data = urllib.urlencode(data)  
    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  
    menuResponse = response.read() 
    LOG_PATH = os.path.join(os.path.dirname(__file__), '../logs').replace('\\', '/')
    filePath = str(LOG_PATH) + '/weixinmenulog.txt'
    logFile = open(filePath, 'a')
    logFile.write(str(menuResponse))
    logFile.close()

import json

def postAgain(url, data):
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    #req.add_header('charset', 'GBK')    

    response = urllib2.urlopen(req, json.dumps(data, ensure_ascii=False))
    res = response.read()

    LOG_PATH = os.path.join(os.path.dirname(__file__), '../logs').replace('\\', '/')
    filePath = str(LOG_PATH) + '/weixinmenuclealog.txt'
    logFile = open(filePath, 'a')
    logFile.write(str(res))
    logFile.close()

def getAccessToken(url):
    token =  urllib2.urlopen(url).read()
  
    LOG_PATH = os.path.join(os.path.dirname(__file__), '../logs').replace('\\', '/')
    filePath = str(LOG_PATH) + '/weixintokenlog.txt'
    logFile = open(filePath, 'a')
    logFile.write(str(token))
    logFile.close()
    
    tokendict = json.loads(token)
    
    LOG_PATH = os.path.join(os.path.dirname(__file__), '../logs').replace('\\', '/')
    filePath = str(LOG_PATH) + '/weixintokenlog.txt'
    logFile = open(filePath, 'a')
    logFile.write(str(tokendict['access_token']))
    logFile.close()

    return tokendict['access_token']

def postMenu(): 
    appid = "wxd54c44f0904016a0"
    appsecret = "e9e9d977ca64d4a51ffd76ad286058e3"
    geturl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
    accessUrl = geturl % (appid, appsecret)
    accessToken = str(getAccessToken(accessUrl))
    posturl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s"
    menuUrl = posturl % accessToken
    data = {
     "button":[
     {  
          "type":"click",
          "name":"今日",
          "key":"V1001_TODAY_MUSIC"
      },
      {
           "type":"view",
           "name":"明日",
           "url":"http://www.qq.com/"
      }]
    }
 
   # print post(posturl, data)  
    postAgain(menuUrl, data)    

import time
#for reply when user focus on the weixinback
def autoReplyXml(msg, content):	
    textTpl = """<xml>
         <ToUserName><![CDATA[%s]]></ToUserName>
         <FromUserName><![CDATA[%s]]></FromUserName>
         <CreateTime>%s</CreateTime>
         <MsgType><![CDATA[text]]></MsgType>
         <Content><![CDATA[%s]]></Content>
         <FuncFlag>0</FuncFlag>
         </xml>"""

    echostr = textTpl % (
        msg['FromUserName'], msg['ToUserName'], str(int(time.time())),
        content)
    return echostr

def replyXml(recvmsg, replyContent):
    textTpl = """ <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
                </xml>
                """
    echostr = textTpl % (recvmsg['FromUserName'], recvmsg['ToUserName'], recvmsg['CreateTime'], recvmsg['MsgType'], replyContent)
    return echostr

def responseMsg(request):
    # post_data = smart_str(request.raw_post_data)
    post_data = request.body
    msg = paraseMsgXml(post_data)
    if msg["MsgType"] == "event":
	helloContent = "欢迎来到大幅 你可以通过此公共平台和你的父母进行通信~"
        return autoReplyXml(msg, helloContent)
    
    content = process(msg['Content'])
    return replyXml(msg, content)

def process(msg):
    if msg == 'hellodarfoo':
        return "welcome to darfoo"
