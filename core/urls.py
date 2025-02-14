from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views  # Import views from accounts
from stories import views as stories_views  # Import views from stories
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('stories.urls')),
    path('', stories_views.story_list, name='story_list'),  # Home page showing story list
    path('story/<int:pk>/', stories_views.story_detail, name='story_detail'),  # Detailed story page
    path('create/', stories_views.create_story, name='create_story'),  # Create story page

    # Authentication-related paths
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login page
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('accounts/signup/', accounts_views.signup_view, name='signup'),  # Custom signup page

    # Include accounts.urls only if needed (usually, it would contain password reset, etc.)
    path('accounts/', include('accounts.urls')),
    path('password_change/', PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



