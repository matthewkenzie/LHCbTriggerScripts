import ROOT
import array
import GaudiPython
import sys

L0_Lines = ['Hadron','Electron','Photon','Muon','DiMuon']
HLT1_Lines = [ 'Hlt1TrackAllL0','Hlt1TrackMVA','Hlt1TwoTrackMVA','Hlt1CalibTrackingKPi','Hlt1CalibTrackingKK','Hlt1CalibTrackingPiPi','Hlt1CalibTrackingKPiDetached','Hlt1B2HH_LTUNB_KPi','Hlt1B2HH_LTUNB_KK','Hlt1B2HH_LTUNB_PiPi','Hlt1IncPhi','Hlt1B2PhiPhi_LTUNB','Hlt1B2PhiGamma_LTUNB']
branches = [  
              (  'M',         'F' ),
              (  'P',         'F' ),
              (  'PT',        'F'),
              (  'PX',        'F' ), 
              (  'PY',        'F' ), 
              (  'PZ',        'F' ), 
              (  'PE',        'F' ), 
              (  'PID',       'I' ),
              (  'VTX_X',     'F' ), 
              (  'VTX_Y',     'F' ),
              (  'VTX_Z',     'F' ), 
              (  'VTX_CHI2',  'F' ),
              (  'VTX_DOF',   'I' ),
              (  'DIRA',      'F' ), 
              (  'IP',        'F' ), 
              (  'IP_CHI2',   'F' ), 
              (  'FD',        'F' ), 
              (  'FD_CHI2',   'F' ), 
              (  'CTAU',      'F' ), 
              (  'TAU' ,      'F' ),
              (  'TR_CHI2' ,  'F' ),
              (  'TR_DOF' ,   'I' ),
              (  'TR_IP' ,    'F' ),
              (  'TR_IP_CHI2','F' )
            ]

def getIP(calc, track, vertex, ip, ipchi2):
  calc.distance(track, vertex ,ip ,ipchi2)

def getMinIP(calc, track, vertices):
  minip      = ROOT.Double(1.e10)
  minipchi2  = ROOT.Double(1.e10)
  for vertex in vertices:
    ip = ROOT.Double(1.e10)
    ipchi2 = ROOT.Double(1.e10)
    getIP(calc, track, vertex, ip, ipchi2)
    if ipchi2 < minipchi2:
      minip = ip
      minipchi2 = ipchi2
  return minip, minipchi2

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

def setVal( val, name, branch_holder, iCand=0 ):
  
  if not branch_holder.has_key(name):
    sys.exit('ERROR -- branch holder has no key named for branch name '+name)
  branch_holder[name][iCand] = val

def fillCandInfo( calc, branch_holder, iCand, name, particle, pvs):

  setVal( particle.momentum().M()       , '%s_M'%name,   branch_holder, iCand )
  setVal( particle.p()                  , '%s_P'%name,   branch_holder, iCand ) 
  setVal( particle.pt()                 , '%s_PT'%name,  branch_holder, iCand )
  setVal( particle.momentum().Px()      , '%s_PX'%name,  branch_holder, iCand )
  setVal( particle.momentum().Py()      , '%s_PY'%name,  branch_holder, iCand )
  setVal( particle.momentum().Pz()      , '%s_PZ'%name,  branch_holder, iCand )
  setVal( particle.momentum().E()       , '%s_PE'%name,  branch_holder, iCand )
  setVal( particle.particleID().pid()   , '%s_PID'%name, branch_holder, iCand )
  
  if particle.endVertex():
    setVal( particle.endVertex().position().X() , '%s_VTX_X'%name,    branch_holder, iCand )
    setVal( particle.endVertex().position().Y() , '%s_VTX_Y'%name,    branch_holder, iCand )
    setVal( particle.endVertex().position().Z() , '%s_VTX_Z'%name,    branch_holder, iCand )
    setVal( particle.endVertex().chi2()         , '%s_VTX_CHI2'%name, branch_holder, iCand )
    setVal( particle.endVertex().nDoF()         , '%s_VTX_DOF'%name,  branch_holder, iCand )

    if pvs:
      pv   = getPV(particle, pvs)
      dira = getDira(particle,pv)
      ip     = ROOT.Double(0.)
      ipchi2 = ROOT.Double(0.)
      getIP(calc, particle, pv, ip, ipchi2)
      fd     = ROOT.Double(0.)
      fdchi2 = ROOT.Double(0.)
      getFD(calc, particle, pv, fd, fdchi2)
      betagamma = particle.momentum().P() / particle.momentum().M()
      ctau = fd / betagamma
      tau = ( fd / betagamma ) / 0.3
      setVal( dira ,   '%s_DIRA'%name,    branch_holder, iCand )
      setVal( ip ,     '%s_IP'%name,      branch_holder, iCand )
      setVal( ipchi2 , '%s_IP_CHI2'%name, branch_holder, iCand )
      setVal( fd ,     '%s_FD'%name,      branch_holder, iCand )
      setVal( fdchi2 , '%s_FD_CHI2'%name, branch_holder, iCand )
      setVal( ctau ,   '%s_CTAU'%name,    branch_holder, iCand )
      setVal( tau ,    '%s_TAU'%name,     branch_holder, iCand )

  if particle.isBasicParticle():
    track = particle.proto().track()
    if track:
      setVal( track.chi2(), '%s_TR_CHI2'%name,  branch_holder, iCand )
      setVal( track.nDoF(), '%s_TR_DOF'%name,   branch_holder, iCand )
      if pvs:
        tr_ip, tr_ip_chi2 = getMinIP(calc, track, pvs)
        setVal( tr_ip,      '%s_TR_IP'%name,        branch_holder, iCand )
        setVal( tr_ip_chi2, '%s_TR_IP_CHI2'%name,   branch_holder, iCand )
      
  for i, daughter in enumerate(particle.daughters()):
    fillCandInfo(calc, branch_holder, iCand, name+'_Daught%d'%(i+1), daughter, pvs)


