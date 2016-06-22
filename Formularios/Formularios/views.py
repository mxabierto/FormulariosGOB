import requests
import json
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404


def informa(request):
	return render(request, 'informa.html', {'organization': request.GET.get('organization', '')})


def reportar(request):
	return render(request, 'reportar.html', {'media_url': request.GET.get('media_url', '')})


@csrf_exempt
def send(request):
	if request.method != 'POST':
		raise Http404

	response_mail = requests.post(
        "https://api.mailgun.net/v3/participa.gob.mx/messages",
        auth=("api", str(settings.MAIL_GUN_API_KEY)),
        data={"from": "Reporte DGM <reporte@participa.gob.mx>",
              "to": ["{0}".format(settings.TO_MAIL_GUN)],
              "subject": "{0}".format(request.POST.get('subject')),
              "html": "{0}".format(request.POST.get('html').encode('utf-8'))})

	if 'Queued. Thank you' in response_mail.text:
		return JsonResponse({'message': 'ok'})
	else:
		return JsonResponse({'message': 'error', 'error': response_mail.text, 'to': request.POST.get('to')})