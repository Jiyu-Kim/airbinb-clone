from django.db import models

# Create your models here.
class CommonModel(models.Model):

    # Common Model Definition
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    # 이 클래스는 Django에서 model을 configure할 때 사용된다.
    # 우리가 이 model을 abstract로 설정하면 Django는 이 model을 봐도 데이터베이스에 저장하지 않는다.
    class Meta:
        abstract = True