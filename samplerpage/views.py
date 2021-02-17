from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HomePageForm
from django.core.files.storage import FileSystemStorage
import hashlib
from media.samplingcode.code.djangofun import djangofun

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self,request):
        form=HomePageForm()
        # args={'form':form}
        args={'form':form,"errormsg":0,'msg':"SOlution not computed",'comp_time':0}

        return render(request,self.template_name,args)


    #taking the input from the search page
    def post(self,request):
        form=HomePageForm(request.POST,request.FILES)
        if form.is_valid():
            nsamples=form.cleaned_data['nsamples']
            method=form.cleaned_data['method']
            selectfile=form.cleaned_data['selectfile']

            # uploaded_file=request.FILES['file']
            # print("--------------------------------")
            # print(uploaded_file)
            
            # if not uploaded_file.name.split('.')[1] in ["txt",'dat']:
            #     print("Not a pdf")
            #     form=HomePageForm()
            #     args={'form':form,"msg":"Only text files (.txt, .out) are accepted"}
            #     return render(request,self.template_name,args)
            
            
            # if 
            # fs=FileSystemStorage("media/samplingcode/inputs/")
            # fs.save(uploaded_file.name,uploaded_file)

            # import os
            # print(os.getcwd())

            # fout=open("./media/samplingcode/inputs/"+uploaded_file.name,"r")
            # data=fout.readlines()
            # print(data)
            

        else:
            errormsg=0
            msg="Not valid input"
            comp_time=0.0
        
        errormsg,msg,comp_time= djangofun(method,selectfile,nsamples)
        impagepath="static/images/"+selectfile[:-4]+"_"+method+".png"

        print(impagepath)

        args={'form':form,"errormsg":errormsg,'msg':msg,'comp_time':comp_time,"impagepath":impagepath}
        return render(request,self.template_name,args)


class ResultsPageView(TemplateView):
    template_name = 'results.html'
