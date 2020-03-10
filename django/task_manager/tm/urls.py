from django.urls import path
from django.contrib import admin
# from authentication import views as auth_views
from dashboard import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path(
        'projects/',
        views.ProjectListView.as_view(),
        name='projects-list'
    ),
    path(
        'projects/<int:pk>/',
        views.ProjectDetailView.as_view(),
        name='projects-detail'
    ),
    path(
        'projects/create/',
        views.ProjectCreateView.as_view(),
        name='projects-create'
    ),
    path(
        'projects/<int:pk>/update/',
        views.ProjectUpdateView.as_view(),
        name='projects-update'
    ),
    path(
        'projects/<int:pk>/delete/',
        views.ProjectDeleteView.as_view(),
        name='projects-delete'
    ),
]
    # auth
#     path(
#         'login/',
#         auth_views.LoginView.as_view(),
#         name='login',
#     ),
#     path(
#         'logout/',
#         auth_views.LogoutView.as_view(),
#         name='logout',
#     ),
# ]
