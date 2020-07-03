import pandas as pd
import numpy as np
from lxml import etree
import time
import pickle
import sys
import os
from Utility.SiteManager import SiteManager
from xmlreader.DataConverter import DataConverter

STACK_EXCHANGE_DATA = "/scratch/parvezku01/MigrationStudy/stackexchange_datadump"
list_subfolders_with_paths = [(f.path,f.name) for f in os.scandir(STACK_EXCHANGE_DATA) if f.is_dir() and f.name.startswith(".")==False]
for path in list_subfolders_with_paths:
    print(path)
site_manager = SiteManager("/home/local/SAIL/parvezku01/Research/MigrationStudy/data/sites_category.csv")


def collect_user_data():
    start_time = time.time()
    siteToUserData = {}
    site_count = 0
    for (path,name) in list_subfolders_with_paths:
        count = 0
        userIdToUserDict = {}
        for event, elem in etree.iterparse(path+"/Users.xml", events=("start","end","start-ns","end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if(count%1000000==0):
                    print("Progress of reading users: "+str(count))
                lu = DataConverter.readLightUser(elem)
                userIdToUserDict[lu.get_id()] = lu
        siteToUserData[name] = userIdToUserDict
        print("Completed: "+str(site_count)+"/"+str(len(list_subfolders_with_paths)))
        site_count = site_count + 1

    print('Now serialize user data...')
    with open("/scratch/parvezku01/MigrationStudy/serialize/user_dict.ser", "wb") as serializeFile:
        pickle.dump(obj=siteToUserData, file=serializeFile)
    print("--- %s seconds ---" % (time.time() - start_time))

def collect_migrated_post():
    # load the post history data
    start_time = time.time()
    siteToMigratedPhDict = {}
    site_count = 0
    for (path, name) in list_subfolders_with_paths:
        count = 0
        phIdToPhDict = {}
        ph = None
        for event, elem in etree.iterparse(path + "/PostHistory.xml", events=("start", "end", "start-ns", "end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if (count % 1000000 == 0):
                    print("Progress of reading post histories: " + str(count))
                ph = DataConverter.readPostHistory(elem)
                ph.set_site(site_manager.getSiteName(name))
                if ph.get_postHistoryTypeId() == 35 or ph.get_postHistoryTypeId() == 36:
                    phIdToPhDict[ph.get_id()] = ph
                elem.clear()
                del elem
        siteToMigratedPhDict[name] = phIdToPhDict
        print("Completed: " + str(site_count) + "/" + str(len(list_subfolders_with_paths)))
        site_count = site_count + 1
    with open("/scratch/parvezku01/MigrationStudy/serialize/migrate_ph_dict.ser",
              "wb") as serializeFile:
        pickle.dump(obj=siteToMigratedPhDict, file=serializeFile)
    print("--- %s seconds ---" % (time.time() - start_time))

#collect_user_data()

collect_migrated_post()