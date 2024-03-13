from rest_framework import viewsets, status
from rest_framework.response import Response
from exercises.models import Exercise
from .models import WorkoutPlan
from .serializers import ExerciseSerializer, WorkoutPlanSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer   
    
    # GET
    def list(self, request, *args, **kwargs):
        # To update cache
        self.queryset.update()
        serializer = self.get_serializer(self.queryset.filter(user_id=request.user_id), many=True)
        return Response(serializer.data)

    # POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # GET
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({'message': 'Workout Plan not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # PUT
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({'message': 'Workout Plan not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # DELETE
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({'message': 'Workout Plan not found!'}, status=status.HTTP_404_NOT_FOUND)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)