# CrabSetup
#Scripts for running and submitting jobs to crab

#CMSSW environment: We are currently using CMSSW_8_0_18_patch1
cmsrel CMSSW_8_0_18_patch1
cd CMSSW_8_0_18_patch1/src/;cmsenv

#Setup framework code:
git clone git@gitlab.com:Thomassen/RutgersIAF.git 
git clone git@gitlab.com:mhwalker/RutgersAODReader.git
#at some date in the future, we may have some tags for the code, but not at the moment

#Compile code
scram b -rj7

#setup crab 
source /cvmfs/cms.cern.ch/crab3/crab.sh

#setup certificate (good idea)
voms-proxy-init -voms cms 

#change directory to the area where this repo is checked out
#run test job:
cmsRun runDisplacedData_cfg.py

#submit crab jobs
python crabConfig_DATA_analysis.py


