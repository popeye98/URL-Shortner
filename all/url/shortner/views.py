
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.views import View

from .models import URL




def kirr_redirect_view(request,sc):
    print(sc)
    #obj = URL.objects.filter(shortcode=sc).first()
    obj = get_object_or_404(URL, shortcode=sc)
    

    return redirect(obj.url)

  


class KirrCBView(View):
    def get(self, request,sc):
        obj = get_object_or_404(URL, shortcode=sc)
        return redirect(obj.url)


    def post(self, request, *args, **kwargs):
        return HttpResponse()