from Configurables import Moore
#Moore().ThresholdSettings = 'MyThresholds_PhysicsDraftEM2015'
Moore().ThresholdSettings = 'Commissioning_Physics_2015'
Moore().ForceSingleL0Configuration = False
Moore().UseTCK = False
Moore().OutputLevel = 3
Moore().EnableTimer = True
Moore().SkipEvents = 0
Moore().RemoveInputHltRawBanks = True
Moore().Split = ''
from Configurables import MooreExpert
MooreExpert().Hlt2Independent=True
from Configurables import HltConf
HltConf().Verbose = True
Moore().EnableDataOnDemand = True
Moore().EvtMax = 10000
Moore().Simulation = True
Moore().DataType = '2015'
Moore().DDDBtag = 'dddb-20140729'
Moore().CondDBtag = 'sim-20140730-vc-mu100'

#from PRConfig.TestFileDB import test_file_db
#input = test_file_db['MC2015_digi_nu2.6_B2Kstmumu_L0']
#input.run(configurable=Moore())

from Configurables import EventSelector
EventSelector().PrintFreq = 100

from Configurables import HltConf
HltConf().Verbose = True
HltConf().AdditionalHlt2Lines = (['Hlt2IncPhi','Hlt2Bs2PhiPhi'])
Moore().inputFiles =  [  'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_0.dst ', 
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_1.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_2.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_3.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_4.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_5.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_6.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_7.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_8.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_9.dst ',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_10.dst',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_11.dst',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_12.dst',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_13.dst',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_14.dst',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_15.dst',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_16.dst',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_17.dst',
                         'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/MagDown/MC2015_Bs2PhiPhi_MagDown_L0Processed_18.dst',
                              ]
#Moore().inputFiles =  [   'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_0.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_1.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_10.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_11.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_12.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_13.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_14.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_15.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_16.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_17.dst',
                          #'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/MagDown/MC2015_Bd2Kpi_MagDown_L0Processed_18.dst',
                      #]                           
                                                  
