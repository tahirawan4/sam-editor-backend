from rest_framework import serializers
from constructor import models
from .shirt import (FrontViewShirtDetailSerializer, BackViewShirtSerializer, LeftViewShirtSerializer,
                    RightViewShirtSerializer)

from .apron import FrontViewApronDetailSerializer
from .bag import FrontViewBagDetailSerializer, BackViewBagDetailSerializer
from .base_ball_jacket import (FrontViewBaseBallJacketDetailSerializer, BackViewBaseBallJacketDetailSerializer,
                               LeftViewBaseBallJacketDetailSerializer, RightViewBaseBallJacketDetailSerializer)
from .base_ball_shirt import (FrontViewBaseBallShirtDetailSerializer, BackViewBaseBallShirtDetailSerializer,
                              LeftViewBaseBallShirtDetailSerializer, RightViewBaseBallShirtDetailSerializer)

from .bomber_jacket import (FrontViewBomberJacketDetailSerializer, BackViewBomberJacketDetailSerializer,
                            LeftViewBomberJacketDetailSerializer, RightViewBomberJacketDetailSerializer)

from .coach_jacket import (FrontViewCoachJacketDetailSerializer, BackViewCoachJacketDetailSerializer,
                           LeftViewCoachJacketDetailSerializer, RightViewCoachJacketDetailSerializer)

from .hat import (FrontViewHatDetailSerializer, BackViewHatDetailSerializer, LeftViewHatDetailSerializer,
                  RightViewHatDetailSerializer)

from .hoodie import (FrontViewHoodieDetailSerializer, BackViewHoodieDetailSerializer, RightViewHoodieDetailSerializer,
                     LeftViewHoodieDetailSerializer)

from .pant import (FrontViewPantDetailSerializer, BackViewPantDetailSerializer)
from .tank_top import (FrontViewTankTopDetailSerializer, BackViewTankTopDetailSerializer)
from .towel import (FrontViewTowelDetailSerializer, BackViewTowelDetailSerializer)
from .vest import (FrontViewVestDetailSerializer, BackViewVestDetailSerializer)


class CategoryListSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'key', 'selected']

    def get_selected(self, obj):
        return False

    # def get_designs(self, obj):
    #     qs = models.ProductDesign.objects.filter(category=obj)
    #     serializer = ProductDesignWithCategorySerializers(qs, many=True)
    #     return serializer.data


class ColorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = ['id', 'name', 'color_code']


class ComponentDetailSerializer(serializers.ModelSerializer):
    # display_image = ProductComponentListSerializer

    class Meta:
        model = models.Components
        fields = ['id', 'name']


class ProductPriceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrintingMethod
        fields = ['name', 'silk_sizes_quantity_cost', 'heat_transfer_sizes_cost', 'digital_sizes_cost']


class FabricDetailSerializer(serializers.ModelSerializer):
    colors = ColorDetailSerializer(many=True)
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.Fabric
        fields = ['id', 'name', 'selected', 'colors', 'short_description', 'cost']

    def get_selected(self, obj):
        return False


class ComponentListDetailSerializer(serializers.ModelSerializer):
    # component_selected = ComponentDetailSerializer(many=True)
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.Components
        fields = ['id', 'selected', 'name']

    def get_selected(self, obj):
        return False


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'display_image']


class ProductDesignWithCategorySerializers(serializers.ModelSerializer):
    key = serializers.SerializerMethodField()
    category_id = serializers.SerializerMethodField()
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'key', 'category_id', 'display_image', 'selected', 'base_price']

    def get_key(self, obj):
        return obj.category.key

    def get_category_id(self, obj):
        return obj.category.id

    def get_selected(self, obj):
        return False


class CategoryDetailSerializer(serializers.ModelSerializer):
    designs = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'designs']

    def get_designs(self, obj):
        qs = models.ProductDesign.objects.filter(category=obj)
        serializer = ProductDesignWithCategorySerializers(qs, many=True)
        return serializer.data


