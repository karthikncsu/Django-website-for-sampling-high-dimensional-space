import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
import copy
import sys
from scipy.stats import norm
import time
import seaborn as sns
import pandas as pd

class BaseClass:
    """Class for different sampling algorithms"""

    def __init__(self,model,qstart,qlims,nsamples,output_file="samples.txt",
                        printoutput=True,plotfigures=True,saveoutputfile=True):
        """
        Construct an object from sampling method

        qstart: Initial value of sampling
        qlims: Limits of the variables
        nsamples: Number of samples
        Vstart: Variance matrix
        method: Choice of method for sampling
        output_file: File name to save the samples
        """
        self.model=model
        self.qstart=np.reshape(np.asarray(qstart),(-1,1))
        self.qlims=qlims
        self.nsamples=nsamples
        self.printoutput=printoutput
        self.plotfigures=plotfigures
        self.saveoutputfile=saveoutputfile
        self.sp=2.38**2/self.qstart.shape[0]

        self.output_file=output_file

    def printoutput(self,qsamples,ntot,neff,accpt_ratio):
        
        """
        Function to call the sampling method of choice and plot results
        """
        if self.printoutput:
            print("Total generated samples:",ntot)
            print("Total effective samples:",int(neff))
            print('Acceptance ratio:',accpt_ratio)
        
        self.testsamples(qsamples)

    def testsamples(self,qsamples):

        testinds=np.random.randint(qsamples.shape[0],size=100)
        print("---------Testing the generated samples randomly for",len(testinds),"samples---------")
        for ind in testinds:
            testval=self.model.apply(list(qsamples[ind,:]))
            if not testval:
                print("Sampling failed for sample number:",ind)
                print(self.model.apply_eval(list(qsamples[ind,:])))
        print("---------Testing successful---------")
        return

    def plotsamples(self,qsamples,method):
        """
        Function for plotting the samples
        """
        if self.plotfigures:
            filname=self.output_file[:-4]+".png"
            print("Plots saved to the folder:",filname)
            fig=sns.pairplot(pd.DataFrame(qsamples), markers='o')
            fig.savefig(filname)
        else:
            print("Plots are not generated")
        return

    def savesamples(self,qsamples,method):
        """
        Function for saving the samples
        """
        if self.saveoutputfile:
            filname=self.output_file[:-4]+".txt"
            print("Saving samples to the folder:",filname)
            np.savetxt(filname,qsamples)
        else:
            print("Results are not saved")
        return
