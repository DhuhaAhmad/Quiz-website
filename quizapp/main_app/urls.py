from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# for the Audio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz_index, name='quiz_index'),
    path('quiz/<int:quiz_id>/', views.quiz_show, name='quiz_show'),
    path('quiz/create/', views.QuizCreate.as_view(), name='quiz_create'),
    path('quiz/<int:pk>/update/', views.QuizUpdate.as_view(), name='quiz_update'),
    path('quiz/<int:pk>/delete/', views.QuizDelete.as_view(), name='quiz_delete'),
    path('levels/question/<int:category_num>/<dif>', views.question, name='question'),
    path('questions/create/', views.QuestionsCreate.as_view(), name='questions_create'),
    path('questions/<int:pk>/update/', views.QuestionsUpdate.as_view(), name='questions_update'),
    path('questions/<int:pk>/delete/', views.QuestionsDelete.as_view(), name='questions_delete'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.Profile, name='profile'),
    path('category/', views.category, name='category'),
    path('result/', views.result, name='result'),
    path('levels/', views.levels, name='levels'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('levels/<int:id>', views.levels, name='levels'),
    path('top_five/', views.top_five, name='top_five')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

