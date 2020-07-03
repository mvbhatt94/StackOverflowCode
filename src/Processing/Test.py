import pickle
import re

from bs4 import BeautifulSoup
from summa import keywords
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
from summa import summarizer

def convert_tag_to_list(input):
    text = re.sub("<|>|><"," ",input).strip()
    return re.split('\s+',text)

print(" I am here ".strip())
siteNameToMigratedPostTopic = None

with open("/scratch/parvezku01/MigrationStudy/serialize/migrated_post_topic.ser", "rb") as pickle_file:
    siteNameToMigratedPostTopic = pickle.load(pickle_file)
    for site_name in siteNameToMigratedPostTopic:
        for tag in siteNameToMigratedPostTopic[site_name]:
            print(set(convert_tag_to_list(tag)))

count = 0
with open("/scratch/parvezku01/MigrationStudy/serialize/migrated_post_dict.ser", "rb") as pickle_file:
    siteNameToMigratedPostDict = pickle.load(pickle_file)

    for site_name in siteNameToMigratedPostDict:
        postIdToPostDict = siteNameToMigratedPostDict[site_name]
        if site_name == "android.stackexchange.com":
            for (id, post) in postIdToPostDict.items():
                if post.get_postTypeId() == 1:

                    print("Id: " + str(post.get_id()) + " site: " + site_name)
                    soup_title = BeautifulSoup(post.get_title(), features="lxml")
                    soup_body = BeautifulSoup(post.get_body(), features="lxml")
                    print("Original Title.......")
                    print(post.get_body())
                    print("Title.......")
                    print(soup_body.get_text())
                    print("Keywords.......")
                    sentences = sent_tokenize(soup_body.get_text())

                    print(keywords.keywords(" \\ ".join(sentences),ratio=0.7,split=True))
                    print("......................")
                    count = count + 1

print("Count: "+str(count))

# postIdToPosition = None
# post_small = None
#
# with open("/scratch/parvezku01/MigrationStudy/post_index/english.meta.stackexchange.com_position.ser", "rb") as pickle_file:
#     postIdToPosition = pickle.load(pickle_file)
#
# with open("/scratch/parvezku01/MigrationStudy/post_index/english.meta.stackexchange.com.ser", "rb") as post_small_file:
#     print(post_small_file.tell())
#     post = pickle.load(file=post_small_file)
#     post.print_post()
#     print(post.get_site())
#
#     print(post_small_file.tell())
#     post = pickle.load(file=post_small_file)
#     post.print_post()
#     print(post.get_site())
#
#     print(post_small_file.tell())
#     post = pickle.load(file=post_small_file)
#     post.print_post()
#     print(post.get_site())
#
#     for id,position in postIdToPosition.items():
#         print("Id: "+str(id)+" Position: "+str(position))
#         post_small_file.seek(position)
#         post = pickle.load(file=post_small_file)
#         post.print_post()
#
#
#
#
#
