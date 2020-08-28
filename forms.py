from django import forms

class Exlmapping(forms.Form):
        Job_ID = forms.CharField()
        Company_Name = forms.CharField()
        Job_Category = forms.CharField()
        Job_Sub_Category = forms.CharField()
        HR_Name = forms.CharField()
        Job_Role = forms.CharField()
        Skills_Required = forms.CharField()
        Creation_Date = forms.CharField()
        End_Date = forms.CharField()
        Number_of_openings = forms.CharField()
        Jopb_Location = forms.CharField()
        Designation_of_job = forms.CharField()
        ctc = forms.CharField()
        Min_Exp = forms.CharField()
        Max_Exp = forms.CharField()
        CompanyID = forms.CharField()
