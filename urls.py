from django.contrib import admin
from django.urls import path
from new_app import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from new_app import CustomPasswordResetView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('login/',views.User_login,name="user_login"),
    path('reset/',views.reset,name="reset"),
    path('register/',views.register,name="register"),
    path('landing/',views.landing,name="landing"),
    path('Resetdone', views.Resetdone, name='Resetdone'),
    path('logout', views.Logout, name='logout'),
    path('update/<int:id>', views.Update, name='update'),
    path('delete/<int:id>', views.Delete, name='delete'),




    path('reset/',views.reset,name='reset'),
    path('reset/done/',auth_views.PasswordResetDoneView.as_view(),name='reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='reset_complete'),
    path('reset_confirm/',views.Resetconfirm,name="reset_confirm"),
    
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
