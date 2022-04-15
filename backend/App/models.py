from django.db import models

# Create your models here.

class User(models.Model):
    """
    User模型类，数据类型应该继承于models.Model或其子类
    """
    id = models.IntegerField(primary_key=True)   # 主键
    username = models.TextField()                # 用户名，文本类型
    email = models.TextField()                   # 邮箱，文本类型
      
class Article(models.Model):
    """
    Article模型类，数据类型应该继承models.Model或其子类
    """
    id = models.IntegerField(primary_key=True)    # 主键
    title = models.CharField(max_length=120)      # 标题，字符串类型
    content = models.TextField()                  # 内容，文本类型
    publish_date = models.DateTimeField           # 出版时间，日期时间类型
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 设置外键
    
class Boundary(models.Model):
    """
    Boundary模型类，数据模型应该继承于models.Model或其子类
    """
    village_id  =models.IntegerField()     # 小区id
    village_name = models.TextField()      # 小区名字
    village_boundary = models.TextField()  # 小区边界坐标
    
class City(models.Model):
    year = models.IntegerField()     # 年份
    data = models.TextField()        # 日期 例如:06.12
    city = models.TextField()        # 城市
    confirm = models.IntegerField()  # 确诊数
    dead = models.IntegerField()     # 死亡数
    heal = models.IntegerField()     # 治愈数
    suspect = models.IntegerField()  # 疑似病例
    confirm_add = models.IntegerField()# 新增确诊
    
class Track(models.Model):
    id = models.IntegerField(blank=True,primary_key=True)   # id 主键
    case_num = models.IntegerField(blank=True,null=True)    # 确诊病例号
    name = models.TextField(blank=True,null=True)           # 确诊人员姓名
    village_name = models.TextField(blank=True,null=True)   # 小区名字
    relation = models.TextField(blank=True,null=True)       # 确诊关系
    confirm_date = models.TextField(blank=True,null=True)   # 确诊日期
    track = models.TextField(blank=True,null=True)          # 确诊患者轨迹
    vehicle = models.TextField(blank=True,null=True)        # 乘坐交通工具
    
class VillageStatus(models.Model):
    village_name = models.TextField()     # 小区名字
    confirmed = models.IntegerField()     # 小区确诊数
    closed_time = models.TextField()      # 小区封闭时间
    opend_time = models.TextField()      # 小区解封时间
    status = models.IntegerField()        # 小区状态标识 0:正常 1:管控 2:封闭
    
class VillageData(models.Model):
    id = models.IntegerField(primary_key=True)              # id
    village_name = models.TextField()      # 小区名字
    village_boundary = models.TextField()  # 小区边界坐标
    confirmed = models.IntegerField()      # 小区确诊数
    name = models.TextField()              # 确诊人员姓名
    closed_time = models.TextField()       # 小区解封时间
    opend_time = models.TextField()        #小区解封时间

class Community(models.Model):
    community_name = models.TextField()      # 小区名字 
    name = models.TextField()               # 患者姓名