from django.shortcuts import render
from .models import Mandate
from .resources import JobResources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from .forms import Exlmapping

# Create your views here.

def mapcolumns(request):
    if request.method =='POST':
         col = Exlmapping(request.POST)
         # validation
         if col.is_valid():
            print('Form validation')
            # it's a dictionary {'colum': col} so we are getting value of the key that are define in our form.
            # this line will show the the value if it is verified
            Job_ID = col.cleaned_data['Job_ID']
            Company_Name = col.cleaned_data['Company_Name']
            Job_Category = col.cleaned_data['Job_Category']
            Job_Sub_Category = col.cleaned_data['Job_Sub_Category']
            HR_Name = col.cleaned_data['HR_Name']
            Job_Role = col.cleaned_data['Job_Role']
            Skills_Required = col.cleaned_data['Skills_Required']
            Creation_Date = col.cleaned_data['Creation_Date']
            End_Date = col.cleaned_data['End_Date']
            Number_of_openings = col.cleaned_data['Number_of_openings']
            Jopb_Location = col.cleaned_data['Jopb_Location']
            Designation_of_job = col.cleaned_data['Designation_of_job']
            ctc = col.cleaned_data['ctc']
            Min_Exp = col.cleaned_data['Min_Exp']
            Max_Exp = col.cleaned_data['Max_Exp']
            CompanyID = col.cleaned_data['CompanyID']

    else:
        col = Exlmapping()
        print('its from get request')

    return render(request, 'mapexl.html', {'column': col})

    mandate = Mandate()
    map = { 
            Job_ID : mandate.Job_ID,
            Company_Name : mandate.Company_Name,
            Job_Category : mandate.Job_Category,
            Job_Sub_Category: mandate.Job_Sub_Category,
            HR_Name : mandate.HR_Name,
            Job_Role : mandate.Job_Role,
            Skills_Required : mandate.Skills_Required,
            Creation_Date : mandate.Creation_Date,
            End_Date : mandate.End_Date,
            Number_of_openings : mandate.Number_of_opening,
            Jopb_Location: mandate.Jopb_Location,
            Designation_of_job : mandate.Designation_of_job,
            ctc : mandate.ctc,
            Min_Exp : mandate.Min_Exp,
            Max_Exp : mandate.Max_Exp,
            CompanyID : mandate.CompanyID,
          }
    print(map)

    if request.method== 'POST':
        job_resources = JobResources()
        dataset = Dataset()
        new_job= request.FILES['myfile']

        if not new_job.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'mapexl.html')
        imported_data = dataset.load(new_job.read(),format='xlsx')
        for data in imported_data:
            value = Mandate(
                data[0],
                data[1],
                data[2],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17]
                )
            value.save()
    return render(request,'mapexl.html')


def simple_upload(request):
    if request.method== 'POST':
        job_resources = JobResources()
        dataset = Dataset()
        new_job= request.FILES['myfile']

        if not new_job.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')
        imported_data = dataset.load(new_job.read(),format='xlsx')
        for data in imported_data:
            value = Mandate(
                data[0],
                data[1],
                data[2],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17]
                )
            value.save()
    return render(request,'upload.html')
        