def fillPVInfo( branch_holder, iPV, name, pv ):
  setVal( pv.position().X(), '%s_PV_X'%name, branch_holder, iPV )
  setVal( pv.position().X(), '%s_PV_Y'%name, branch_holder, iPV )
  setVal( pv.position().X(), '%s_PV_Z'%name, branch_holder, iPV )

def initBranches( branch_holder ):

  for name, arr in branch_holder.iteritems():
    for i, val in enumerate(arr):
      branch_holder[name][i] = -999999

def setTreeBranches(tree, branch_holder):

  ndaughts = 2
  depth = 2 # i.e go to two daughters at depth 2
  
  maxarraylen = 500
  cand_names = { 'MC_Mother'   : 'nMCCands' , 
                 'Trig_Mother' : 'nTrigCands'
               }
  pv_names =   { 'MC_PV'   : 'nMCPVs',
                 'Trig_PV' : 'nTrigPVs'
               }

  import itertools

  branch_holder['L0_Any']      = array.array('i',[0])
  branch_holder['L0_Physics']  = array.array('i',[0])
  tree.Branch( 'L0_Any', branch_holder['L0_Any'], 'L0_Any/I')
  tree.Branch( 'L0_Physics', branch_holder['L0_Physics'], 'L0_Physics/I')
  for l0 in L0_Lines:
    br_name = 'L0_%s'%l0
    branch_holder[br_name] = array.array('i',[0])
    tree.Branch( br_name, branch_holder[br_name], '%s/I'%br_name )
  for hlt1 in HLT1_Lines:
    branch_holder[hlt1] = array.array('i',[0])
    tree.Branch( hlt1, branch_holder[hlt1], '%s/I'%hlt1 )
  
  branch_holder['nMCCands']    =  array.array('i',[0])
  branch_holder['nMCPVs']      =  array.array('i',[0]) 
  branch_holder['nTrigCands']  =  array.array('i',[0])
  branch_holder['nTrigPVs']    =  array.array('i',[0]) 
  tree.Branch( 'nMCCands'  , branch_holder['nMCCands']  , 'nMCCands/I'   )
  tree.Branch( 'nMCPVs'    , branch_holder['nMCPVs']    , 'nMCPVs/I'     )
  tree.Branch( 'nTrigCands', branch_holder['nTrigCands'], 'nTrigCands/I' )
  tree.Branch( 'nTrigPVs'  , branch_holder['nTrigPVs']  , 'nTrigPVs/I'   )
  
  for name, number in cand_names.iteritems():
    for branch, typ in branches:
      br_name = name+'_'+branch
      branch_holder[br_name] = array.array(typ.lower(),maxarraylen*[0])
      tree.Branch( br_name, branch_holder[br_name], '%s[%s]/%s'%(br_name, number, typ) ) 
    for d in range(1,depth+1):
      a = itertools.product(range(1,ndaughts+1),repeat=d)
      for item in a:
        sub_name = name
        for i in item:
          sub_name += '_Daught'+str(i)
          for branch, typ in branches:
            br_name = sub_name+'_'+branch
            branch_holder[br_name] = array.array(typ.lower(),maxarraylen*[0])
            tree.Branch( br_name, branch_holder[br_name], '%s[%s]/%s'%(br_name, number, typ) ) 
  
  for name, number in pv_names.iteritems():
    branch_holder['%s_PV_X'%name] = array.array('f', maxarraylen*[0])
    branch_holder['%s_PV_Y'%name] = array.array('f', maxarraylen*[0])
    branch_holder['%s_PV_Z'%name] = array.array('f', maxarraylen*[0])
    tree.Branch( '%s_PV_X'%name, branch_holder['%s_PV_X'%name], '%s_PV_X[%s]/F'%(name,number) )
    tree.Branch( '%s_PV_Y'%name, branch_holder['%s_PV_Y'%name], '%s_PV_Y[%s]/F'%(name,number) )
    tree.Branch( '%s_PV_Z'%name, branch_holder['%s_PV_Z'%name], '%s_PV_Z[%s]/F'%(name,number) )

