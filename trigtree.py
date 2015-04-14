import ROOT
import array
import GaudiPython

def getIP(calc, track, vertex, ip, ipchi2):
  calc.distance(track, vertex ,ip ,ipchi2)

def getMinIP(calc, track, vertices, result_ip, result_ipchi2):
  minip      = ROOT.Double(1.e10)
  minipchi2  = ROOT.Double(1.e10)
  for vertex in vertices:
    ip = ROOT.Double(1.e10)
    ipchi2 = ROOT.Double(1.e10)
    getIP(calc, track, vertex, ip, ipchi2)
    if ipchi2 < minipchi2:
      minip = ip
      minipchi2 = ipchi2

  result_ip = minip
  result_ipchi2 = minipchi2

def getDira(particle, pv):
  p = particle.momentum()
  dirvec = ROOT.TVector3(p.Px(), p.Py(), p.Pz())
  endpos = particle.endVertex().position()
  pvpos  = pv.position()
  posvec = ROOT.TVector3(endpos.X()-pvpos.X(), endpos.Y()-pvpos.Y(), endpos.Z()-pvpos.Z())
  norm = ROOT.TMath.Sqrt(dirvec.Mag2()*posvec.Mag2())
  dira = dirvec.Dot(posvec)/norm
  return dira

def getFD(calc, particle, pv, fd, fdchi2):
  calc.distance(pv,particle.endVertex(),fd,fdchi2)

def getPV(particle, pvs):

  assocpv = 0
  bestdira = -1
  for pv in pvs:
    dira = getDira(particle,pv)
    if dira > bestdira:
      assocpv = pv
      bestdira = dira
  return assocpv

