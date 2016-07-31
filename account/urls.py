from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import dashboard, register, edit

urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^$', dashboard, name='dashboard'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'registration/b_logged_out.html'},
        name='logout'),

    url(r'^logout-then-login/$',
        auth_views.logout_then_login,
        name='logout_then_login'),

    url(r'^password-change/$',
        auth_views.password_change,
        {'template_name': 'registration/b_password_change_form.html'},
        name='password_change'),

    url(r'^password-change/done/$',
        auth_views.password_change_done,
        {'template_name': 'registration/b_password_change_done.html'},
        name='password_change_done'),

    url(r'^password-reset/$',
        auth_views.password_reset,
        {'template_name': 'registration/b_password_reset.html'},
        name='password_reset'),

    url(r'^password-reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'registration/b_password_reset_done.html'},
        name='password_reset_done'),

    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.password_reset_confirm,
        {'template_name': 'registration/b_password_reset_confirm.html'},
        name='password_reset_confirm'),

    url(r'^password-reset/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'registration/b_password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^register/$', register, name='register'),
    url(r'^edit/$', edit, name='edit'),
]
