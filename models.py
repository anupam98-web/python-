from django.db import models


# Create your models here.
class Mandate(models.Model):
        Job_ID = models.CharField(max_length=50)
        Company_Name = models.TextField(max_length=200)
        Job_Category= models.CharField(max_length= 100)
        Job_Sub_Category =models.CharField(max_length = 100, default='')
        HR_Name = models.TextField(max_length=100)
        Job_Role = models.CharField(max_length=3000, default='')
        Skills_Required = models.CharField(max_length=3000,default='', null=True)
        Creation_Date = models.DateField()
        End_Date = models.DateField(default='')
        Number_of_openings = models.IntegerField()
        Jopb_Location = models.CharField(max_length = 300)
        Designation_of_job = models.CharField(max_length=200, blank=True, null=True)
        ctc = models.IntegerField()
        Min_Exp = models.IntegerField()
        Max_Exp = models.IntegerField()
        CompanyID = models.CharField(max_length = 50)

        def savedata(self):
		        self.save()

