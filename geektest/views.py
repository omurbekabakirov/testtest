from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import ListAPIView


# @api_view(['GET', 'POST'])
# def task_list_api_view(request):
#     if request.method == 'GET':
#         task = Task.objects.all()
#         data = TaskSerializer(task, many=True).data
#         return Response(data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED,
#                             data=serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail_api_view(request, task_id):
#     try:
#         task = Task.get(id=task_id)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = TaskSerializer(task).data
#         return Response(data=data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED,
#                             data=serializer.data)
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
