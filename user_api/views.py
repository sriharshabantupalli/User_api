from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

def validate_access_token(access_token):
    return True

def generate_access_token(request):
    expiration_time = datetime.now() + timedelta(minutes=3)
    access_token = "your_generated_access_token"
    response_data = {
        "access_token": access_token,
        "expires_in": expiration_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return JsonResponse(response_data)

@csrf_exempt
def insert_user_details(request):
    access_token = request.META.get('HTTP_ACCESS_TOKEN')
    if not access_token:
        return JsonResponse({"error": "Access token missing"}, status=401)

    if not validate_access_token(access_token):
        return JsonResponse({"error": "Invalid access token"}, status=401)

    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    email_id = request.POST.get('email_id')
    phone_number = request.POST.get('phone_number')
    address = request.POST.get('address')
    created_date = datetime.now()

    user = User(f_name=f_name, l_name=l_name, email_id=email_id,
                phone_number=phone_number, address=address,
                created_date=created_date)
    user.save()

    return JsonResponse({"success": True})

def list_users(request):
    access_token = request.META.get('HTTP_ACCESS_TOKEN')
    if not access_token:
        return JsonResponse({"error": "Access token missing"}, status=401)

    if not validate_access_token(access_token):
        return JsonResponse({"error": "Invalid access token"}, status=401)

    page = int(request.GET.get('page', 1))
    limit = 5
    sort_by = request.GET.get('sort_by', 'created_date')

    users = User.objects.order_by(sort_by).all()[(page-1)*limit:page*limit]

    response_data = {
        "users": [
            {
                "f_name": user.f_name,
                "l_name": user.l_name,
                "email_id": user.email_id,
                "phone_number": user.phone_number,
                "address": user.address,
                "created_date": user.created_date.strftime("%Y-%m-%d %H:%M:%S")
            }
            for user in users
        ],
        "next_url": f"/users/?page={page+1}",
        "prev_url": f"/users/?page={page-1}" if page > 1 else None
    }

    return JsonResponse(response_data)
