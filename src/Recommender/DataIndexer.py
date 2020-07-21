import os
import pickle
import time
from lxml import etree

from Utility.SiteManager import SiteManager
from xmlreader.DataConverter import DataConverter

'''The goal of this class is to serialize questions of stack exchange websites and index their position using a dictionary'''
class DataIndexer:
    def __init__(self):
    #The folder can contain hidden directory. so we ignore them
       self.list_subfolders_with_paths = [(f.path, f.name) for f in os.scandir("/media/parvez/SamsungOneTB/MigrationRecom/StackExchangeData") if f.is_dir() and f.name.startswith(".") is False]
    def index_site(self,path,name):
        postIdToPosition = {}
        count = 0
        with open("/media/parvez/IntelSSD/MigrationRecommender/post_index_full/"+name+"_full.ser", "wb") as serializePostFile,open("/media/parvez/IntelSSD/MigrationRecommender/post_index_full/"+name+"_position_full.ser", "wb") as serializePositionFile:
            for event, elem in etree.iterparse(path + "/Posts.xml", events=("start", "end", "start-ns", "end-ns")):
                if elem.tag == "row" and event == "start":
                    count = count + 1
                    if (count % 1000000 == 0):
                        print("Progress of reading posts: " + str(count))
                    post = DataConverter.readPost(elem)
                    post.set_site(name)
                    if post.get_postTypeId() == 1:
                        start_position = serializePostFile.tell()
                        pickle.dump(obj=post, file=serializePostFile)
                        postIdToPosition[post.get_id()] = start_position
                elem.clear()
                del elem
            pickle.dump(obj = postIdToPosition, file = serializePositionFile)
    def index(self):
        start_time = time.time()
        site_count = 0
        for (path, name) in self.list_subfolders_with_paths:
            self.index_site(path,name)
            print("Completed: " + str(site_count) + "/" + str(len(self.list_subfolders_with_paths)) + " " + name)
            site_count = site_count + 1

        #print("Now serialize post position dictionary...")
        #with open("/scratch/parvezku01/MigrationStudy/serialize/post_position_dict_small.ser", "wb") as serializePostPositionDictFile:
        #    pickle.dump(obj=siteNameToPostPositionDict, file=serializePostPositionDictFile)
        print("Time required to read posts: " + str(time.time() - start_time))

#run the code to index all the data
dataIndexer = DataIndexer()
dataIndexer.index()