from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test



def user_requiered(funtion=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a stnadard user,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and not u.is_company,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if funtion:
        return actual_decorator(funtion)
    return actual_decorator



def company_required(funtion=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a company,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_company,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if funtion:
        return actual_decorator(funtion)
    return actual_decorator