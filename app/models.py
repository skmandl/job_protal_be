from django.db import models

# Create your models here.
class Category(models.Model):
    types=models.CharField(max_length=30)

    def __str__(self):
        return self.types

class Degree(models.Model):
    option=models.CharField(max_length=30)
    subject=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.option

class Company(models.Model):
    name=models.CharField(max_length=30)
    company_logo=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name

class JobType(models.Model):
    option=models.CharField(max_length=30)

    def __str__(self):
        return self.option


class JobList(models.Model):
    job_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)  
    job_type=models.ForeignKey(JobType,on_delete=models.CASCADE)
    post_name=models.CharField(max_length=30)
    degree=models.ManyToManyField(Degree)
    # description=models.ForeignKey(JobDetail,on_delete=models.CASCADE,null=True,blank=True)
    is_active=models.BooleanField(null=True,blank=True)
    last_date=models.DateField(null=True,blank=True)  
    apply_link=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.post_name


class JobDetail(models.Model):
    overview=models.TextField(max_length=800)
    job=models.ForeignKey(JobList,on_delete=models.CASCADE,null=True,blank=True)
    salary_from=models.PositiveIntegerField()
    salary_to=models.PositiveIntegerField()

    def __str__(self):
        return str(self.job)


class Recuirement(models.Model):
    job_detail=models.ForeignKey(JobDetail,on_delete=models.CASCADE)
    name=models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Responsibilities(models.Model):
    job_detail=models.ForeignKey(JobDetail,on_delete=models.CASCADE)
    name=models.TextField(max_length=200)
    def __str__(self):
        return self.name
