import FWCore.ParameterSet.Config as cms

#from Configuration.Generator.PythiaUEZ2Settings_cfi import *
from Configuration.GenProduction.EightTeV.DYToMuMu_M_20_TuneZ2_8TeV_pythia6_cff import generator

tfFilter = cms.EDFilter("DYGenFilter",
  code = cms.untracked.int32(13),
  etaMax = cms.untracked.double(2.5),
  ptMin  = cms.untracked.double(15)
)

ProductionFilterSequence = cms.Sequence(generator*tfFilter)







