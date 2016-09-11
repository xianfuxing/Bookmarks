from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse


def refresh_redirect(f):
    def wrapper(*args, **kwargs):
        if args[0].user.is_authenticated():
            return f(*args, **kwargs)
        else:
            return redirect_to_login('/account/',
                                     reverse('login'))
    return wrapper
