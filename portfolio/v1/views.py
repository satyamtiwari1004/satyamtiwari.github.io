from django.shortcuts import render
from django.http import JsonResponse
from .data import experience_data,skills_data,other_projects_data,social_data

def load_home(request):
    exp_data=experience_data()
    ski_dat=skills_data()
    oth_pro_data=other_projects_data()
    soc_data=social_data()
    context={"exp_data":exp_data[0],"ski_dat":ski_dat[0],"oth_pro_data":oth_pro_data,"soc_data":soc_data}
    return render(request,"v1/index.html",context)

def load_data(request):
    exp_data=experience_data()
    ski_dat=skills_data()
    oth_pro_data=other_projects_data()
    soc_data=social_data()
    context={"exp_data":exp_data[0],"ski_dat":ski_dat[0],"oth_pro_data":oth_pro_data,"soc_data":soc_data}
    return JsonResponse({"context":context},status=200)
