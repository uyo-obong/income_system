from django.utils.encoding import force_text, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core.mail import send_mail
from validate_email import validate_email
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from ..utils import token_generator
import json


import pdb
