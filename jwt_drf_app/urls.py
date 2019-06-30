from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from jwt_drf_app import views

urlpatterns = [
    path('user/signup/', views.SignupUser.as_view(), name='signup_user'),
    path('user/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('user/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('post/create/', views.CreatePost.as_view(),
         name='create_post'),
    path('post/<int:pk>/<str:post_action>/', views.UpdatePost.as_view(),
         name='update_post')
]
