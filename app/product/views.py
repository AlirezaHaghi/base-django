from django.db.models import F
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Cart, Category, Order, OrderItem, Product


class ProductModelViewSet(ModelViewSet):
    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = "__all__"

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"])
    def add_to_cart(self, request, *args, **kwargs):
        product = self.get_object()
        cart, created = Cart.objects.get_or_create(user=request.user, status=Cart.CartStatus.PENDING)

        order_item = cart.items.create(
            product=product,
            quantity=request.data.get("quantity", 1),
        )
        cart.total_price += product.price * request.data.get("quantity", 1)
        cart.save()
        return Response(CartModelViewSet.CartSerializer(cart).data)


class CartModelViewSet(ModelViewSet):
    class CartSerializer(serializers.ModelSerializer):
        class Meta:
            model = Cart
            fields = "__all__"

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CategoryModelViewSet(ModelViewSet):
    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = "__all__"

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderItemModelViewSet(ModelViewSet):
    class OrderItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = "__all__"

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderModelViewSet(ModelViewSet):
    class OrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = "__all__"

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
