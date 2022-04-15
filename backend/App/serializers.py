from attr import fields
from .models import Boundary, City, Track, VillageStatus


class BoundarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Boundary  # 指定的模型类
        fields = '__all__'  # 需要序列化的属性
        
class City(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        
class Track(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
        
class VillageStatus(serializers.ModelSerializer):
    class Meta:
        model = VillageStatus
        fields = '__all__'
