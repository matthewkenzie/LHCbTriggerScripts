class run_options():

  def __init__(self):
    self.name = ''
    self.files = []
    self.UseTCK = False
    self.TCK = ''
    self.MCFilterLoc = ''
    self.runType = 'MinBias'
    self.output  = 'TrigTuple.root'
    self.DDDBtag = None
    self.CondDBtag = None
    self.Simulation = None
    self.DataType = None


all_runoptions = {}

MinBias_SPD_lt_300 = run_options()
MinBias_SPD_lt_300.name = 'MinBias_SPD_lt_300'
MinBias_SPD_lt_300.UseTCK = False
MinBias_SPD_lt_300.TCK = '0xFF66'
MinBias_SPD_lt_300.MCFilterLoc = ''
MinBias_SPD_lt_300.runType = 'MinBias'
MinBias_SPD_lt_300.output  = 'MinBias_SPD_lt_300_Tuple.root'
MinBias_SPD_lt_300.DDDBtag = 'dddb-20140729'
MinBias_SPD_lt_300.CondDBtag = 'sim-20140730-vc-md100'
MinBias_SPD_lt_300.Simulation = True
MinBias_SPD_lt_300.DataType = '2015'
MinBias_SPD_lt_300.files =    [  'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_000.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_001.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_002.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_003.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_004.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_005.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_006.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_007.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_008.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_009.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_010.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_011.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_012.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_013.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_014.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_015.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_016.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_017.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_018.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_019.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_020.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_021.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_022.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_023.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_024.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_025.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_026.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_027.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_028.ldst',
                              ]
all_runoptions['MinBias_SPD_lt_300'] = MinBias_SPD_lt_300

MinBias_SPD_lt_420 = run_options()
MinBias_SPD_lt_420.name = 'MinBias_SPD_lt_420'
MinBias_SPD_lt_420.UseTCK = False
MinBias_SPD_lt_420.TCK = '0xFF65'
MinBias_SPD_lt_420.MCFilterLoc = ''
MinBias_SPD_lt_420.runType = 'MinBias'
MinBias_SPD_lt_420.DDDBtag = 'dddb-20140729'
MinBias_SPD_lt_420.CondDBtag = 'sim-20140730-vc-md100'
MinBias_SPD_lt_420.Simulation = True
MinBias_SPD_lt_420.DataType = '2015'
MinBias_SPD_lt_420.output  = 'MinBias_SPD_lt_420_Tuple.root'
MinBias_SPD_lt_420.files =    [  'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_000.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_001.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_002.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_003.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_004.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_005.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_006.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_007.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_008.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_009.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_010.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_011.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_012.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_013.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_014.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_015.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_016.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_017.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_018.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_019.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_020.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_021.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_022.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_023.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_024.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_025.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_026.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_027.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_028.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_029.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_030.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_031.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_032.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_033.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_034.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_035.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_036.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_037.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_420/MagDown/MC2015_MinBias_0xFF63_038.ldst',
                              ]
all_runoptions['MinBias_SPD_lt_420'] = MinBias_SPD_lt_420

MinBias_SPD_lt_600 = run_options()
MinBias_SPD_lt_600.name = 'MinBias_SPD_lt_600'
MinBias_SPD_lt_600.UseTCK = False
MinBias_SPD_lt_600.TCK = '0xFF67'
MinBias_SPD_lt_600.MCFilterLoc = ''
MinBias_SPD_lt_600.runType = 'MinBias'
MinBias_SPD_lt_600.DDDBtag = 'dddb-20140729'
MinBias_SPD_lt_600.CondDBtag = 'sim-20140730-vc-md100'
MinBias_SPD_lt_600.Simulation = True
MinBias_SPD_lt_600.DataType = '2015'
MinBias_SPD_lt_600.output  = 'MinBias_SPD_lt_600_Tuple.root'
MinBias_SPD_lt_600.files =    [  'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_000.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_001.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_002.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_003.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_004.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_005.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_006.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_007.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_008.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_009.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_010.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_011.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_012.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_013.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_014.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_015.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_016.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_017.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_018.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_019.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_020.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_021.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_022.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_023.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_024.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_025.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_026.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_027.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_028.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_029.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_030.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/ldst/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_031.ldst',
                              ]
all_runoptions['MinBias_SPD_lt_600'] = MinBias_SPD_lt_600

SigMC_Bd2Kpi = run_options()
SigMC_Bd2Kpi.name = 'SigMC_Bd2Kpi'
SigMC_Bd2Kpi.UseTCK = False
SigMC_Bd2Kpi.TCK = '0xFF66'
SigMC_Bd2Kpi.MCFilterLoc = 'SelBd2KPi'
SigMC_Bd2Kpi.runType = 'SigMC'
SigMC_Bd2Kpi.DDDBtag = 'dddb-20140729'
SigMC_Bd2Kpi.CondDBtag = 'sim-20140730-vc-md100'
SigMC_Bd2Kpi.Simulation = True
SigMC_Bd2Kpi.DataType = '2015'
SigMC_Bd2Kpi.output  = 'Bd2Kpi_FF66_Tuple.root'
SigMC_Bd2Kpi.files =          [  'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_0.ldst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_1.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_2.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_3.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_4.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_5.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_7.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_8.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_9.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_10.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_11.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_12.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_13.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_14.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_15.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_16.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_17.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_18.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_19.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_20.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bd2Kpi/TCK_FF66/MC2015_Bd2Kpi_0xFF66_21.ldst',
                              ]
