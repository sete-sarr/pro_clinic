from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'comptes'

urlpatterns = [
    path('admin/', views.PannelAdminView.as_view(), name='admin_dashboard'),

    # 🔐 AUTH
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='registration/deconnexion.html'), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'
    ), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('rapport/', views.dashboard_rapport, name='rapport'),

    path('rapport/data/', views.dashboard_data, name="dashboard_data"),
    # 🏠 DASHBOARD (TOUJOURS EN DERNIER)
    path('', views.dashboard, name='dashboard'),
]

# from django.urls import path, include
# from . import views

# app_name = 'comptes'

# urlpatterns = [

#     # 🔐 Django auth (utilise registration/)
#     path('', include('django.contrib.auth.urls')),

#     # 🏠 Dashboard
#     path('', views.dashboard, name='dashboard'),
# ]
