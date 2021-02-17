from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HomePageForm
from django.core.files.storage import FileSystemStorage
import hashlib
# from media.samplingcode.code.testing import *

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self,request):
        form=HomePageForm()
        args={'form':form}
        return render(request,self.template_name,args)

    #taking the input from the search page
    def post(self,request):
        form=HomePageForm(request.POST,request.FILES)
        if form.is_valid():
            nsamples=form.cleaned_data['nsamples']
            method=form.cleaned_data['method']

            uploaded_file=request.FILES['file']
            if not uploaded_file.name.split('.')[1] in ["txt",'dat']:
                print("Not a pdf")
                form=HomePageForm()
                args={'form':form,"msg":"Only text files (.txt, .out) are accepted"}
                return render(request,self.template_name,args)
            
            fs=FileSystemStorage("media/samplingcode/inputs/")
            fs.save(uploaded_file.name,uploaded_file)

            # import os
            # print(os.getcwd())

            # fout=open("./media/samplingcode/inputs/"+uploaded_file.name,"r")
            # data=fout.readlines()
            # print(data)
            

        else:
            msg=0
            searchtext=""
            output=["Not valid input"]

        args={'form':form}
        return render(request,self.template_name,args)


class ResultsPageView(TemplateView):
    template_name = 'results.html'
