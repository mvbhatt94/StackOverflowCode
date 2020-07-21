import os
import pickle
import time
from lxml import etree

from Utility.SiteManager import SiteManager
from xmlreader.DataConverter import DataConverter

list_subfolders_with_paths = [(f.path, f.name) for f in os.scandir("/media/parvez/SamsungOneTB/MigrationRecom/StackExchangeData") if f.is_dir() and f.name.startswith(".") is False]
siteNameToMigratedPhDict = None

#step-1: load the migrated post history dictionary
with open("/media/parvez/IntelSSD/MigrationRecommender/serialize/migrate_ph_dict.ser", "rb") as pickle_file:
    siteNameToMigratedPhDict = pickle.load(pickle_file)
print("Total sites: " + str(len(siteNameToMigratedPhDict)))

site_count = 0
siteNameToMigratedPostDict = {}
for (path, name) in list_subfolders_with_paths:
    #step-2: determine migrated post ids in this site
    postIdToMigratedPostDict = {}
    phIdToPhDict = siteNameToMigratedPhDict[name]
    migrated_post_set = set()
    for id in phIdToPhDict:
        ph = phIdToPhDict[id]
        migrated_post_set.add(ph.get_postId())
    count=0
    #step-3:
    for event, elem in etree.iterparse(path + "/Posts.xml", events=("start", "end", "start-ns", "end-ns")):
        if elem.tag == "row" and event == "start":
            count = count + 1
            if (count % 1000000 == 0):
                print("Progress of reading posts: " + str(count))
            post = DataConverter.readPost(elem)
            post.set_site(name)
            if post.get_id() in migrated_post_set:
                postIdToMigratedPostDict[post.get_id()]=post
        elem.clear()
        del elem
    siteNameToMigratedPostDict[name]=postIdToMigratedPostDict
    print("Completed: " + str(site_count) + "/" + str(len(list_subfolders_with_paths)) + " " + name)
    site_count = site_count + 1

#step-4: serialize the data
with open("/media/parvez/IntelSSD/MigrationRecommender/serialize/migrated_post_dict.ser", "wb") as pickle_file:
    pickle.dump(obj=siteNameToMigratedPostDict, file=pickle_file)


