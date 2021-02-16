from django import forms

class HomePageForm(forms.Form):

    nsamplesrange= [tuple([x,x]) for x in range(100,1001,100)]
    nsamples=forms.IntegerField(label="Number of samples?",
    widget=forms.Select(choices=nsamplesrange))

    methodchoices= [
        ('SMC', 'Sequential Monte Carlo'),
        ('AdaptiveMetropolis', 'Adaptive Metropolis'),
        ('metropolis', 'Metropolis'),
        ]
    method= forms.CharField(label='Method', widget=forms.Select(choices=methodchoices))

    selectfilechoices= [
        ('x+y<1', 'x+y<1'),
        ('twocircles', 'Two circles'),
        ]
    selectfile= forms.CharField(label='Select a file',
    widget=forms.Select(choices=selectfilechoices))

    file=forms.FileField(required=False)