def trigtree(gaudi, TES, mcfilterlocation, nevents, fname):

  outputFile = ROOT.TFile(fname, 'RECREATE')
  outputTree = ROOT.TTree('TriggerAnalysisTree','Trigger Analysis Tree For Signal MC')
  res_tuple = {}
  setTreeBranches( outputTree, res_tuple )
  
  # need to adjust so can hold arrays of candidates -- BUS!

  calc =  gaudi.toolsvc().create('LoKi::DistanceCalculator',interface ='IDistanceCalculator')

  print 'Will run', nevents, 'events'
                            
  for ev in range(nevents):
    
    # init storage tuple
    initBranches( res_tuple )
    
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

    #if not l0decision:
      #print 'WARNING -- no L0 decision found at: /Event/Trig/L0/L0DUReport'
    #if not hlt1decision:
      #print 'WARNING -- no HLT1 decision found at: /Event/Hlt1/SelReports'
    #if not mccands and mcfilterlocation!='':
      #print 'WARNING -- no MC candidates found at: /Event/MCFilter/Phys/%s/Particles'%mcfilterlocation
    #if not mcpvs and mcfilterlocation!='':
      #print 'WARNING -- no MC primary vertices found at: /Event/MCFilter/Rec/Vertex/Primary'
    #if not trigcands:
      #print 'WARNING -- no trigger candidates found at: /Event/Hlt/Candidates'
    if not trigpvs:
      print 'WARNING -- no trigger primary vertices found at: /Event/Hlt/Vertex/PV3D'

    # fill l0 info
    setVal(0, 'L0_Any',     res_tuple)
    setVal(0, 'L0_Physics', res_tuple)
    for l0 in L0_Lines:
      setVal(0, 'L0_%s'%l0, res_tuple)

    if l0decision:
      setVal( l0decision.decisionValue(),       'L0_Any', res_tuple )
      setVal( l0decision.decisionFromSummary(), 'L0_Physics', res_tuple )
      for l0 in L0_Lines:
        setVal( l0decision.channelDecisionByName(l0), 'L0_%s'%l0, res_tuple )

    # fill hlt1 info
    for hlt1 in HLT1_Lines:
      setVal( 0, hlt1, res_tuple)

    if hlt1decision:
      for hlt1 in HLT1_Lines:
        setVal( hlt1decision.hasSelectionName('%sDecision'%hlt1), hlt1, res_tuple )

    # fill mc candidate info
    nMCCands = 0
    if mccands:
      for mccand in mccands:  
        fillCandInfo(calc, res_tuple, nMCCands, 'MC_Mother', mccand, mcpvs ) 
        nMCCands += 1
    
    # fill mc pv info
    nMCPVs = 0
    if mcpvs:
      for pv in mcpvs:
        fillPVInfo( res_tuple, nMCPVs, 'MC_PV', pv )
        nMCPVs += 1

    # fill trig candidate info
    nTrigCands = 0
    if trigcands:
      for candidate in trigcands:
        if candidate.currentStage().__getattribute__("is")('LHCb::Particle')():
          trigcand = candidate.currentStage().get('LHCb::Particle')()
          if not trigcand.isBasicParticle():
            fillCandInfo(calc, res_tuple, nTrigCands, 'Trig_Mother', trigcand, trigpvs )
            nTrigCands += 1
    
    # fill trig pv info
    nTrigPVs = 0
    if trigpvs:
      for pv in trigpvs:
        fillPVInfo( res_tuple, nTrigPVs, 'Trig_PV', pv)
        nTrigPVs += 1

    # fill from tuple here:
    outputTree.Fill()

  outputFile.Write()
  outputFile.Close()





