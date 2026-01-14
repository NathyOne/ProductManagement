from django.urls import path
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('products',views.ProductViewSet)
router.register('category',views.CategoryViewSet)
router.register('store',views.StoreViewSet)





urlpatterns = router.urls 
