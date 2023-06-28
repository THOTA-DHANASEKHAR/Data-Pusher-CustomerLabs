import json
import requests
from django.http import JsonResponse
from .models import Account, Destination
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def incoming_data(request):
    print(request)
    if request.method == 'POST':
        app_secret_token = request.headers.get('CL-X-TOKEN')
        content_type1 = request.content_type
        #print(content_type1,"-----")
# ----------------

        content_type = request.headers.get('Content_Type')
        #print(content_type, "_-_-_-")
        if content_type == 'application/json':

            try:
                data = request.body
                json_data = json.loads(data)
            except ValueError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        else:
            return JsonResponse({'error': 'Unsupported content type'}, status=415)
# ---------------------------
        if app_secret_token:
            try:
                account = Account.objects.get(app_secret_token=app_secret_token)
                destinations = account.destination_set.all()
            except Account.DoesNotExist:
                print('error Invalid app secret token')
                return JsonResponse({'error': 'Invalid app secret token'}, status=401)

            try:
                for destination in destinations:
                    url = destination.url
                    http_method = destination.http_method
                    headers = destination.headers
                    print(url)
                    if http_method == 'GET':
                       result= requests.PUT(url, params=json_data, headers=headers)
                       print('--',result.content,"------------")
                    elif http_method == 'POST' or 'PUT':
                        requests.post(url, json=json_data, headers=headers)
                    else:
                        pass

                return JsonResponse({'message': 'Data sent successfully'})

            except Account.DoesNotExist:
                return JsonResponse({'error': 'Invalid app_secret_token'}, status=400)
        else:
            print("Error Invalid Formate")
    return JsonResponse({'error': 'Invalid request'}, status=400)

