from django.urls import path
from .views import ExerciseViewSet, WorkoutPlanViewSet

urlpatterns = [
    path('exercises', ExerciseViewSet.as_view({'get': 'list'})),
    path('exercises/<int:pk>', ExerciseViewSet.as_view({'get': 'retrieve'})),
    path('workout-plans', WorkoutPlanViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('workout-plans/<int:pk>', WorkoutPlanViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]