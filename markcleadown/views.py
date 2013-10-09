#coding=utf-8
# Create your views here.
from django.http import HttpResponse
import markdown
import os

def plan(request):
    FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'files').replace('\\','/')
    mdFilePath = str(FILE_PATH) + "/plan.md"
    STATIC_PATH = os.path.join(os.path.dirname(__file__), '../static').replace('\\', '/')
    cssFilePath = str(STATIC_PATH) + "/mdcss/GitHub2.css"


    # input = "## cleantha \n * cleantha"
    '''mdInput = open(mdFilePath)
    text = mdInput.read()
    print text
    html = markdown.markdown(text.encode('gbk'))
    print html
    return HttpResponse(html)'''

    # text = '# 大标题 ## 第二号 ... '
    '''mdInput = open(mdFilePath)
    text = mdInput.read()
    md = unicode(text, 'utf-8')
    result = markdown.markdown(md).encode('utf-8')

    return HttpResponse(result)'''

    csstext = '''<link rel="stylesheet" type="text/css" href="/site_media/mdcss/GitHub2.css"/>'''
    cssmd = unicode(csstext, 'utf-8')
    mdInput = open(mdFilePath)
    text = mdInput.read()
    md = unicode(text, 'utf-8')
    finalmd = cssmd + '\n' + md
    result = markdown.markdown(finalmd).encode('utf-8')
    print result
    return HttpResponse(result)

