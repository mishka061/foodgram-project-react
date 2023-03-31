from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import IngredientViewSet, RecipeViewSet, TagViewSet
from .views import UsersViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'tags', TagViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
