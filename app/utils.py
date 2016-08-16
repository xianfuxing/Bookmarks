from django.contrib.auth.models import User
from account.models import Profile


def create_profile(strategy, details, response, user, *args, **kwargs):

    if Profile.objects.filter(user=user).exists():
        pass
    else:
        new_profile = Profile.objects.create(user=user)
        new_profile.save()

    return kwargs