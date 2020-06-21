import os
import pickle
import time
from lxml import etree

from Utility.SiteManager import SiteManager
from xmlreader.DataConverter import DataConverter


class DataIndexer:
    def __init__(self):
       self.list_subfolders_with_paths = [(f.path, f.name) for f in os.scandir("/media/parvez/SamsungOneTB/MigrationRecom/StackExchangeData") if f.is_dir()]
    def index_site(self,path,name, siteNameToPostPositionDict, serializePostFile):
        postIdToPosition = {}
        for event, elem in etree.iterparse(path + "/Posts.xml", events=("start", "end", "start-ns", "end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if (count % 1000000 == 0):
                    print("Progress of reading posts: " + str(count))
                post = DataConverter.readPost(elem)
                if post.get_postTypeId() == 1:
                    start_position = serializePostFile.tell()
                    pickle.dump(obj=post, file=serializePostFile)
                    postIdToPosition[post.get_id()] = start_position

        siteNameToPostPositionDict[name] = postIdToPosition
    def index(self):
        start_time = time.time()
        site_count = 0
        siteNameToPostPositionDict = {}
        with open("/media/parvez/SamsungOneTB/MigrationRecom/serialize/posts.ser", "wb") as serializePostFile:
            for (path, name) in self.list_subfolders_with_paths:
                count = 0
                '''postIdToPosition = {}
                for event, elem in etree.iterparse(path + "/Posts.xml", events=("start", "end", "start-ns", "end-ns")):
                    if elem.tag == "row" and event == "start":
                        count = count + 1
                        if (count % 1000000 == 0):
                            print("Progress of reading posts: " + str(count))
                        post = DataConverter.readPost(elem)
                        if post.get_postTypeId()==1:
                            start_position = serializePostFile.tell()
                            pickle.dump(obj=post, file=serializePostFile)
                            #postIdToPosition[post.get_id()] = start_position

                print("Completed: " + str(site_count) + "/" + str(len(self.list_subfolders_with_paths))+" "+name)
                site_count = site_count + 1
                siteNameToPostPositionDict[name] = postIdToPosition'''
                self.index_site(path,name,siteNameToPostPositionDict,serializePostFile)
                print("Completed: " + str(site_count) + "/" + str(len(self.list_subfolders_with_paths)) + " " + name)
                site_count = site_count + 1

        with open("/media/parvez/SamsungOneTB/MigrationRecom/serialize/post_position_dict.ser", "wb") as serializePostPositionDictFile:
            pickle.dump(obj=siteNameToPostPositionDict, file=serializePostPositionDictFile)
        print("Time required to read posts: " + str(time.time() - start_time))


#run the code to index all the data
dataIndexer = DataIndexer()
dataIndexer.index()