from .models import UserDetails
from django.contrib.auth.hashers import make_password, check_password


def authenticate_user(request):
    username = request.session.get('username')
    isValidUser = False
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        user_details = UserDetails.objects.filter(email_id=email_id).first()
        if user_details is not None:
            username = user_details.first_name
        if user_details is not None:
            isValidUser = check_password(password, user_details.password)
    else:
        if username is not None:
            isValidUser = True
    return isValidUser, username


