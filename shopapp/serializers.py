from rest_framework import serializers
from .models import Product , Department, DeliveryDetail, Order,OrderProduct,Review,Profile2,Profile
from django.contrib.auth.models import User



class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department 
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    p_type = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Product 

        fields = ['p_name','id', 'p_desc', 'p_price', 'p_type', 'p_amount', 'p_image']

    def create(self, validated_data):
        product = Product.objects.create(**validated_data) 
        return product
#add to the views try and except


class ProfileSerializer2(serializers.ModelSerializer):

    items222 = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all(), required=False)
    
    class Meta:
        fields = ['id','username','password','email','first_name','last_name','is_staff','items222']
        model = Profile2 


class ProfileSerializer(serializers.ModelSerializer):

    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all(), required=False)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        fields = '__all__'
        model = Profile 



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        items_data = profile_data.pop('items', [])
        profile = Profile.objects.create(user=user, **profile_data)
        for item_data in items_data:
            profile.items.add(item_data)
        return user

class DeliveryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryDetail
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source='product', queryset=Product.objects.all())
    order_id = serializers.PrimaryKeyRelatedField(source='order', queryset=Order.objects.all(), many=False)


    class Meta:
        model = OrderProduct
        fields = ['product_id', 'order_id']



# class OrderSerializer(serializers.ModelSerializer):
#     buyer_id = serializers.PrimaryKeyRelatedField(source='buyer', queryset=Profile.objects.all())
#     delivery_details_id = serializers.PrimaryKeyRelatedField(source='delivery_details', queryset=DeliveryDetail.objects.all())
#     product_ids = serializers.PrimaryKeyRelatedField(source='products', queryset=Product.objects.all(), many=True)

#     class Meta:
#         model = Order
#         fields = ['buyer_id','id', 'delivery_details_id', 'product_ids', 'total_price', 'total_product_amount']
    
#     def create(self, validated_data):
#         products = validated_data.pop('products')
#         order = Order.objects.create(**validated_data)
#         for product in products:
#             OrderProduct.objects.create(order=order, product=product)
#         return order

class OrderSerializer(serializers.ModelSerializer):
    buyer = ProfileSerializer(read_only=True)
    delivery_details = DeliveryDetailSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['buyer', 'id', 'delivery_details', 'products', 'total_price', 'total_product_amount']

    def create(self, validated_data):
        delivery_details_data = validated_data.pop('delivery_details')
        products_data = validated_data.pop('products')
        
        delivery_details = DeliveryDetail.objects.create(**delivery_details_data)
        products = [Product.objects.get(pk=product_data['id']) for product_data in products_data]
        
        order = Order.objects.create(delivery_details=delivery_details, **validated_data)
        order.products.set(products)
        return order


    def update(self, instance, validated_data):
        delivery_details_data = validated_data.pop('delivery_details', None)
        products_data = validated_data.pop('products', None)
        
        if delivery_details_data:
            delivery_details_serializer = DeliveryDetailSerializer(instance.delivery_details, data=delivery_details_data)
            if delivery_details_serializer.is_valid():
                delivery_details = delivery_details_serializer.save()
                validated_data['delivery_details'] = delivery_details
            else:
                raise serializers.ValidationError(delivery_details_serializer.errors)

        if products_data:
            products = [Product.objects.get(pk=product_data['id']) for product_data in products_data]
            instance.products.set(products)

        return super().update(instance, validated_data)


#  {
#   "buyer_id": 1,
#   "delivery_details": {
#     "field1": "value1",
#     "field2": "value2",
    
#   },
#   "product_ids": [1, 2, 3],
#   "total_price": 100.00,
#   "total_product_amount": 3
# }





class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'



