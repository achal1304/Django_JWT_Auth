from rest_framework import serializers
from .models import Robot, RobotCategory, Manufacturer

class RobotCategorySerializer(serializers.HyperLinkedModelSerialzer):
    robots = serializers.HyperLinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'robot-details'
    )

    class Meta:
        model = RobotCategory
        fields = '__all__'
    
class ManufacturerSerializer(serializers.HyperLinkedModelSerializer):
    robots = serializers.HyperLinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'manufacturer_detail'
    )
    class Meta:
        model = Manufacturer
        fields = '__all__'

class RobotSerializer(serializers.HyperLinkedModelSerialzer):
    robot_category = serializers.SlugRelatedField(
        query_set = RobotCategory.objects.all(),
        slug_field = 'name'
    )
    manufacturer = serializers.SlugRelatedField(
        query_set = Manufacturer.objects.all(),
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

