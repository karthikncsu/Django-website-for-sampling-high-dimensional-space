from django import forms

class HomePageForm(forms.Form):

    nsamplesrange= [tuple([x,x]) for x in range(100,1001,100)]
    nsamples=forms.IntegerField(label="Number of samples?",
    widget=forms.Select(choices=nsamplesrange))

    methodchoices= [
        ('smc', 'Sequential Monte Carlo'),
        ('gibbs', 'Gibbs'),
        ('adaptivemetropolis', 'Adaptive Metropolis'),
        ('metropolis', 'Metropolis'),
        ]
    method= forms.CharField(label='Method', widget=forms.Select(choices=methodchoices))

    "example.txt","formulation.txt","alloy.txt"

    selectfilechoices= [
        ('mixture.txt', 'mixture'),
        ('example.txt', 'example'),
        ('formulation.txt','formulation'),
        ('alloy.txt', 'alloy'),
        ]
    selectfile= forms.CharField(label='Select a file',
    widget=forms.Select(choices=selectfilechoices))

    # file=forms.FileField(required=False)
