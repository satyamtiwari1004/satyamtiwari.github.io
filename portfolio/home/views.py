from django.shortcuts import render
from django.http import JsonResponse
from .data import experience_data,skills_data,other_projects_data

def load_home(request):
    exp_data=experience_data()
    ski_dat=skills_data()
    oth_pro_data=other_projects_data()
    context={"exp_data":exp_data,"ski_dat":ski_dat,"oth_pro_data":oth_pro_data}
    return render(request,"index.html",context)

def load_data(request):
    exp_data=experience_data()
    ski_dat=skills_data()
    oth_pro_data=other_projects_data()
    print(exp_data)
    context={"exp":exp_data,"ski_dat":ski_dat,"oth_pro_data":oth_pro_data}
    print(context)
    return JsonResponse({"context":context},status=200)
