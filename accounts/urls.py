from django.urls import path, re_path, reverse_lazy,include
from .import views
from .views import register,login
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet, UserLogIn
from django.conf.urls.static import static
from django.conf import settings



router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register', views.register, name ='register'),
    path('login', views.login, name ='login'),
    # path('logout', views.register, name ='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotpassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    # path('edit_profile/', views.edite_profile, name='edite_profile'),
    path('api/v1/', include(router.urls)),
    path('api-user-login/', UserLogIn.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

