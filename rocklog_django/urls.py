"""rocklog_django URL Configuration
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # rocklog
    path('', include('rocklog.urls'), name='rocklog'),
    # path('', include('social_django.urls', namespace='social')),
    path('madmin/', admin.site.urls),

    # simpleisbetter (works, but authentication process is cancelled)
    # path(r'^oauth/', include('social_django.urls', namespace='social')),

    # some other tutorial (works as above)
    # path('social-auth/', include('social_django.urls', namespace="social")),

    # official social docs (works)
    path('auth/', include('social_django.urls', namespace='social')),
    # path('logout/', LogoutView.as_view(), name='logout'),
]

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = ''
