from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from khm_questions.views import KhmQuestionsViewSet, KhmQuestionsCrudViewSet, KhmCategoryViewSet, UserList, UserDetail
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/users/', UserList.as_view()),
    path('api/v1/users/<int:pk>/', UserDetail.as_view()),

    path('api/v1/khmlist/', KhmQuestionsViewSet.as_view({'get': 'list'})),
    path('api/v1/khmlist/<int:pk>/', KhmQuestionsViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/khm_update/<int:pk>/', KhmQuestionsCrudViewSet.as_view({'put': 'update'})),
    path('api/v1/khm_create/', KhmQuestionsCrudViewSet.as_view({'post': 'create'})),

    path('api/v1/khm_catlist/', KhmCategoryViewSet.as_view({'get': 'list'})),
    path('api/v1/khm_catcreate/', KhmCategoryViewSet.as_view({'post': 'create'})),
    path('api/v1/khm_catupdate/<int:pk>/', KhmCategoryViewSet.as_view({'put': 'update'})),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
