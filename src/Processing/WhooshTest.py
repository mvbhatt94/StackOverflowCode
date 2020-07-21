from whoosh.analysis import RegexTokenizer
from whoosh.analysis import LowercaseFilter
from whoosh.index import create_in, open_dir
from whoosh.fields import *

import time
start_time = time.time()
#schema = Schema(title=TEXT(stored=True), id=NUMERIC(stored=True), content=TEXT(stored=True))
schema = Schema(title=TEXT(analyzer=RegexTokenizer() | LowercaseFilter(), stored=True), id=TEXT(stored=True), content=TEXT(analyzer=RegexTokenizer() | LowercaseFilter(), stored=True,))

# ix = create_in("/home/parvez/Desktop/index_dir", schema)
# #ix = open_dir("/Users/parvez/Desktop/indexdir")
#
# writer = ix.writer(limitmb=256,procs=2,multisegment = True)
# t1="First document"
# t2="This is the first document we've added!"
# for i in range(0,5):
#  if i%100000==0:
#   print("progress: "+str(i))
#  writer.add_document(title=t1, id=i,content=t2)
#  #writer.add_document(title="Second document", path=u"/b",content=u"first document ")
# writer.commit()
# writer = ix.writer()
# for i in range(5,10):
# if i%100000==0:
# print("progress: "+str(i))
# writer.add_document(title="First document", id=i,content=u"This is the first document we've added!")
# #writer.add_document(title="Second document", path=u"/b",content=u"first document ")
# writer.commit()


ix = open_dir("/media/parvez/IntelSSD/MigrationRecommender/whoosh_index_basic/astronomy.meta.stackexchange.com")
from whoosh import qparser

with ix.searcher() as searcher:
 query = qparser.QueryParser("title", ix.schema, group=qparser.OrGroup).parse("Where do we draw the line concerning planetary science questions?")
 results = searcher.search(query, limit=100)
 print(len(results))
 for result in results:
  print(result)
print("--- %s seconds ---" % (time.time() - start_time))
