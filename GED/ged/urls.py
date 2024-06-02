#from django.urls import path, include
#from rest_framework import routers
#from . import views

#router = routers.DefaultRouter()
#router.register(r'myapi', views.MyAPIViewSet)

#urlpatterns = [
#    path('', include(router.urls)),
#]

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'document-types', views.DocumentTypeViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
