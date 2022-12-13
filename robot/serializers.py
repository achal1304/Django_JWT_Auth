from rest_framework import serializers
from .models import Robot, RobotCategory, Manufacturer

class RobotCategorySerializer(serializers.HyperlinkedModelSerializer):
    robot = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'robot-detail'
    )

    class Meta:
        model = RobotCategory
        fields = '__all__'
    
class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    robot = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'robot-detail'
    )
    class Meta:
        model = Manufacturer
        fields = '__all__'

class RobotSerializer(serializers.HyperlinkedModelSerializer):
    robot_category = serializers.SlugRelatedField(
        queryset = RobotCategory.objects.all(),
        slug_field = 'name'
    )
    manufacturer = serializers.SlugRelatedField(
        queryset = Manufacturer.objects.all(),
        slug_field = 'name'
    )
    currency = serializers.ChoiceField(
        choices = Robot.CURRENCY_CHOICES
    )
    currency_name = serializers.CharField(
        source = 'get_currency_display',
        read_only = True
    )

    class Meta:
        model = Robot
        fields = '__all__'

