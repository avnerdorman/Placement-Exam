from django.http import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .forms import FriendForm, ExamForm
from .models import Friend

from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt

def indexView(request):
    form = FriendForm()
    friends = Friend.objects.all()
    return render(request, "index.html", {"form": form, "friends": friends})


def postFriend(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = FriendForm(request.POST)
        # queryset = Friend.objects.all()
        updated_exam = form['exam'].value()
        # print (json.loads(updated_exam))

        if form.is_valid():
            instance = form.save()
            # serialize in n    ew friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

@csrf_exempt
def updateFriend(request):
    if request.is_ajax:
        form = FriendForm(request.POST)
        # print ("slate id is ", form['slate_id'].value())
        this_entry = Friend.objects.get(slate_id=form['slate_id'].value())
        # # print ("this entry is ", this_entry)
        updated_exam = json.loads(form['exam'].value())
        # print (updated_exam)
        Friend.objects.filter(pk=this_entry.pk).update(exam=updated_exam)
        return JsonResponse({'foo': 'bar'})
    return JsonResponse({"error": ""}, status=400)


# BONUS CBV
def checkSlateID(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the slate id from the client side.
        slate_id = request.GET.get("slate_id", None)
        # check for the slate id in the database.
        if Friend.objects.filter(slate_id = slate_id).exists():
            # if slate_id found return not valid new friend
            objectQuerySet = Friend.objects.filter(slate_id = slate_id)
            data = serializers.serialize("json", objectQuerySet)
            return HttpResponse(data, content_type="text/json-comment-filtered")

            # return JsonResponse({"valid":False}, status = 200)
        else:
            # if slate_id not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)
    



class FriendView(View):
    form_class = FriendForm
    template_name = "index.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        friends = Friend.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "friends": friends})

    def post(self, *args, **kwargs):
        # request should be ajax and method should be POST.
        if self.request.is_ajax and self.request.method == "POST":
            # get the form data
            form = self.form_class(self.request.POST)
            # save the data and after fetch the object in instance
            if form.is_valid():
                instance = form.save()
                # serialize in new friend object in json
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                # some form errors occured.
                return JsonResponse({"error": form.errors}, status=400)

        # some error occured
        return JsonResponse({"error": ""}, status=400)

