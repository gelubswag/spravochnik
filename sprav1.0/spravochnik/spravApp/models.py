from django.db import models

class Fam(models.Model):
    val = models.CharField(max_length=30, verbose_name="Фамилия", blank=True, unique=True)
    
    def __str__(self):
        return self.val
    
class Name(models.Model):
    val = models.CharField(max_length=30, verbose_name="Имя", blank=True, unique=True)

    def __str__(self):
        return self.val
    
class Otc(models.Model):
    val = models.CharField(max_length=30, verbose_name="Отчество", blank=True, unique=True)

    def __str__(self):
        return self.val
    
class Street(models.Model):
    val = models.CharField(max_length=30, verbose_name="Улица", blank=True, unique=True)

    def __str__(self):
        return self.val
    
class MainItem(models.Model):
    fam = models.ForeignKey(Fam,on_delete=models.RESTRICT,blank=True, verbose_name="Фамилия")
    name = models.ForeignKey(Name,on_delete=models.RESTRICT,blank=True, verbose_name="Имя")
    otc = models.ForeignKey(Otc,on_delete=models.RESTRICT,blank=True, verbose_name="Отчество")
    street = models.ForeignKey(Street,on_delete=models.RESTRICT,blank=True, verbose_name="Улица")
    bldn = models.CharField(max_length=5, verbose_name="Дом",null=True,blank=True)
    bldn_k = models.CharField(max_length=5, verbose_name="Корпус",null=True,blank=True)
    appr = models.IntegerField(verbose_name="Квартира",null=True,blank=True)
    tel = models.CharField(max_length=12, verbose_name="Телефон",null=True,blank=True, unique=True)
    
    def __str__(self):
        return f"{self.fam} {self.name} {self.otc}"
# Create your models here.