def trigtree(gaudi, TES, mcfilterlocation, nevents, fname):

  outputFile = ROOT.TFile(fname, 'RECREATE')
  outputTree = ROOT.TTree('TriggerAnalysisTree','Trigger Analysis Tree For Signal MC')
  
  maxarraylen = 500

  # L0 Dec branches
  L0_Any                    = array.array('i',[0])
  L0_Physics                = array.array('i',[0])
  L0_Hadron                 = array.array('i',[0])
  L0_Photon                 = array.array('i',[0])
  L0_Electron               = array.array('i',[0])
  L0_Muon                   = array.array('i',[0])
  L0_DiMuon                 = array.array('i',[0])
  outputTree.Branch('L0_Any',                 L0_Any,                'L0_Any/I')
  outputTree.Branch('L0_Physics',             L0_Physics,            'L0_Physics/I')
  outputTree.Branch('L0_Hadron',              L0_Hadron,             'L0_Hadron/I')
  outputTree.Branch('L0_Electron',            L0_Electron,           'L0_Electron/I')
  outputTree.Branch('L0_Photon',              L0_Photon,             'L0_Photon/I')
  outputTree.Branch('L0_Muon',                L0_Muon,               'L0_Muon/I')
  outputTree.Branch('L0_DiMuon',              L0_DiMuon,             'L0_DiMuon/I')

  # HLT1 Dec branches               
  Hlt1TrackAllL0            = array.array('i',[0])
  Hlt1TrackMVA              = array.array('i',[0])
  Hlt1TwoTrackMVA           = array.array('i',[0])
  Hlt1CalibTrackingKPi      = array.array('i',[0]) 
  Hlt1CalibTrackingKK       = array.array('i',[0])
  Hlt1CalibTrackingPiPi     = array.array('i',[0])
  Hlt1B2HH_LTUNB_KPi        = array.array('i',[0])
  Hlt1B2HH_LTUNB_KK         = array.array('i',[0])
  Hlt1B2HH_LTUNB_PiPi       = array.array('i',[0])
  Hlt1IncPhi                = array.array('i',[0])
  Hlt1B2PhiPhi_LTUNB        = array.array('i',[0])
  Hlt1B2PhiGamma_LTUNB      = array.array('i',[0])
  outputTree.Branch('Hlt1TrackAllL0',         Hlt1TrackAllL0,        'Hlt1TrackAllL0/I')              
  outputTree.Branch('Hlt1TrackMVA',           Hlt1TrackMVA,          'Hlt1TrackMVA/I')              
  outputTree.Branch('Hlt1TwoTrackMVA',        Hlt1TwoTrackMVA,       'Hlt1TwoTrackMVA /I')          
  outputTree.Branch('Hlt1CalibTrackingKPi',   Hlt1CalibTrackingKPi,  'Hlt1CalibTrackingKPi/I')
  outputTree.Branch('Hlt1CalibTrackingKK',    Hlt1CalibTrackingKK,   'Hlt1CalibTrackingKK/I')
  outputTree.Branch('Hlt1CalibTrackingPiPi',  Hlt1CalibTrackingPiPi, 'Hlt1CalibTrackingPiPi/I')
  outputTree.Branch('Hlt1B2HH_LTUNB_KPi',     Hlt1B2HH_LTUNB_KPi,    'Hlt1B2HH_LTUNB_KPi/I')
  outputTree.Branch('Hlt1B2HH_LTUNB_KK',      Hlt1B2HH_LTUNB_KK,     'Hlt1B2HH_LTUNB_KK/I')
  outputTree.Branch('Hlt1B2HH_LTUNB_PiPi',    Hlt1B2HH_LTUNB_PiPi,   'Hlt1B2HH_LTUNB_PiPi/I')
  outputTree.Branch('Hlt1IncPhi',             Hlt1IncPhi,            'Hlt1IncPhi/I')
  outputTree.Branch('Hlt1B2PhiPhi_LTUNB',     Hlt1B2PhiPhi_LTUNB,    'Hlt1B2PhiPhi_LTUNB/I')
  outputTree.Branch('Hlt1B2PhiGamma_LTUNB',   Hlt1B2PhiGamma_LTUNB,  'Hlt1B2PhiGamma_LTUNB/I')
 
  # MC Candidates
  mcCands                   = array.array('i',[0])
  D0_MC_M                   = array.array('d',maxarraylen*[0])
  D0_MC_P                   = array.array('d',maxarraylen*[0])
  D0_MC_PT                  = array.array('d',maxarraylen*[0])
  D0_MC_PX                  = array.array('d',maxarraylen*[0])
  D0_MC_PY                  = array.array('d',maxarraylen*[0])
  D0_MC_PZ                  = array.array('d',maxarraylen*[0])
  D0_MC_E                   = array.array('d',maxarraylen*[0])
  D0_MC_PID                 = array.array('i',maxarraylen*[0])
  D0_MC_VTX_X               = array.array('d',maxarraylen*[0])
  D0_MC_VTX_Y               = array.array('d',maxarraylen*[0])
  D0_MC_VTX_Z               = array.array('d',maxarraylen*[0])
  D0_MC_VTX_CHI2            = array.array('d',maxarraylen*[0])
  D0_MC_VTX_nDOF            = array.array('d',maxarraylen*[0])
  D0_MC_DIRA                = array.array('d',maxarraylen*[0])
  D0_MC_FD                  = array.array('d',maxarraylen*[0])
  D0_MC_FD_CHI2             = array.array('d',maxarraylen*[0])
  D0_MC_CTAU                = array.array('d',maxarraylen*[0])
  D0_MC_TAU                 = array.array('d',maxarraylen*[0])
  D0_MC_Daught1_PID         = array.array('i',maxarraylen*[0])
  D0_MC_Daught1_M           = array.array('d',maxarraylen*[0])
  D0_MC_Daught1_P           = array.array('d',maxarraylen*[0])
  D0_MC_Daught1_PT          = array.array('d',maxarraylen*[0])
  D0_MC_Daught1_IP          = array.array('d',maxarraylen*[0])
  D0_MC_Daught1_IP_CHI2     = array.array('d',maxarraylen*[0])
  D0_MC_Daught1_Track_CHI2  = array.array('d',maxarraylen*[0])
  D0_MC_Daught1_Track_nDOF  = array.array('d',maxarraylen*[0])
  D0_MC_Daught2_PID         = array.array('i',maxarraylen*[0])
  D0_MC_Daught2_M           = array.array('d',maxarraylen*[0])
  D0_MC_Daught2_P           = array.array('d',maxarraylen*[0])
  D0_MC_Daught2_PT          = array.array('d',maxarraylen*[0])
  D0_MC_Daught2_IP          = array.array('d',maxarraylen*[0])
  D0_MC_Daught2_IP_CHI2     = array.array('d',maxarraylen*[0])
  D0_MC_Daught2_Track_CHI2  = array.array('d',maxarraylen*[0])
  D0_MC_Daught2_Track_nDOF  = array.array('d',maxarraylen*[0])
  
  outputTree.Branch('mcCands',                    mcCands,                    'mcCands/I')         
  outputTree.Branch('D0_MC_M',                    D0_MC_M,                    'D0_MC_M[mcCands]/D'),
  outputTree.Branch('D0_MC_P',                    D0_MC_P,                    'D0_MC_P[mcCands]/D'),
  outputTree.Branch('D0_MC_PT',                   D0_MC_PT,                   'D0_MC_PT[mcCands]/D'),
  outputTree.Branch('D0_MC_PX',                   D0_MC_PX,                   'D0_MC_PX[mcCands]/D'),
  outputTree.Branch('D0_MC_PY',                   D0_MC_PY,                   'D0_MC_PY[mcCands]/D'),
  outputTree.Branch('D0_MC_PZ',                   D0_MC_PZ,                   'D0_MC_PZ[mcCands]/D'),
  outputTree.Branch('D0_MC_E',                    D0_MC_E,                    'D0_MC_E[mcCands]/D'),
  outputTree.Branch('D0_MC_PID',                  D0_MC_PID,                  'D0_MC_PID[mcCands]/I'),
  outputTree.Branch('D0_MC_VTX_X',                D0_MC_VTX_X,                'D0_MC_VTX_X[mcCands]/D'),
  outputTree.Branch('D0_MC_VTX_Y',                D0_MC_VTX_Y,                'D0_MC_VTX_Y[mcCands]/D'),
  outputTree.Branch('D0_MC_VTX_Z',                D0_MC_VTX_Z,                'D0_MC_VTX_Z[mcCands]/D'),
  outputTree.Branch('D0_MC_VTX_CHI2',             D0_MC_VTX_CHI2,             'D0_MC_VTX_CHI2[mcCands]/D'),
  outputTree.Branch('D0_MC_VTX_nDOF',             D0_MC_VTX_nDOF,             'D0_MC_VTX_nDOF[mcCands]/D'),
  outputTree.Branch('D0_MC_DIRA',                 D0_MC_DIRA,                 'D0_MC_DIRA[mcCands]/D'),
  outputTree.Branch('D0_MC_FD',                   D0_MC_FD,                   'D0_MC_FD[mcCands]/D'),
  outputTree.Branch('D0_MC_FD_CHI2',              D0_MC_FD_CHI2,              'D0_MC_FD_CHI2[mcCands]/D'),
  outputTree.Branch('D0_MC_CTAU',                 D0_MC_CTAU,                 'D0_MC_CTAU[mcCands]/D'),
  outputTree.Branch('D0_MC_TAU',                  D0_MC_TAU,                  'D0_MC_TAU[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught1_PID',          D0_MC_Daught1_PID,          'D0_MC_Daught1_PID[mcCands]/I'),
  outputTree.Branch('D0_MC_Daught1_M',            D0_MC_Daught1_M,            'D0_MC_Daught1_M[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught1_P',            D0_MC_Daught1_P,            'D0_MC_Daught1_P[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught1_PT',           D0_MC_Daught1_PT,           'D0_MC_Daught1_PT[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught1_IP',           D0_MC_Daught1_IP,           'D0_MC_Daught1_IP[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught1_IP_CHI2',      D0_MC_Daught1_IP_CHI2,      'D0_MC_Daught1_IP_CHI2[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught1_Track_CHI2',   D0_MC_Daught1_Track_CHI2,   'D0_MC_Daught1_Track_CHI2[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught1_Track_nDOF',   D0_MC_Daught1_Track_nDOF,   'D0_MC_Daught1_Track_nDOF[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught2_PID',          D0_MC_Daught2_PID,          'D0_MC_Daught2_PID[mcCands]/I'),
  outputTree.Branch('D0_MC_Daught2_M',            D0_MC_Daught2_M,            'D0_MC_Daught2_M[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught2_P',            D0_MC_Daught2_P,            'D0_MC_Daught2_P[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught2_PT',           D0_MC_Daught2_PT,           'D0_MC_Daught2_PT[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught2_IP',           D0_MC_Daught2_IP,           'D0_MC_Daught2_IP[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught2_IP_CHI2',      D0_MC_Daught2_IP_CHI2,      'D0_MC_Daught2_IP_CHI2[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught2_Track_CHI2',   D0_MC_Daught2_Track_CHI2,   'D0_MC_Daught2_Track_CHI2[mcCands]/D'),
  outputTree.Branch('D0_MC_Daught2_Track_nDOF',   D0_MC_Daught2_Track_nDOF,   'D0_MC_Daught2_Track_nDOF[mcCands]/D'),
 
  # Online Cands
  onCands                   = array.array('i',[0])
  D0_ON_M                   = array.array('d',maxarraylen*[0])
  D0_ON_P                   = array.array('d',maxarraylen*[0])
  D0_ON_PT                  = array.array('d',maxarraylen*[0])
  D0_ON_PX                  = array.array('d',maxarraylen*[0])
  D0_ON_PY                  = array.array('d',maxarraylen*[0])
  D0_ON_PZ                  = array.array('d',maxarraylen*[0])
  D0_ON_E                   = array.array('d',maxarraylen*[0])
  D0_ON_PID                 = array.array('i',maxarraylen*[0])
  D0_ON_VTX_X               = array.array('d',maxarraylen*[0])
  D0_ON_VTX_Y               = array.array('d',maxarraylen*[0])
  D0_ON_VTX_Z               = array.array('d',maxarraylen*[0])
  D0_ON_VTX_CHI2            = array.array('d',maxarraylen*[0])
  D0_ON_VTX_nDOF            = array.array('d',maxarraylen*[0])
  D0_ON_DIRA                = array.array('d',maxarraylen*[0])
  D0_ON_FD                  = array.array('d',maxarraylen*[0])
  D0_ON_FD_CHI2             = array.array('d',maxarraylen*[0])
  D0_ON_CTAU                = array.array('d',maxarraylen*[0])
  D0_ON_TAU                 = array.array('d',maxarraylen*[0])
  D0_ON_Daught1_PID         = array.array('i',maxarraylen*[0])
  D0_ON_Daught1_M           = array.array('d',maxarraylen*[0])
  D0_ON_Daught1_P           = array.array('d',maxarraylen*[0])
  D0_ON_Daught1_PT          = array.array('d',maxarraylen*[0])
  D0_ON_Daught1_IP          = array.array('d',maxarraylen*[0])
  D0_ON_Daught1_IP_CHI2     = array.array('d',maxarraylen*[0])
  D0_ON_Daught1_Track_CHI2  = array.array('d',maxarraylen*[0])
  D0_ON_Daught1_Track_nDOF  = array.array('d',maxarraylen*[0])
  D0_ON_Daught2_PID         = array.array('i',maxarraylen*[0])
  D0_ON_Daught2_M           = array.array('d',maxarraylen*[0])
  D0_ON_Daught2_P           = array.array('d',maxarraylen*[0])
  D0_ON_Daught2_PT          = array.array('d',maxarraylen*[0])
  D0_ON_Daught2_IP          = array.array('d',maxarraylen*[0])
  D0_ON_Daught2_IP_CHI2     = array.array('d',maxarraylen*[0])
  D0_ON_Daught2_Track_CHI2  = array.array('d',maxarraylen*[0])
  D0_ON_Daught2_Track_nDOF  = array.array('d',maxarraylen*[0])
                            
  outputTree.Branch('onCands',                    onCands,                    'onCands/I')         
  outputTree.Branch('D0_ON_M',                    D0_ON_M,                    'D0_ON_M[onCands]/D'),
  outputTree.Branch('D0_ON_P',                    D0_ON_P,                    'D0_ON_P[onCands]/D'),
  outputTree.Branch('D0_ON_PT',                   D0_ON_PT,                   'D0_ON_PT[onCands]/D'),
  outputTree.Branch('D0_ON_PX',                   D0_ON_PX,                   'D0_ON_PX[onCands]/D'),
  outputTree.Branch('D0_ON_PY',                   D0_ON_PY,                   'D0_ON_PY[onCands]/D'),
  outputTree.Branch('D0_ON_PZ',                   D0_ON_PZ,                   'D0_ON_PZ[onCands]/D'),
  outputTree.Branch('D0_ON_E',                    D0_ON_E,                    'D0_ON_E[onCands]/D'),
  outputTree.Branch('D0_ON_PID',                  D0_ON_PID,                  'D0_ON_PID[onCands]/I'),
  outputTree.Branch('D0_ON_VTX_X',                D0_ON_VTX_X,                'D0_ON_VTX_X[onCands]/D'),
  outputTree.Branch('D0_ON_VTX_Y',                D0_ON_VTX_Y,                'D0_ON_VTX_Y[onCands]/D'),
  outputTree.Branch('D0_ON_VTX_Z',                D0_ON_VTX_Z,                'D0_ON_VTX_Z[onCands]/D'),
  outputTree.Branch('D0_ON_VTX_CHI2',             D0_ON_VTX_CHI2,             'D0_ON_VTX_CHI2[onCands]/D'),
  outputTree.Branch('D0_ON_VTX_nDOF',             D0_ON_VTX_nDOF,             'D0_ON_VTX_nDOF[onCands]/D'),
  outputTree.Branch('D0_ON_DIRA',                 D0_ON_DIRA,                 'D0_ON_DIRA[onCands]/D'),
  outputTree.Branch('D0_ON_FD',                   D0_ON_FD,                   'D0_ON_FD[onCands]/D'),
  outputTree.Branch('D0_ON_FD_CHI2',              D0_ON_FD_CHI2,              'D0_ON_FD_CHI2[onCands]/D'),
  outputTree.Branch('D0_ON_CTAU',                 D0_ON_CTAU,                 'D0_ON_CTAU[onCands]/D'),
  outputTree.Branch('D0_ON_TAU',                  D0_ON_TAU,                  'D0_ON_TAU[onCands]/D'),
  outputTree.Branch('D0_ON_Daught1_PID',          D0_ON_Daught1_PID,          'D0_ON_Daught1_PID[onCands]/I'),
  outputTree.Branch('D0_ON_Daught1_M',            D0_ON_Daught1_M,            'D0_ON_Daught1_M[onCands]/D'),
  outputTree.Branch('D0_ON_Daught1_P',            D0_ON_Daught1_P,            'D0_ON_Daught1_P[onCands]/D'),
  outputTree.Branch('D0_ON_Daught1_PT',           D0_ON_Daught1_PT,           'D0_ON_Daught1_PT[onCands]/D'),
  outputTree.Branch('D0_ON_Daught1_IP',           D0_ON_Daught1_IP,           'D0_ON_Daught1_IP[onCands]/D'),
  outputTree.Branch('D0_ON_Daught1_IP_CHI2',      D0_ON_Daught1_IP_CHI2,      'D0_ON_Daught1_IP_CHI2[onCands]/D'),
  outputTree.Branch('D0_ON_Daught1_Track_CHI2',   D0_ON_Daught1_Track_CHI2,   'D0_ON_Daught1_Track_CHI2[onCands]/D'),
  outputTree.Branch('D0_ON_Daught1_Track_nDOF',   D0_ON_Daught1_Track_nDOF,   'D0_ON_Daught1_Track_nDOF[onCands]/D'),
  outputTree.Branch('D0_ON_Daught2_PID',          D0_ON_Daught2_PID,          'D0_ON_Daught2_PID[onCands]/I'),
  outputTree.Branch('D0_ON_Daught2_M',            D0_ON_Daught2_M,            'D0_ON_Daught2_M[onCands]/D'),
  outputTree.Branch('D0_ON_Daught2_P',            D0_ON_Daught2_P,            'D0_ON_Daught2_P[onCands]/D'),
  outputTree.Branch('D0_ON_Daught2_PT',           D0_ON_Daught2_PT,           'D0_ON_Daught2_PT[onCands]/D'),
  outputTree.Branch('D0_ON_Daught2_IP',           D0_ON_Daught2_IP,           'D0_ON_Daught2_IP[onCands]/D'),
  outputTree.Branch('D0_ON_Daught2_IP_CHI2',      D0_ON_Daught2_IP_CHI2,      'D0_ON_Daught2_IP_CHI2[onCands]/D'),
  outputTree.Branch('D0_ON_Daught2_Track_CHI2',   D0_ON_Daught2_Track_CHI2,   'D0_ON_Daught2_Track_CHI2[onCands]/D'),
  outputTree.Branch('D0_ON_Daught2_Track_nDOF',   D0_ON_Daught2_Track_nDOF,   'D0_ON_Daught2_Track_nDOF[onCands]/D'),
 
  calc =  gaudi.toolsvc().create('LoKi::DistanceCalculator',interface ='IDistanceCalculator')

  print 'Will run', nevents, 'events'
                            
  for ev in range(nevents):

    gaudi.run(1)

    # check for raw event
    if not TES["/Event/DAQ/RawEvent"]: continue

    # get l0 decisions
    l0decision = TES["/Event/Trig/L0/L0DUReport"]

    # hlt1 decisions
    hlt1decision = TES["/Event/Hlt1/SelReports"]

    # mc filter particles and pvs
    mccands = TES["/Event/MCFilter/Phys/%s/Particles"%mcfilterlocation]
    mcpvs = TES["/Event/MCFilter/Rec/Vertex/Primary"]

    # trigger candidates and pvs
    trigcands = TES["/Event/Hlt/Candidates"]
    trigpvs = TES["/Event/Hlt/Vertex/PV3D"]

    if not l0decision:
      print 'WARNING -- no L0 decision found at: /Event/Trig/L0/L0DUReport'
    if not hlt1decision:
      print 'WARNING -- no HLT1 decision found at: /Event/Hlt1/SelReports'
    if not mccands and mcfilterlocation!='':
      print 'WARNING -- no MC candidates found at: /Event/MCFilter/Phys/%s/Particles'%mcfilterlocation
    if not mcpvs and mcfilterlocation!='':
      print 'WARNING -- no MC primary vertices found at: /Event/MCFilter/Rec/Vertex/Primary'
    if not trigcands:
      print 'WARNING -- no trigger candidates found at: /Event/Hlt/Candidates'
    if not trigpvs:
      print 'WARNING -- no trigger primary vertices found at: /Event/Hlt/Vertex/PV3D'

    # fill l0 info
    L0_Any[0]      = 0
    L0_Physics[0]  = 0
    L0_Hadron[0]   = 0
    L0_Photon[0]   = 0
    L0_Electron[0] = 0
    L0_Muon[0]     = 0
    L0_DiMuon[0]   = 0
    if l0decision:
      L0_Any[0]      = l0decision.decisionValue()
      L0_Physics[0]  = l0decision.decisionFromSummary()
      L0_Hadron[0]   = l0decision.channelDecisionByName('Hadron')
      L0_Electron[0] = l0decision.channelDecisionByName('Electron')
      L0_Photon[0]   = l0decision.channelDecisionByName('Photon')
      L0_Muon[0]     = l0decision.channelDecisionByName('Muon')
      L0_DiMuon[0]   = l0decision.channelDecisionByName('DiMuon')

    # fill hlt1 info
    Hlt1TrackAllL0[0]          = 0
    Hlt1TrackMVA[0]            = 0
    Hlt1TwoTrackMVA[0]         = 0
    Hlt1CalibTrackingKPi[0]    = 0 
    Hlt1CalibTrackingKK[0]     = 0
    Hlt1CalibTrackingPiPi[0]   = 0
    Hlt1B2HH_LTUNB_KPi[0]      = 0
    Hlt1B2HH_LTUNB_KK[0]       = 0
    Hlt1B2HH_LTUNB_PiPi[0]     = 0
    Hlt1IncPhi[0]              = 0
    Hlt1B2PhiPhi_LTUNB[0]      = 0
    Hlt1B2PhiGamma_LTUNB[0]    = 0
    if hlt1decision:
      Hlt1TrackAllL0[0]          = hlt1decision.hasSelectionName('Hlt1TrackAllL0Decision')
      Hlt1TrackMVA[0]            = hlt1decision.hasSelectionName('Hlt1TrackMVADecision')
      Hlt1TwoTrackMVA[0]         = hlt1decision.hasSelectionName('Hlt1TwoTrackMVADecision')
      Hlt1CalibTrackingKPi[0]    = hlt1decision.hasSelectionName('Hlt1CalibTrackingKPiDecision')
      Hlt1CalibTrackingKK[0]     = hlt1decision.hasSelectionName('Hlt1CalibTrackingKKDecision')
      Hlt1CalibTrackingPiPi[0]   = hlt1decision.hasSelectionName('Hlt1CalibTrackingPiPiDecision')
      Hlt1B2HH_LTUNB_KPi[0]      = hlt1decision.hasSelectionName('Hlt1B2HH_LTUNB_KPiDecision')
      Hlt1B2HH_LTUNB_KK[0]       = hlt1decision.hasSelectionName('Hlt1B2HH_LTUNB_KKDecision')
      Hlt1B2HH_LTUNB_PiPi[0]     = hlt1decision.hasSelectionName('Hlt1B2HH_LTUNB_PiPiDecision')
      Hlt1IncPhi[0]              = hlt1decision.hasSelectionName('Hlt1IncPhiDecision')
      Hlt1B2PhiPhi_LTUNB[0]      = hlt1decision.hasSelectionName('Hlt1B2PhiPhi_LTUNBDecision')
      Hlt1B2PhiGamma_LTUNB[0]    = hlt1decision.hasSelectionName('Hlt1B2PhiGamma_LTUNBDecision')
  
    # init mc arrays
    mcCands[0] = 0
    for i in range(maxarraylen):
      D0_MC_M[i]                  = -99999.
      D0_MC_P[i]                  = -99999.
      D0_MC_PT[i]                 = -99999.
      D0_MC_PX[i]                 = -99999.
      D0_MC_PY[i]                 = -99999.
      D0_MC_PZ[i]                 = -99999.
      D0_MC_E[i]                  = -99999.
      D0_MC_PID[i]                = -99999
      D0_MC_VTX_X[i]              = -99999.
      D0_MC_VTX_Y[i]              = -99999.
      D0_MC_VTX_Z[i]              = -99999.
      D0_MC_VTX_CHI2[i]           = -99999.
      D0_MC_VTX_nDOF[i]           = -99999.
      D0_MC_DIRA[i]               = -99999.
      D0_MC_FD[i]                 = -99999.
      D0_MC_FD_CHI2[i]            = -99999.
      D0_MC_CTAU[i]               = -99999.
      D0_MC_TAU[i]                = -99999.
      D0_MC_Daught1_PID[i]        = -99999
      D0_MC_Daught1_M[i]          = -99999.
      D0_MC_Daught1_P[i]          = -99999.
      D0_MC_Daught1_PT[i]         = -99999.
      D0_MC_Daught1_IP[i]         = -99999.
      D0_MC_Daught1_IP_CHI2[i]    = -99999.
      D0_MC_Daught1_Track_CHI2[i] = -99999.
      D0_MC_Daught1_Track_nDOF[i] = -99999.
      D0_MC_Daught2_PID[i]        = -99999
      D0_MC_Daught2_M[i]          = -99999.
      D0_MC_Daught2_P[i]          = -99999.
      D0_MC_Daught2_PT[i]         = -99999.
      D0_MC_Daught2_IP[i]         = -99999.
      D0_MC_Daught2_IP_CHI2[i]    = -99999.
      D0_MC_Daught2_Track_CHI2[i] = -99999.
      D0_MC_Daught2_Track_nDOF[i] = -99999.
  
    # fill mc info
    if mccands:
      mcCands[0] = len(mcCands)
      for i, mccand in enumerate(mcCands):
        D0_MC_M[i]                   = mccand.momentum().M()
        D0_MC_P[i]                   = mccand.p()
        D0_MC_PT[i]                  = mccand.pt()
        D0_MC_PX[i]                  = mccand.momentum().Px()
        D0_MC_PY[i]                  = mccand.momentum().Py()
        D0_MC_PZ[i]                  = mccand.momentum().Pz()
        D0_MC_E[i]                   = mccand.momentum().E()
        D0_MC_PID[i]                 = mccand.particleID().pid()

        if mccand.endVertex():
          D0_MC_VTX_X[i]               = mccand.endVertex().position().X()
          D0_MC_VTX_Y[i]               = mccand.endVertex().position().Y()
          D0_MC_VTX_Z[i]               = mccand.endVertex().position().Z()
          D0_MC_VTX_CHI2[i]            = mccand.endVertex().chi2()
          D0_MC_VTX_nDOF[i]            = mccand.endVertex().nDoF()

        if len(mccand.daughters())>0:
          daught1 = mccand.daughters()[0]
          track1  = mccand.daughters()[0].proto().track()
          D0_MC_Daught1_PID[i]         = daught1.particleID().pid()
          D0_MC_Daught1_M[i]           = daught1.momentum().M()
          D0_MC_Daught1_P[i]           = daught1.p()
          D0_MC_Daught1_PT[i]          = daught1.pt()
          D0_MC_Daught1_Track_CHI2[i]  = track1.chi2()
          D0_MC_Daught1_Track_nDOF[i]  = track1.nDoF()
          minip     = ROOT.Double(1.e10)
          minipchi2 = ROOT.Double(1.e10)
          if mcpvs:
            getMinIP(calc, track1, mcpvs, minip, minipchi2)
            D0_MC_Daught1_IP[i]      = minip
            D0_MC_Daught1_IP_CHI2[i] = minipchi2

        if len(mccand.daughters())>1:
          daught2 = mccand.daughters()[1]
          track2  = mccand.daughters()[1].proto().track()
          D0_MC_Daught2_PID[i]         = daught2.particleID().pid()
          D0_MC_Daught2_M[i]           = daught2.momentum().M()
          D0_MC_Daught2_P[i]           = daught2.p()
          D0_MC_Daught2_PT[i]          = daught2.pt()
          D0_MC_Daught2_Track_CHI2[i]  = track2.chi2()
          D0_MC_Daught2_Track_nDOF[i]  = track2.nDoF()
          minip     = ROOT.Double(1.e10)
          minipchi2 = ROOT.Double(1.e10)
          if mcpvs:
            getMinIP(calc, track2, mcpvs, minip, minipchi2)
            D0_MC_Daught2_IP[i]      = minip
            D0_MC_Daught2_IP_CHI2[i] = minipchi2
        
        if mcpvs:
          mcpv = getPV(mccand, mcpvs)
          D0_MC_DIRA[i] = getDira(mccand, mcpv)
          fd     = ROOT.Double(0.)
          fdchi2 = ROOT.Double(0.)
          getFD(calc, mccand, mcpv, fd, fdchi2)
          betagamma = mccand.momentum().P() / mccand.momentum().M()
          D0_MC_FD[i]      = fd
          D0_MC_FD_CHI2[i] = fdchi2
          D0_MC_CTAU[i]    = fd / betagamma
          D0_MC_TAU[i]     = ( fd /betagamma ) / 0.3
          
    # init trig arrays
    onCands[0] = 0
    for i in range(maxarraylen):
      D0_ON_M[i]                  = -99999.
      D0_ON_P[i]                  = -99999.
      D0_ON_PT[i]                 = -99999.
      D0_ON_PX[i]                 = -99999.
      D0_ON_PY[i]                 = -99999.
      D0_ON_PZ[i]                 = -99999.
      D0_ON_E[i]                  = -99999.
      D0_ON_PID[i]                = -99999
      D0_ON_VTX_X[i]              = -99999.
      D0_ON_VTX_Y[i]              = -99999.
      D0_ON_VTX_Z[i]              = -99999.
      D0_ON_VTX_CHI2[i]           = -99999.
      D0_ON_VTX_nDOF[i]           = -99999.
      D0_ON_DIRA[i]               = -99999.
      D0_ON_FD[i]                 = -99999.
      D0_ON_FD_CHI2[i]            = -99999.
      D0_ON_CTAU[i]               = -99999.
      D0_ON_TAU[i]                = -99999.
      D0_ON_Daught1_PID[i]        = -99999
      D0_ON_Daught1_M[i]          = -99999.
      D0_ON_Daught1_P[i]          = -99999.
      D0_ON_Daught1_PT[i]         = -99999.
      D0_ON_Daught1_IP[i]         = -99999.
      D0_ON_Daught1_IP_CHI2[i]    = -99999.
      D0_ON_Daught1_Track_CHI2[i] = -99999.
      D0_ON_Daught1_Track_nDOF[i] = -99999.
      D0_ON_Daught2_PID[i]        = -99999
      D0_ON_Daught2_M[i]          = -99999.
      D0_ON_Daught2_P[i]          = -99999.
      D0_ON_Daught2_PT[i]         = -99999.
      D0_ON_Daught2_IP[i]         = -99999.
      D0_ON_Daught2_IP_CHI2[i]    = -99999.
      D0_ON_Daught2_Track_CHI2[i] = -99999.
      D0_ON_Daught2_Track_nDOF[i] = -99999.
  
    # fill trig cand info
    if trigcands:
      for candidate in trigcands:
        if candidate.currentStage().__getattribute__("is")('LHCb::Particle')():
          trigcand = candidate.currentStage().get('LHCb::Particle')()
          if not trigcand.isBasicParticle():
            D0_ON_M[onCands[0]]               = trigcand.momentum().M()
            D0_ON_P[onCands[0]]               = trigcand.p()
            D0_ON_PT[onCands[0]]              = trigcand.pt()
            D0_ON_PX[onCands[0]]              = trigcand.momentum().Px()
            D0_ON_PY[onCands[0]]              = trigcand.momentum().Py()
            D0_ON_PZ[onCands[0]]              = trigcand.momentum().Pz()
            D0_ON_E[onCands[0]]               = trigcand.momentum().E()
            D0_ON_PID[onCands[0]]             = trigcand.particleID().pid()
             
            if trigcand.endVertex():
              D0_ON_VTX_X[onCands[0]]           = trigcand.endVertex().position().X()
              D0_ON_VTX_Y[onCands[0]]           = trigcand.endVertex().position().Y()
              D0_ON_VTX_Z[onCands[0]]           = trigcand.endVertex().position().Z()
              D0_ON_VTX_CHI2[onCands[0]]        = trigcand.endVertex().chi2()
              D0_ON_VTX_nDOF[onCands[0]]        = trigcand.endVertex().nDoF()

            if len(trigcand.daughters())>0:
              daught1 = trigcand.daughters()[0]
              track1  = trigcand.daughters()[0].proto().track()
              D0_ON_Daught1_PID[onCands[0]]     = daught1.particleID().pid()
              D0_ON_Daught1_M[onCands[0]]       = daught1.momentum().M()
              D0_ON_Daught1_P[onCands[0]]       = daught1.p()
              D0_ON_Daught1_PT[onCands[0]]      = daught1.pt()
              D0_ON_Daught1_Track_CHI2[i]  = track1.chi2()
              D0_ON_Daught1_Track_nDOF[i]  = track1.nDoF()
              minip     = ROOT.Double(1.e10)
              minipchi2 = ROOT.Double(1.e10)
              if trigpvs:
                getMinIP(calc, track1, trigpvs, minip, minipchi2)
                D0_ON_Daught1_IP[onCands[0]]  = minip
                D0_ON_Daught1_IP_CHI2[i] = minipchi2

            if len(trigcand.daughters())>1:
              daught2 = trigcand.daughters()[1]
              track2  = trigcand.daughters()[1].proto().track()
              D0_ON_Daught2_PID[onCands[0]]     = daught2.particleID().pid()
              D0_ON_Daught2_M[onCands[0]]       = daught2.momentum().M()
              D0_ON_Daught2_P[onCands[0]]       = daught2.p()
              D0_ON_Daught2_PT[onCands[0]]      = daught2.pt()
              D0_ON_Daught2_Track_CHI2[i]  = track2.chi2()
              D0_ON_Daught2_Track_nDOF[i]  = track2.nDoF()
              minip     = ROOT.Double(1.e10)
              minipchi2 = ROOT.Double(1.e10)
              if trigpvs:
                getMinIP(calc, track2, trigpvs, minip, minipchi2)
                D0_ON_Daught2_IP[onCands[0]]  = minip
                D0_ON_Daught2_IP_CHI2[i] = minipchi2
            
            if trigpvs:
              trigpv = getPV(trigcand, trigpvs)
              D0_ON_DIRA[i] = getDira(trigcand, trigpv)
              fd     = ROOT.Double(0.)
              fdchi2 = ROOT.Double(0.)
              getFD(calc, trigcand, trigpv, fd, fdchi2)
              betagamma = trigcand.momentum().P() / trigcand.momentum().M()
              D0_ON_FD[onCands[0]]  = fd
              D0_ON_FD_CHI2[i] = fdchi2
              D0_ON_CTAU[onCands[0]]= fd / betagamma
              D0_ON_TAU[onCands[0]] = ( fd /betagamma ) / 0.3
              
            onCands[0] += 1

    outputTree.Fill()

  outputFile.Write()
  outputFile.Close()





