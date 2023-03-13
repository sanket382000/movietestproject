
from django.urls import path,include
from .views import movie_list,MovieViewset,movie_data,movie_detail,student_list,Addstudent
from rest_framework import routers
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Movie API database",
        default_version='v1',
        description='My first Test Documentation',
        contact=openapi.Contact(email='contact@swaggeringblog.local'),
        license=openapi.License(name='Django License')

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

routers = routers.DefaultRouter()
routers.register(r'movie-api',MovieViewset)

urlpatterns = [
    # path('movie',movie_list,name='movie'),
    # path('',include(routers.urls)),
    # path('auth-token',views.obtain_auth_token,name='auth-token'),
    path('movies',movie_data,name='movies'),
    path('movie-detail/<int:pk>',movie_detail),
    path('movie-details/<int:pk>',movie_detail),
    path('swagger',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('student-list',student_list),
    path('addstudent', Addstudent)

]
