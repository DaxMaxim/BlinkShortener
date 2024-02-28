from django.shortcuts import render, redirect
from blink.models import Links
from django.http import HttpResponseRedirect, HttpResponse
from blink.forms import Linkform
from .algo import URL_Shortener
# Create your views here.

def generate(request):
    form = Linkform()
    if request.method == 'POST':
        original_link = request.POST.get('link')
        new_link = request.POST.get('newlink')


        try:
            ob = Links.objects.latest('accessed')
        except Links.DoesNotExist:
            ob = None


        if ob:
            id = ob.element_id + 1
        else:
            id = 1


        # check if newlink is present
        if len(new_link)>0:

            new_link = "http://localhost:8000/" + new_link

            #if newlink present, check db
            try:
                link_obj = Links.objects.get(newlink = new_link)
            except Links.DoesNotExist:
                link_obj = None

            if link_obj:
                # raise error if newlink present in db
                return HttpResponse("Link already present, Try another one")

            Links.objects.create(link = original_link, newlink = new_link, element_id = id)

        else:
            #if newlink not present, go to encoding logic

            shortener = URL_Shortener()

            # fix this, Do not check DB in this method.
            new_link = shortener.shorten_url(original_link, id)


            try:
                objec = Links.objects.filter(link = original_link)
            except Links.DoesNotExist:
                objec = None

            if objec:
                pass
            else:
                Links.objects.create(link = original_link, newlink = new_link, element_id = id)


        return HttpResponse(new_link)
    return render(request,'blink/index.html', {'form':form})

def redir(request, link_key):
    obj = Links.objects.get(newlink = "http://localhost:8000/" + link_key)

    if obj.link[:4] == 'http':
        return redirect(obj.link)
    else:
        return redirect("https://" + obj.link)
