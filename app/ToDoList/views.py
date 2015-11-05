from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import redirect

from ToDoList.models import List
from ToDoList.models import Item
from ToDoList.models import ListAddForm
from ToDoList.models import ItemAddForm
from ToDoList.models import ItemEditForm
from ToDoList.models import LogInForm

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from COMP204P import config

import hmac
import hashlib
import json
import os
import subprocess

# Create your views here.
 
def login_view(request):
	if request.user.is_authenticated():
		return redirect('ToDoList.views.index')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					# Redirect to a success page.
					return redirect('ToDoList.views.index')
				else:
					# Return a 'disabled account' error message
					return redirect('ToDoList.views.login_view')
			else:
				# Return an 'invalid login' error message.
				return redirect('ToDoList.views.login_view')
		else:
			form = AuthenticationForm()
			return render(request, 'ToDoList/login.html', { 'form': form })

def signup_view(request):
	if request.user.is_authenticated():
		return redirect('ToDoList.views.index')
	else:
		if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
    			form.save()
    			'''
                try:
    				user = User.objects.create_user(username, '', password)
    				user.save()
    			except:
    				return redirect('ToDoList.views.signupfail_view')
                '''
    			return redirect('ToDoList.views.login_view')
		form = UserCreationForm()
		return render(request, 'ToDoList/signup.html', {
			'form': form,
		})

def signupfail_view(request):
	return render(request, 'ToDoList/signup_fail.html')

def logout_view(request):
	logout(request)
	return redirect('ToDoList.views.login_view')

def validateSignature(request):
	x_hub_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
	if x_hub_signature:
		sha_name, signature = x_hub_signature.split('=')
		mac = hmac.new(config.GITHUB_WEBHOOK_KEY, msg=request.body, digestmod=hashlib.sha1)
		return mac.hexdigest() == signature
	else:
		return False

@csrf_exempt
def github(request):
	if request.method == 'POST':
		if validateSignature(request):
			body = json.loads(request.body)
			if body.get("ref", None) and request.META.get('HTTP_X_GITHUB_EVENT', None):
				if body.get("ref") == config.GITHUB_AUTOPULL_BRANCH and request.META.get("HTTP_X_GITHUB_EVENT") == "push":
					subprocess.Popen('at now -f /home/localuser/comp204p/bin/restartAndPull.bash', shell=True)
					return HttpResponse("restarting server")
				else:
					return HttpResponse("not pulling because %s != %s" % (body.get('ref'), config.GITHUB_AUTOPULL_BRANCH) )
			else:
				return HttpResponse("headers and body not even initialized")
		else:
			return HttpResponse("authentication failed")
	else:
		return HttpResponse("wrong HTTP method")

@login_required
def index(request):
	lists = List.objects.filter(user=request.user)
	return render(request, 'ToDoList/index.html', {
		'lists': lists,
	})

@login_required
def list_detail(request, id):
	list = List.objects.get(id=id)
	if list.user==request.user:
		try:
			items = Item.objects.filter(list=id)
		except Item.DoesNotExist:
			raise Http404('This item does not exist')
		return render(request, 'ToDoList/list_detail.html', {
			'items': items,
			'list': list,
		})
	else:
		return redirect('ToDoList.views.index')

@login_required
def item_form(request, id):
	try:
		u = Item.objects.get(id=id).list.user
	except:
		u = ''
	if id == '0' or u==request.user:
		if request.method == 'POST':
			if id == '0':
				form = ItemAddForm(request.POST)
			else:
				inst = Item.objects.get(id=id)
				form = ItemEditForm(request.POST, instance=inst)
			if form.is_valid():
				form.save()
				return redirect('ToDoList.views.index')
		else:
			if id == '0':
				form = ItemAddForm()
				form.fields['list'].queryset = List.objects.filter(user=request.user)
			else:
				form = ItemEditForm()
		return render(request, 'ToDoList/item_form.html', {
			'form': form,
			'id': id,
		})
	else:
		return redirect('ToDoList.views.index')

@login_required
def delete_item(request, id):
	try:
		item = Item.objects.get(id=id).list
	except:
		return redirect('ToDoList.views.index')
	if item.user == request.user:
		try:
			Item.objects.filter(id=id).delete()
			return redirect('ToDoList.views.index')
		except Item.DoesNotExist:
			raise Http404('This item does not exist')
	else:
		return redirect('ToDoList.views.index')
		
@login_required
def list_form(request, id):
	try:
		u = List.objects.get(id=id).user
	except:
		u = ''
	if id == '0' or u==request.user:
		if request.method == 'POST':
			if id == '0':
				form = ListAddForm(request.POST)
			else:
				inst = List.objects.get(id=id)
				form = ListAddForm(request.POST, instance=inst)
			if form.is_valid():
				if id == '0':
					form = form.save(commit=False)
					form.user = request.user
				form.save()
				return redirect('ToDoList.views.index')
		else:
			form = ListAddForm()
		return render(request, 'ToDoList/list_form.html', {
			'form': form,
			'id': id,
		})
	else:
		return redirect('ToDoList.views.index')

@login_required
def delete_list(request, id):
	try:
		list = List.objects.get(id=id)
	except:
		return redirect('ToDoList.views.index')
	if list.user == request.user:
		try:
			list.delete()
			return redirect('ToDoList.views.index')
		except List.DoesNotExist:
			raise Http404('This item does not exist')
	else:
		return redirect('ToDoList.views.index')