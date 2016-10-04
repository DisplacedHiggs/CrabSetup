from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsernameFromSiteDB
from datetime import datetime
import sys

# Select dataset to crab over
number = 0

# List of datasets
datasetnames = [
"/SingleElectron/Run2016G-PromptReco-v1/AOD", #0
"/SingleMuon/Run2016G-PromptReco-v1/AOD",#1
]
# Storage path for output files
#storagepath = '/store/user/'+getUsernameFromSiteDB()+'/mwalker/NTUPLES/2016/Data'
storagepath = '/store/group/lpchbb/'+getUsernameFromSiteDB()+'/2016/DisplacedDijet'

# cmsRun file
psetname = 'runDisplacedData_cfg.py'

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
config.Data.splitting = 'LumiBased'
#config.Data.lumiMask = './json_DCSONLY_Run2015B_20150721.txt'
#config.Data.lumiMask = './golden_246908-258750_20151026.txt'
#config.Data.lumiMask = './golden_246908-260627_20151120.txt'
#config.Data.lumiMask = './Cert_271036-274240_13TeV_PromptReco_Collisions16_JSON.txt'
config.Data.lumiMask = './Cert_271036-279588_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
config.Data.runRange = '271036-279588'

config.Data.unitsPerJob = 2
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
