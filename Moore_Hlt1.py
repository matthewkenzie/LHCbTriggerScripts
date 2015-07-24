#!/usr/bin/env python
#
# script to make trigger ntuples

import GaudiPython
import Gaudi.Configuration
from Gaudi.Configuration import *
from LHCbKernel.Configuration import *
from Configurables import Moore,HltConf,ToolSvc,DstConf,CaloDstUnPackConf
from ROOT import *
from math import *
from array import *
from files import all_runoptions

import sys

def printUsage():
  print 'usage python Moore_Hlt1.py <setting> <nevents>'
  print 'Available settings:'
  keys = sorted(all_runoptions.keys())
  for run_opt in keys:
    print '\t', run_opt
  sys.exit()

if len(sys.argv)!=2 and len(sys.argv)!=3:
  printUsage()

if sys.argv[1] not in all_runoptions.keys():
  print 'You requested run option %s which is not a valid setting'%sys.argv[1]
  printUsage()

eventstorun = 1000
if len(sys.argv)==3:
  eventstorun = int(sys.argv[2])
  print 'Requested nevents = %d'%eventstorun
else:
  print 'No request for nevents. Using default nevents = %d'%eventstorun

##################################################
##                RUN CONFIG                    ##
##################################################

run_opts = all_runoptions[sys.argv[1]]

from Configurables import EventSelector
if run_opts.runType == 'MinBias':
  EventSelector().PrintFreq = 1000
else:
  EventSelector().PrintFreq = 100

##################################################
##               MOORE CONFIG                   ##
##################################################

# if you want to generate a configuration, uncomment the following lines:
#Moore().generateConfig = True
#Moore().configLabel = 'Default'
#Moore().ThresholdSettings = 'Commissioning_PassThrough'
#Moore().configLabel = 'ODINRandom acc=0, TELL1Error acc=1'

#Moore().ThresholdSettings = 'Physics_draftEM2015'
Moore().ThresholdSettings = 'Commissioning_Physics_2015'
Moore().ForceSingleL0Configuration = False

Moore().inputFiles   = run_opts.files
Moore().DDDBtag      = run_opts.DDDBtag
Moore().CondDBtag    = run_opts.CondDBtag
Moore().Simulation   = run_opts.Simulation
Moore().DataType     = run_opts.DataType
Moore().UseTCK       = run_opts.UseTCK

Moore().OutputLevel = 3
Moore().EnableTimer = True
Moore().SkipEvents = 0
#from Configurables import HltRecoConf
#HltRecoConf.MoreOfflineLikeFit = False

# default is HltDecisionSequence, which Split = 'Hlt1' will remove (maybe it should remove Hlt2 from HltDecisionSequence instead???)
#Moore().WriterRequires = [ 'Hlt1' ]
#Moore().outputFile = '/data/bfys/graven/0x46/hlt1.raw'
Moore().RemoveInputHltRawBanks = True
Moore().Split = 'Hlt1'
Moore().EnableDataOnDemand = True
from Configurables import MooreExpert
MooreExpert().Hlt2Independent=True
from Configurables import HltConf
HltConf().Verbose = True

#### ENABLE UNPACKING ####
DstConf           ( EnableUnpack = ["Reconstruction","Stripping"] )
CaloDstUnPackConf().Enable = True

##################################################
##               GAUDI CONFIG                   ##
##################################################

from Configurables import ApplicationMgr
appConf = ApplicationMgr()
appConf.HistogramPersistency = 'ROOT'
gaudi = GaudiPython.AppMgr(outputlevel=3)
gaudi.initialize()
TES = gaudi.evtsvc()

from trigtree import *
trigtree(gaudi, TES, run_opts.MCFilterLoc, eventstorun, run_opts.output)
