import re

from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
	EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


if hasattr(settings,'ADMIN_EXEMPT_URLS'):
	ADMIN_URL = [re.compile(settings.ADMIN_EXEMPT_URLS)]

RESTRICT_URLS =[];
if hasattr(settings,'RESTRICT_EXEMPT_URLS'):
	RESTRICT_URLS += [re.compile(url) for url in settings.RESTRICT_EXEMPT_URLS]

class LoginRequiredMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		response = self.get_response(request)
		return response

	def process_view(self,request,view_func,view_args,view_kwargs):
		assert hasattr(request,'user')
		path =request.path_info.lstrip('/')
		print(path)


		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

		if request.user.is_authenticated and url_is_exempt:
			return redirect(settings.LOGIN_REDIRECT_URL)
		elif request.user.is_authenticated:
			if request.user.is_active == False:
				logout(request)
				return redirect(settings.LOGIN_URL)

		if request.user.is_authenticated:
			if request.user.role == 2 and any(url.match(path) for url in ADMIN_URL):
				return redirect(settings.LOGIN_REDIRECT_URL)
		elif not request.user.is_authenticated and any(url.match(path) for url in ADMIN_URL):
			return redirect(settings.LOGIN_REDIRECT_URL)
		