all_runoptions['SigMC_Bd2Kpi'] = SigMC_Bd2Kpi

SigMC_Bs2PhiPhi = run_options()
SigMC_Bs2PhiPhi.name = 'SigMC_Bs2PhiPhi'
SigMC_Bs2PhiPhi.UseTCK = False
SigMC_Bs2PhiPhi.TCK = '0xFF66'
SigMC_Bs2PhiPhi.MCFilterLoc = 'SelBs2PhiPhi'
SigMC_Bs2PhiPhi.runType = 'SigMC'
SigMC_Bs2PhiPhi.DDDBtag = 'dddb-20140729'
SigMC_Bs2PhiPhi.CondDBtag = 'sim-20140730-vc-md100'
SigMC_Bs2PhiPhi.Simulation = True
SigMC_Bs2PhiPhi.DataType = '2015'
SigMC_Bs2PhiPhi.output  = 'Bs2PhiPhi_FF66_Tuple.root'
SigMC_Bs2PhiPhi.files =       [  'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_0.ldst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_1.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_2.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_3.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_4.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_5.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_6.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_7.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_8.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_9.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_10.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_11.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_12.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_13.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_14.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_15.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_16.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_17.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_18.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_19.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_20.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_21.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_22.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_23.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_25.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_26.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_27.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_28.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_29.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_30.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_31.ldst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/BnoC/Bs2PhiPhi/TCK_FF66/MC2015_Bs2PhiPhi_0xFF66_32.ldst',
                              ]
all_runoptions['SigMC_Bs2PhiPhi'] = SigMC_Bs2PhiPhi

SigMC_Dst2D0Pi_D02KK = run_options()
SigMC_Dst2D0Pi_D02KK.name = 'SigMC_Dst2D0Pi_D02KK'
SigMC_Dst2D0Pi_D02KK.UseTCK = False
SigMC_Dst2D0Pi_D02KK.TCK = '0xFF66'
SigMC_Dst2D0Pi_D02KK.MCFilterLoc = 'SelDst2D0Pi_D02KK'
SigMC_Dst2D0Pi_D02KK.runType = 'SigMC'
SigMC_Dst2D0Pi_D02KK.DDDBtag = 'dddb-20140729'
SigMC_Dst2D0Pi_D02KK.CondDBtag = 'sim-20140730-vc-md100'
SigMC_Dst2D0Pi_D02KK.Simulation = True
SigMC_Dst2D0Pi_D02KK.DataType = '2015'
SigMC_Dst2D0Pi_D02KK.output  = 'Dst2D0Pi_D02KK_FF66_Tuple.root'
SigMC_Dst2D0Pi_D02KK.files =  [  'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file00.dst',
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file01.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file02.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file04.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file05.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file06.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file08.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file09.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file10.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file11.dst', 
                                 'root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/filtered/Charm/TCK_0xFF66/MagDown_27163002_Dst2D0Pi_D02KK_file12.dst', 
                              ]
all_runoptions['SigMC_Dst2D0Pi_D02KK'] = SigMC_Dst2D0Pi_D02KK


################
## OLD FILES  ##
################
"""
MinBias_SPD_lt_300.files =    [  'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_000.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_001.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_002.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_003.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_004.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_005.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_006.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_007.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_008.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_009.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_010.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_011.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_012.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_013.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_014.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_015.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_016.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_017.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_018.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_019.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_020.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_021.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_022.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_023.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_024.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_025.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_026.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_027.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_028.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_029.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_030.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_300/MagDown/MC2015_MinBias_0xFF66_031.mdf', 
                              ]
MinBias_SPD_lt_420.files =    [  'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_000.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_001.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_002.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_003.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_004.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_005.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_006.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_007.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_008.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_009.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_010.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_011.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_012.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_013.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_014.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_015.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_016.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_017.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_018.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_019.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_020.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_021.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_022.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_023.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_024.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_025.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_026.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_027.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_028.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_420/MagDown/MC2015_MinBias_0xFF65_029.mdf',
                              ]
MinBias_SPD_lt_600.files =    [  'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_000.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_001.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_002.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_003.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_004.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_005.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_006.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_007.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_008.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_009.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_010.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_011.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_012.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_013.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_014.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_015.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_016.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_017.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_018.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_019.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_020.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_021.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_022.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_023.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_024.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_025.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_026.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_027.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_028.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_029.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_030.mdf',
                                 'mdf:root://eoslhcb.cern.ch//eos/lhcb/wg/HLT/MC2015_L0Processed/mdf/SPD_lt_600/MagDown/MC2015_MinBias_0xFF67_031.mdf', 
                              ]
"""
