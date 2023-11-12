from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from serialrizers.test import UserSerializer
from django.contrib.auth.models import User


def login(request):
    return render(request, 'users/login.html')


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def registration(request):
    serializer = UserSerializer
    user = request.user
    user_data = serializer(user).data
    print(user_data)
    return Response(user_data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_all_users(request):
    serializer = UserSerializer
    all_users = User.objects.all()
    print(User.objects.all())
    all_users = serializer(all_users, many=True).data
    return Response(all_users)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_user_by_id(request):
    id = request.GET.get('id', None)
    if not id:
        return Response(data={"error_msg": "Не указан ID пользователя"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(data={"error_msg": "Не найден ID пользователя"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer
    print(User.objects.all())
    user_data = serializer(user).data
    return Response(user_data)


@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer])
def create_user(request):
    if request.method == 'GET':
        # Обработка GET-запроса, например, отображение страницы с формой
        return render(request, 'users/create_user.html')
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # username = request.POST.get('username', None)
    # email = request.POST.get('email', None)
    # if not username or not email:
    #     return Response(data={"error_msg": "Не указаны параметры пользователя"}, status=status.HTTP_400_BAD_REQUEST)
    #
    # same_email_users = User.objects.filter(email=email).count()
    # same_username_users = User.objects.filter(username=username).count()
    #
    # if same_email_users:
    #     return Response(data={"error_msg": "Пользователь с этой почтой уже существует"},
    #                     status=status.HTTP_400_BAD_REQUEST)
    #
    # if same_username_users:
    #     return Response(data={"error_msg": "Пользователь с этим именем уже существует"},
    #                     status=status.HTTP_400_BAD_REQUEST)
    #
    # new_user = User(
    #     username=username,
    #     email=email,
    # )
    #
    # new_user.save()
    # serializer = UserSerializer
    # new_user_info = serializer(new_user).data
    # return Response(new_user_info)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_user_email(request):
    user_id = request.GET.get('id')
    user_data = User.objects.get(id=user_id)
    email = user_data.email
    data = {'email': email}
    return Response(data)

# https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer
