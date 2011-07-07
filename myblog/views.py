# Create your views here.
from django.template import Context, loader
from myblog.models import blogpost
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    latest_blog_list = blogpost.objects.all().order_by('-pub_date')[:5]
    return render_to_response('myblog/index.html', {'latest_blog_list': latest_blog_list,
                                                     'user': request.user})


def detail(request, blogpost_id):
    post=blogpost.objects.filter(id=blogpost_id)[0]
    return render_to_response('myblog/details.html', {'post': post,
                                                      'user': request.user})
