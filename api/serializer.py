from django.conf import settings
from rest_framework import serializers

# 定义一个序列化器类 与想要序列化的模型的字段进行对应
from api.models import Student


class StudentSerializer(serializers.Serializer):
    # 想要序列化的模型的字段
    username = serializers.CharField()
    password = serializers.CharField()
    number = serializers.IntegerField()
    phone = serializers.CharField()

    gender = serializers.SerializerMethodField()

    # 自定义性别的返回值  obj是当前要序列化的对象
    def get_gender(self, obj):
        # 性别是choices类型  get_字段名_display直接访问
        return obj.get_gender_display()

    # 自定义返回图片的全路径
    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(obj.pic))


# 定义反序列化器
class StudentDeSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length=10,
        min_length=3,
        error_messages={
            "max_length": "名字长度太长了",
            "min_length": "名字长度太短了",
        }
    )
    password = serializers.CharField(
        min_length=6,
        error_messages={
            "min_length": "密码长度太短了",
        }
    )
    phone = serializers.CharField(
        max_length=11,
        min_length=11,
    )

    # 如果想要完成员工的新增 必须重写create()方法
    def create(self, validated_data):
        # 自己完成对象的创建 validated_data是前端传递的需要保存到数据库的数据
        emp_obj = Employee.objects.create(**validated_data)
        # 把创建成功的对象返回
        return emp_obj
