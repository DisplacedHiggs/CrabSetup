from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsernameFromSiteDB
from datetime import datetime
import sys

# Select dataset to crab over
number = 0

# List of datasets
datasetnames = [
"/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/AODSIM",
"/DYJetsToLL_M-5to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
"/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/AODSIM",
"/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext3-v1/AODSIM",
"/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
"/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
"/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/AODSIM",
"/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/AODSIM",
"/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
"/WW_TuneCUETP8M1_13TeV-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM"
"/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
"/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/AODSIM",
"/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring16DR80-PUSpring16_magnetOn_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
"/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
#"/WWTo2L2Nu_13TeV-powheg/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
#"/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
#"/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
#"/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
#"/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
#"/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/AODSIM",
#"/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
#"/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
"/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM",
]
# Storage path for output files
#storagepath = '/store/user/'+getUsernameFromSiteDB()+'/mwalker/NTUPLES/2016/Data'
storagepath = '/store/group/lpcmbja/'+getUsernameFromSiteDB()+'/2016/DisplacedDijet'

# cmsRun file
psetname = 'runDisplacedMC_cfg.py'

# Output filename
OutputFilename = 'results.root'

# Storage site of output files
#storageSite = 'T3_US_Rutgers'
storageSite = 'T3_US_FNALLPC'

# White list sites
whiteList = ['']

# Black list sites
blackList = ['']


########## No modifications below this line are necessary ##########

dataset = filter(None, datasetnames[number].split('/'))

config = config()

#config.General.workArea = "job_"+datetime.now().strftime("%Y%m%d_%H%M%S")
#config.General.requestName = dataset[0]+"_"+dataset[1]
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = psetname 
config.JobType.outputFiles = [OutputFilename]
config.JobType.pyCfgParams = ['outputFile='+OutputFilename]

config.Data.inputDataset = datasetnames[number]
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.ignoreLocality = True
config.Data.outLFNDirBase = storagepath
config.Data.publication = False

config.Site.storageSite = storageSite

if not whiteList:
  config.Site.whitelist = whiteList

if not blackList:
  config.Site.blacklist = blackList

if __name__ == '__main__':

  from CRABAPI.RawCommand import crabCommand
  
  for dataset in datasetnames:
    print dataset
    ds = filter(None, dataset.split('/'))
    config.Data.inputDataset = dataset
    config.Data.unitsPerJob = 2
    config.Data.inputDBS = 'global'
    config.General.requestName = ds[0]
    config.General.workArea = "job_"+datetime.now().strftime("%Y%m%d")+"_"+ds[0]
    config.Data.outputDatasetTag = ds[1]+'_'+ds[2]
    
    crabCommand('submit', config = config)
