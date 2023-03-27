from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import Product, Department,Order,OrderProduct,Review,DeliveryDetail,Profile2,Profile
from .serializers import ReviewSerializer, ProductSerializer,DeliveryDetailSerializer,UserSerializer,ProfileSerializer, DepartmentSerializer,ProfileSerializer2,OrderProductSerializer,OrderSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import mixins


def index(req):
    return JsonResponse('hello', safe=False)


# @user_passes_test(lambda u: u.is_staff)
# def my_view(request):
#     # Only staff users can access this view
#     return render(request, 'my_template.html')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['emaillll'] = user.email
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer




# @permission_classes([IsAuthenticated])
class OrderSerView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request,pk=-1):
        """
        Handle GET requests to return a list of MyModel objects
        """
        if (pk > -1):
            my_model = OrderProduct.objects.get(id=pk)
            serializer = OrderProductSerializer(my_model)
        else:
            my_model = OrderProduct.objects.all()
            serializer = OrderProductSerializer(my_model, many=True)
        return Response(serializer.data)


# @permission_classes([IsAuthenticated])
class DeliveryView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request,pk=-1):
        """
        Handle GET requests to return a list of MyModel objects
        """
        if (pk > -1):
            my_model = DeliveryDetail.objects.get(id=pk)
            serializer = DeliveryDetailSerializer(my_model)
        else:
            my_model = DeliveryDetail.objects.all()
            serializer = DeliveryDetailSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = DeliveryDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = DeliveryDetail.objects.get(pk=pk)
        serializer = DeliveryDetailSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = DeliveryDetail.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @permission_classes([IsAuthenticated])
class ReviewView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request,pk=-1):
        """
        Handle GET requests to return a list of MyModel objects
        """
        if (pk > -1):
            my_model = Review.objects.get(id=pk)
            serializer = ReviewSerializer(my_model)
        else:
            my_model = Review.objects.all()
            serializer = ReviewSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Review.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# if request.user.is_authenticated:
#         serializer = DepartmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

# @permission_classes([IsAuthenticated])
class CategoryView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request,pk=-1):
        """
        Handle GET requests to return a list of MyModel objects
        """
        if (pk > -1):
            my_model = Department.objects.get(id=pk)
            serializer = DepartmentSerializer(my_model)
        else:
            my_model = Department.objects.all()
            serializer = DepartmentSerializer(my_model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if request.user.is_authenticated:
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Please register/login to continue.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Task object
        """
        if request.user.is_authenticated:
            my_model = Department.objects.get(pk=pk)
            serializer = DepartmentSerializer(my_model, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Please register/login to continue.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Task object
        """
        if request.user.is_authenticated:
            my_model = Department.objects.get(pk=pk)
            my_model.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Please register/login to continue.'}, status=status.HTTP_401_UNAUTHORIZED)



# @permission_classes([IsAuthenticated])
class ProductView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request,pk=-1):
        """
        Handle GET requests to return a list of MyModel objects
        """
        if (pk > -1):
            my_model = Product.objects.filter(id=pk) #category
            serializer = ProductSerializer(my_model, many=True)
        else:
            my_model = Product.objects.all()
            serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class OrderView(APIView):

#     def get(self, request, pk=-1):
#         if (pk > -1):
#             my_model = get_object_or_404(Order, id=pk)
#             serializer = OrderSerializer(my_model)
#         else:
#             my_model = Order.objects.all()
#             serializer = OrderSerializer(my_model, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer = serializer.create(serializer.validated_data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         my_model = get_object_or_404(Order, pk=pk)
#         serializer = OrderSerializer(my_model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk





# @permission_classes([IsAuthenticated])
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def get_object(self):
#         id = self.kwargs.get('id')
#         return get_object_or_404(Order, id=id)



# @permission_classes([IsAuthenticated])
class OrderView(APIView):

    def get(self, request, pk=-1):
        # print(request.user.__dict__) 
        if pk > -1:
            my_model = Order.objects.get(id=pk)
            serializer = OrderSerializer(my_model)
        else:
            # Filter orders by authenticated user's profile
            user = request.user
            profile = get_object_or_404(Profile, user=user)
            orders = Order.objects.filter(buyer=profile.id)
            serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
 

    # def get(self, request,pk=-1):
    #     if (pk > -1):
    #         my_model = Order.objects.get(id=pk)
    #         serializer = OrderSerializer(my_model)
    #     else:
    #         my_model = Order.objects.all()
    #         serializer = OrderSerializer(my_model, many=True)
    #     return Response(serializer.data)

    def post(self, request):

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):

        my_model = Order.objects.get(pk=pk)
        serializer = OrderSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        my_model = Order.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @permission_classes([IsAuthenticated])
class ProfileView(APIView):
    
    def get(self, request, pk=-1):
        if pk > -1:
            my_model = Profile.objects.get(id=pk)
            serializer = ProfileSerializer(my_model)
        else:
            # profile = Profile.objects.get(user=request.user)
            # serializer = ProfileSerializer(profile)
            # return Response(serializer.data)


            profile = request.user.profile
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        


            # Filter orders by authenticated user's profile
            # profile = request.user.profile
            # my_model = Profile.objects.filter(user=profile)
            # serializer = ProfileSerializer(my_model, many=True)
        return Response(serializer.data)

    # def get(self, request,pk=-1):
    #     if (pk > -1):
    #         my_model = Profile.objects.get(id=pk)
    #         serializer = ProfileSerializer(my_model)
    #     else:
    #         my_model = Profile.objects.all()
    #         serializer = ProfileSerializer(my_model, many=True)
    #     return Response(serializer.data)

    def post(self, request):

        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):

        my_model = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        my_model = Profile.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ProfileView2(APIView):

    def get(self, request,pk=-1):
        if (pk > -1):
            my_model = Profile2.objects.get(id=pk)
            serializer = ProfileSerializer2(my_model)
        else:
            my_model = Profile2.objects.all()
            serializer = ProfileSerializer2(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ProfileSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):

        my_model = Profile2.objects.get(pk=pk)
        serializer = ProfileSerializer2(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        my_model = Profile2.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



