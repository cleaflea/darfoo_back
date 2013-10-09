# __author__ = 'zjh'

from django.shortcuts import render_to_response

def cleantha(request):
    cleantha = 'Cleantha'
    return render_to_response('darfoo_team/darfoocleantha.html', locals())