class ProductDetailSerializer(serializers.ModelSerializer):
    fabrics = FabricDetailSerializer(many=True)
    component_selected = ComponentDetailSerializer(many=True)
    front_view = serializers.SerializerMethodField()
    back_view = serializers.SerializerMethodField()
    left_view = serializers.SerializerMethodField()
    right_view = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    # back_view = serializers.SerializerMethodField()

    # front_view = BodyDetailSerializer()
    # left_view = LeftViewSerializer()
    # right_view = RightViewSerializer()
    # back_view = BackViewSerializer()

    class Meta:
        model = models.ProductDesign
        # fields = ['id', 'name', 'fabrics', 'front_view', 'left_view', 'right_view', 'back_view']
        fields = ['id', 'name', 'category', 'fabrics', 'component_selected', 'front_view', 'back_view', 'left_view',
                  'right_view',
                  'base_price']

    def get_category(self, obj):
        return obj.category.key

    def get_front_view(self, obj):
        if obj.category.key == 'polo-shirt':
            serializer = FrontViewShirtDetailSerializer(obj.front_view)
            return serializer.data
        if obj.category.key == 'shirt':
            serializer = FrontViewShirtDetailSerializer(obj.front_view)
            return serializer.data
        if obj.category.key == 'apron':
            serializer = FrontViewApronDetailSerializer(obj.front_view_apron)
            return serializer.data
        if obj.category.key == 'bag':
            serializer = FrontViewBagDetailSerializer(obj.front_view_bag)
            return serializer.data
        if obj.category.key == 'base-ball-jacket':
            serializer = FrontViewBaseBallJacketDetailSerializer(obj.front_view_base_b_jacket)
            return serializer.data
        if obj.category.key == 'base-ball-shirt':
            serializer = FrontViewBaseBallShirtDetailSerializer(obj.front_view_base_b_shirt)
            return serializer.data
        if obj.category.key == 'bomber-jacket':
            serializer = FrontViewBomberJacketDetailSerializer(obj.front_view_bomber_jac)
            return serializer.data
        if obj.category.key == 'hat':
            serializer = FrontViewHatDetailSerializer(obj.front_view_hat)
            return serializer.data
        if obj.category.key == 'hoodie':
            serializer = FrontViewHoodieDetailSerializer(obj.front_view_hoodie)
            return serializer.data
        if obj.category.key == 'coach-jacket':
            serializer = FrontViewCoachJacketDetailSerializer(obj.front_view_coach_jac)
            return serializer.data
        if obj.category.key == 'pants':
            serializer = FrontViewPantDetailSerializer(obj.front_view_pant)
            return serializer.data
        if obj.category.key == 'tank-top':
            serializer = FrontViewTankTopDetailSerializer(obj.front_view_tank_top)
            return serializer.data
        if obj.category.key == 'towel':
            serializer = FrontViewTowelDetailSerializer(obj.front_view_towel)
            return serializer.data
        if obj.category.key == 'vest':
            serializer = FrontViewVestDetailSerializer(obj.front_view_vest)
            return serializer.data

        return None

        #

        #

        #

        #

        #
        # if product_design.category.key == 'coach-jacket':
        #     serializer = product_serializer.CoachJacDetailSerializer(product_design)
        #     return Response(serializer.data)
        #

        #

        #

        #

    def get_back_view(self, obj):
        if obj.category.key == 'polo-shirt':
            serializer = BackViewShirtSerializer(obj.back_view)
            return serializer.data
        if obj.category.key == 'shirt':
            serializer = BackViewShirtSerializer(obj.back_view)
            return serializer.data
        if obj.category.key == 'bag':
            serializer = BackViewBagDetailSerializer(obj.back_view_bag)
            return serializer.data
        if obj.category.key == 'base-ball-jacket':
            serializer = BackViewBaseBallJacketDetailSerializer(obj.back_view_base_b_jacket)
            return serializer.data
        if obj.category.key == 'base-ball-shirt':
            serializer = BackViewBaseBallShirtDetailSerializer(obj.back_view_base_b_shirt)
            return serializer.data
        if obj.category.key == 'bomber-jacket':
            serializer = BackViewBomberJacketDetailSerializer(obj.back_view_base_bomber_jac)
            return serializer.data
        if obj.category.key == 'hat':
            serializer = BackViewHatDetailSerializer(obj.back_view_hat)
            return serializer.data
        if obj.category.key == 'hoodie':
            serializer = BackViewHoodieDetailSerializer(obj.back_view_hoodie)
            return serializer.data
        if obj.category.key == 'pants':
            serializer = BackViewPantDetailSerializer(obj.back_view_pant)
            return serializer.data
        if obj.category.key == 'tank-top':
            serializer = BackViewTankTopDetailSerializer(obj.back_view_tank_top)
            return serializer.data
        if obj.category.key == 'towel':
            serializer = BackViewTowelDetailSerializer(obj.back_view_towel)
            return serializer.data
        if obj.category.key == 'vest':
            serializer = BackViewVestDetailSerializer(obj.back_view_vest)
            return serializer.data
        if obj.category.key == 'coach-jacket':
            serializer = BackViewCoachJacketDetailSerializer(obj.back_view_base_coach_jac)
            return serializer.data

        return None

    def get_left_view(self, obj):
        if obj.category.key == 'polo-shirt':
            serializer = LeftViewShirtSerializer(obj.left_view)
            return serializer.data
        if obj.category.key == 'shirt':
            serializer = LeftViewShirtSerializer(obj.left_view)
            return serializer.data
        if obj.category.key == 'base-ball-jacket':
            serializer = LeftViewBaseBallJacketDetailSerializer(obj.left_view_base_b_jacket)
            return serializer.data
        if obj.category.key == 'base-ball-shirt':
            serializer = LeftViewBaseBallShirtDetailSerializer(obj.left_view_base_b_shirt)
            return serializer.data
        if obj.category.key == 'bomber-jacket':
            serializer = LeftViewBomberJacketDetailSerializer(obj.left_view_bomber_jac)
            return serializer.data
        if obj.category.key == 'hat':
            serializer = LeftViewHatDetailSerializer(obj.left_view_hat)
            return serializer.data
        if obj.category.key == 'hoodie':
            serializer = LeftViewHoodieDetailSerializer(obj.left_view_hoodie)
            return serializer.data
        if obj.category.key == 'coach-jacket':
            serializer = LeftViewCoachJacketDetailSerializer(obj.left_view_coach_jac)
            return serializer.data

        return None

    def get_right_view(self, obj):
        if obj.category.key == 'polo-shirt':
            serializer = RightViewShirtSerializer(obj.right_view)
            return serializer.data
        if obj.category.key == 'shirt':
            serializer = RightViewShirtSerializer(obj.right_view)
            return serializer.data
        if obj.category.key == 'base-ball-jacket':
            serializer = RightViewBaseBallJacketDetailSerializer(obj.right_view_base_b_jacket)
            return serializer.data
        if obj.category.key == 'base-ball-shirt':
            serializer = RightViewBaseBallShirtDetailSerializer(obj.right_view_base_b_shirt)
            return serializer.data
        if obj.category.key == 'bomber-jacket':
            serializer = RightViewBomberJacketDetailSerializer(obj.right_view_bomber_jac)
            return serializer.data
        if obj.category.key == 'hat':
            serializer = RightViewHatDetailSerializer(obj.right_view_hat)
            return serializer.data
        if obj.category.key == 'hoodie':
            serializer = RightViewHoodieDetailSerializer(obj.right_view_hoodie)
            return serializer.data
        if obj.category.key == 'coach-jacket':
            serializer = RightViewCoachJacketDetailSerializer(obj.right_view_coach_jac)
            return serializer.data

        return None
