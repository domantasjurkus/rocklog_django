from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('rocklog.urls'), name='rocklog'),
    path('madmin/', admin.site.urls),

    path('auth/', include('social_django.urls', namespace='social')),
    # path(r'^oauth/', include('social_django.urls', namespace='social')),
    # path('social-auth/', include('social_django.urls', namespace="social")),

    path('', include('rocklog_react.urls'))
]

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = ''
