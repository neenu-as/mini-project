from django.db import models

# Create your models here.
class login_table(models.Model):
    Username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    type=models.CharField(max_length=100)
class officer(models.Model):
    LOGINID = models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    phon=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo=models.FileField()
class shops(models.Model):
    LOGINID = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    phon=models.BigIntegerField()
    email = models.CharField(max_length=100)
    photo = models.FileField()
class user(models.Model):
    LOGINID = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    phon=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo=models.FileField()
class complaint(models.Model):
    USER= models.ForeignKey(user,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.DateField()
class farmer(models.Model):
    LOGINID = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    DOB = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    phon = models.BigIntegerField()
    email = models.CharField(max_length=100)
    photo = models.FileField()
class doubts(models.Model):
    FARMER = models.ForeignKey(farmer,on_delete=models.CASCADE)
    OFFICER = models.ForeignKey(officer,on_delete=models.CASCADE)
    doubt = models.CharField(max_length=100)
    date =models.DateField()
    reply = models.CharField(max_length=100)
class product(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    price =models.CharField(max_length=100)
    quantity =models.CharField(max_length=100)
    image = models.FileField()
    FARMER = models.ForeignKey(farmer,on_delete=models.CASCADE)

class schemes(models.Model):
    name = models.CharField(max_length=100)
    documents =models.FileField()
    fdate = models.DateField()
    tdate = models.DateField()
    details = models.CharField(max_length=100)



# class request_schemes(models.Model):
#     SCHEMES = models.ForeignKey(schemes,on_delete=models.CASCADE)
#     FARMER = models.ForeignKey(farmer,on_delete=models.CASCADE)
#     documents = models.FileField()
#     date = models.DateField()
#     status = models.CharField(max_length=100)

class fertilizer(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    SHOPS = models.ForeignKey(shops,on_delete=models.CASCADE)


class rating(models.Model):
    PRODUCT = models.ForeignKey(product,on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    rating=models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    review =models.CharField(max_length=100)
class subsidy(models.Model):
    FERTILIZER = models.ForeignKey(fertilizer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
class order (models.Model):
    USER = models.ForeignKey(user,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100)
    price=models.IntegerField()
class order_details (models.Model):
    PRODUCT = models.ForeignKey(product,on_delete=models.CASCADE)
    ORDER = models.ForeignKey(order,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    date = models.DateField()




class subsidy_product(models.Model):
    sproduct=models.CharField(max_length=100)
    image = models.FileField()
    details = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    OFFICER = models.ForeignKey(officer,on_delete=models.CASCADE)

class s_product_request(models.Model):
    FARMER= models.ForeignKey(farmer,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100)
    price = models.IntegerField()


class sorder_details (models.Model):
    PRODUCT = models.ForeignKey(subsidy_product,on_delete=models.CASCADE)
    ORDER = models.ForeignKey(s_product_request,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    date = models.DateField()








