import os
from lxml import etree
from xmlreader.DataConverter import DataConverter
from bs4 import BeautifulSoup
from whoosh.index import create_in, open_dir
from whoosh.fields import *
import pickle
from whoosh.writing import BufferedWriter
from xmlreader.Post import Post

'''The goal of this class is to index posts'''

class WhooshIndexer:
    def __init__(self):
        self.list_subfolders_with_paths = [(f.path, f.name) for f in os.scandir(
            "/scratch/parvezku01/MigrationStudy/stackexchange_datadump") if
                                     f.is_dir() and f.name.startswith(".") is False]
        self.output_dir = "/scratch/parvezku01/MigrationStudy/whoosh_index_basic"
    def index(self):
        site_count = 0

        for (path, name) in self.list_subfolders_with_paths:

            schema = Schema(title=TEXT(stored=True), id=TEXT(stored=True), content=TEXT(stored=True))

            dir_path = self.output_dir+"/" + name
            print("I am working on...{} ".format(name))
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            ix = create_in(dir_path, schema)
            writer = ix.writer() #BufferedWriter(ix,period=120,limit=100000)
            count = 0
            with open("/scratch/parvezku01/MigrationStudy/post_index/"+name+".ser", "rb") as pickle_file, open("/scratch/parvezku01/MigrationStudy/post_index/"+name+"_position.ser", "rb") as pickle_position_file:
                postIdToPositionDict = pickle.load(pickle_position_file)
                for id in postIdToPositionDict:
                    if (count % 1000000 == 0):
                        print("Progress of reading posts: " + str(count))
                    count = count +1
                    post = pickle.load(pickle_file)
                    soup_title = BeautifulSoup(post.get_title(), features="lxml")
                    soup_body = BeautifulSoup(post.get_body(), features="lxml")
                    writer.add_document(title=soup_title.get_text(), id=str(post.get_id()),
                                        content=soup_body.get_text())
            writer.commit()
            site_count = site_count + 1
            print("Completed: " + str(site_count) + "/" + str(len(self.list_subfolders_with_paths)) + " " + name)

whoosh = WhooshIndexer()
whoosh.index()