import numpy as np
import sys
from media.samplingcode.code.constraints import Constraint
from media.samplingcode.code.metropolis import Metropolis
from media.samplingcode.code.SMC import SMC
# from constraints import *
# from metropolis import Metropolis
# from SMC import SMC
import time

def djangofun(method,filename,nsamples):

    print(method,filename,nsamples)

    filename=filename.lower()
    method=method.lower()

    if filename == "formulation.txt" and method == "metropolis":
        return 0,"Exceeding time limit for formulation problem using metropolis, select other methods ",0
    if filename == "alloy.txt" and method == "adaptivemetropolis":
        return 0,"Exceeding time limit for alloy problem using adaptive metropolis, select other methods ",0
    if filename == "alloy.txt" and method == "metropolis":
        return 0,"Exceeding time limit for alloy problem using metropolis, select other methods ",0

    start_time=time.time()

    input_file="media/samplingcode/inputs/examplefiles/"+filename
    output_file="static/images/"+filename
    n_results=nsamples

    constrains=Constraint(input_file)
    qstart=constrains.get_example()
    qlims=np.zeros((len(qstart),2))
    qlims[:,1]=1.0

    if method=="smc":
        sampling=SMC(model=constrains,
                        qstart=constrains.get_example(),
                        qlims=qlims,
                        nsamples=int(n_results),
                        output_file=output_file[:-4]+"_"+method+".txt",
                        plotfigures=True,
                        saveoutputfile=True)
    elif method=="metropolis" or method=="adaptivemetropolis":
        sampling=Metropolis(model=constrains,
                        qstart=constrains.get_example(),
                        qlims=qlims,
                        nsamples=int(n_results),
                        output_file=output_file[:-4]+"_"+method+".txt",
                        method=method,
                        plotfigures=True,
                        saveoutputfile=True)
    naccept,acceptratio=sampling.sample()
    comp_time=time.time()-start_time


    return 1,"Successfully Computed",int(comp_time)
