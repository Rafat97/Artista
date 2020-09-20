
from register.models import User

def get_current_user(request):
    if request.session.has_key('user'):
        uid = request.session['user'] 
        user =  User.objects.filter(uuid__exact=uid).get()
        return user
    else:
        return None