import os
import pickle
import time
from lxml import etree

from Utility.SiteManager import SiteManager
from xmlreader.DataConverter import DataConverter

'''The goal of this class is to collect tags or topics of migrated posts'''
class TopicDetector:
    def __init__(self):
    #The folder can contain hidden directory. so we ignore them
       self.list_subfolders_with_paths = [(f.path, f.name) for f in os.scandir("/scratch/parvezku01/MigrationStudy/stackexchange_datadump") if f.is_dir() and f.name.startswith(".") is False]
    def index_site(self,path,name,siteNameToMigratedPhDict, siteNameToMigratedPostTopic):

        # Step1: load serialized migrated post history data set
        phIdToPhDict = siteNameToMigratedPhDict[name]
        count = 0

        # Step-2: determine migrated post in this site
        migrated_post_set = set()
        for id in phIdToPhDict:
            ph=phIdToPhDict[id]
            migrated_post_set.add(ph.get_postId())

        #Step-3: determines topics for migrated post of this site
        topic_set = set()
        for event, elem in etree.iterparse(path + "/Posts.xml", events=("start", "end", "start-ns", "end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if (count % 1000000 == 0):
                    print("Progress of reading posts: " + str(count))
                post = DataConverter.readPost(elem)
                post.set_site(name)
                if post.get_postTypeId() == 1 and post.get_id() in migrated_post_set:
                    topic_set.add(post.get_tags())
            elem.clear()
            del elem
        siteNameToMigratedPostTopic[name] = topic_set
    def index(self):

        start_time = time.time()
        site_count = 0
        siteNameToMigratedPhDict = None
        with open("/scratch/parvezku01/MigrationStudy/serialize/migrate_ph_dict.ser", "rb") as pickle_file:
            siteNameToMigratedPhDict = pickle.load(pickle_file)
            print("Total sites: "+str(len(siteNameToMigratedPhDict)))

            siteNameToMigratedPostTopic = {}
            for (path, name) in self.list_subfolders_with_paths:
                self.index_site(path, name, siteNameToMigratedPhDict, siteNameToMigratedPostTopic)
                print("Completed: " + str(site_count) + "/" + str(len(self.list_subfolders_with_paths)) + " " + name)
                site_count = site_count + 1
            with open("/scratch/parvezku01/MigrationStudy/serialize/migrated_post_topic.ser", "wb") as serializeFile:
                pickle.dump(obj=siteNameToMigratedPostTopic, file=serializeFile)
        print("--- %s seconds ---" % (time.time() - start_time))

#run the code to index all the data
topic_detector = TopicDetector()
topic_detector.index()