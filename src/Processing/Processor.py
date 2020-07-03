from lxml import etree
import time
import pickle
import sys
import os
from Utility.SiteManager import SiteManager
from xmlreader.DataConverter import DataConverter
import numpy as np
import pandas as pd

STACK_EXCHANGE_DATA = "/home/local/SAIL/parvezku01/Research/MigrationStudy/stackexchange_datadump"
list_subfolders_with_paths = [(f.path,f.name) for f in os.scandir(STACK_EXCHANGE_DATA) if f.is_dir() and f.name.startswith(".") is False]
for path in list_subfolders_with_paths:
    print(path)
site_manager = SiteManager("/home/local/SAIL/parvezku01/Research/MigrationStudy/data/sites_category.csv")


def create_user_dict():
    # load the user data
    start_time = time.time()
    siteToUserData = {}
    site_count = 0
    for (path, name) in list_subfolders_with_paths:
        count = 0
        userIdToUserDict = {}
        for event, elem in etree.iterparse(path + "/Users.xml", events=("start", "end", "start-ns", "end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if (count % 1000000 == 0):
                    print("Progress of reading users: " + str(count))
                lu = DataConverter.readLightUser(elem)
                userIdToUserDict[lu.get_id()] = lu
        siteToUserData[name] = userIdToUserDict
        print("Completed: " + str(site_count) + "/" + str(len(list_subfolders_with_paths)))
        site_count = site_count + 1

    print('Now serialize user data...')
    with open("/home/local/SAIL/parvezku01/Research/MigrationStudy/serialize/user_dict.ser", "wb") as serializeFile:
        pickle.dump(obj=siteToUserData, file=serializeFile)
    print("--- %s seconds ---" % (time.time() - start_time))

def create_user_csv():
    start_time = time.time()
    columns = ['site_id', 'id', 'reputation', 'creation_date', 'display_name', 'views', 'upvotes', 'downvotes',
               'account_id']
    data_list = [[], [], [], [], [], [], [], [], []]
    start_time = time.time()
    count = 0
    dataframe = pd.DataFrame(columns=columns)
    for (path, name) in list_subfolders_with_paths:
        for event, elem in etree.iterparse(path+"/Users.xml", events=("start", "end", "start-ns", "end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if (count % 1000000 == 0):
                    print("Progress of reading users: " + str(count))
                user = DataConverter.readUser(elem)
                site_id = site_manager.nameToIdDict[name]
                data_list[0].append(site_id)
                data_list[1].append(user.get_id())
                data_list[2].append(user.get_reputation())
                data_list[3].append(user.get_creationDate())
                data_list[4].append(user.get_displayName())
                data_list[5].append(user.get_views())
                data_list[6].append(user.get_upVotes())
                data_list[7].append(user.get_downVotes())
                data_list[8].append(user.get_accountId())

    df_user = pd.DataFrame(
        {columns[0]: data_list[0], columns[1]: data_list[1], columns[2]: data_list[2], columns[3]: data_list[3],
         columns[4]: data_list[4],
         columns[5]: data_list[5], columns[6]: data_list[6], columns[7]: data_list[7], columns[8]: data_list[8]})
    df_user.to_csv('/home/local/SAIL/parvezku01/Research/MigrationStudy/serialize/users.csv')
    print("Time required to read users: " + str(time.time() - start_time))

def create_vote_csv():
    columns = ['site_id', 'id', 'post_id', 'vote_type_id', 'user_id', 'creation_date', 'bounty_amount']
    data_list = [[], [], [], [], [], [],[]]
    start_time = time.time()
    count = 0
    for (path, name) in list_subfolders_with_paths:
        for event, elem in etree.iterparse(path + "/Votes.xml", events=("start", "end", "start-ns", "end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if (count % 1000000 == 0):
                    print("Progress of reading votes: " + str(count))
                vote = DataConverter.readVote(elem)
                site_id = site_manager.nameToIdDict[name]
                data_list[0].append(site_id)
                data_list[1].append(vote.get_id())
                data_list[2].append(vote.get_postId())
                data_list[3].append(vote.get_voteTypeId())
                data_list[4].append(vote.get_userId())
                data_list[5].append(vote.get_creationDate())
                data_list[6].append(vote.get_bountyAmount())
    df_vote = pd.DataFrame(
        {columns[0]: data_list[0], columns[1]: data_list[1], columns[2]: data_list[2], columns[3]: data_list[3],
         columns[4]: data_list[4], columns[5]: data_list[5], columns[6]: data_list[6]})
    df_vote.to_csv('/home/local/SAIL/parvezku01/Research/MigrationStudy/serialize/votes.csv')

def create_migrate_post_history_dict():
    # load the post history data
    start_time = time.time()
    siteToMigratedPhDict = {}
    site_count = 0
    for (path, name) in list_subfolders_with_paths:
        count = 0
        phIdToPhDict = {}
        for event, elem in etree.iterparse(path + "/PostHistory.xml", events=("start", "end", "start-ns", "end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if (count % 1000000 == 0):
                    print("Progress of reading post histories: " + str(count))
                ph = DataConverter.readPostHistory(elem)
                ph.set_site(site_manager.getSiteName(name))

                if ph.get_postHistoryTypeId() == 35 and ph.get_destination() is not None:
                    site_name = site_manager.getSiteName(ph.get_destination())
                    ph.set_destination(site_name)
                    phIdToPhDict[ph.get_id()] = ph

                elif ph.get_postHistoryTypeId() == 36 and ph.get_origin() is not None:
                    site_name = site_manager.getSiteName(ph.get_origin())
                    ph.set_origin(site_name)
                    phIdToPhDict[ph.get_id()] = ph
        siteToMigratedPhDict[name] = phIdToPhDict
        print("Completed: " + str(site_count) + "/" + str(len(list_subfolders_with_paths)))
        site_count = site_count + 1
    with open("/home/local/SAIL/parvezku01/Research/MigrationStudy/serialize/migrate_post_history_dict.ser",
              "wb") as serializeFile:
        pickle.dump(obj=siteToMigratedPhDict, file=serializeFile)
    print("--- %s seconds ---" % (time.time() - start_time))

def create_migrate_post_history_csv():
    columns = ['site_id', 'id', 'ph_type_id', 'post_id', 'revision_guid', 'creation_date', 'user_id',
               'user_display_name', 'comment', 'text', 'destination', 'destination_post_id', 'origin', 'origin_post_id']
    data_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
    start_time = time.time()

    site_count = 0
    dataframe = pd.DataFrame(columns=columns)
    for (path, name) in list_subfolders_with_paths:
        count = 0
        print("Processsing site: " + name)
        for event, elem in etree.iterparse(path + "/PostHistory.xml", events=("start", "end", "start-ns", "end-ns")):
            if elem.tag == "row" and event == "start":
                count = count + 1
                if (count % 1000000 == 0):
                    print("Progress of reading post histories: " + str(count))
                postHistory = DataConverter.readPostHistory(elem)
                site_id = site_manager.nameToIdDict[name]
                if postHistory.get_postHistoryTypeId() == 35 or postHistory.get_postHistoryTypeId() == 36:
                    data_list[0].append(site_id)
                    data_list[1].append(postHistory.get_id())
                    data_list[2].append(postHistory.get_postHistoryTypeId())
                    data_list[3].append(postHistory.get_postId())
                    data_list[4].append(postHistory.get_revisionGUID())
                    data_list[5].append(postHistory.get_creationDate())
                    data_list[6].append(postHistory.get_userId())
                    data_list[7].append(postHistory.get_userDisplayName())
                    data_list[8].append(postHistory.get_comment())
                    data_list[9].append(postHistory.get_text())
                    data_list[10].append(postHistory.get_destination())
                    data_list[11].append(postHistory.get_destinationId())
                    data_list[12].append(postHistory.get_origin())
                    data_list[13].append(postHistory.get_originId())
        print("Completed: " + str(site_count) + "/" + str(len(list_subfolders_with_paths)))
        site_count = site_count + 1
    df_ph = pd.DataFrame(
        {columns[0]: data_list[0], columns[1]: data_list[1], columns[2]: data_list[2], columns[3]: data_list[3],
         columns[4]: data_list[4], columns[5]: data_list[5], columns[6]: data_list[6], columns[7]: data_list[7],
         columns[8]: data_list[8], columns[9]: data_list[9], columns[10]: data_list[10], columns[11]: data_list[11],
         columns[12]: data_list[12], columns[13]: data_list[13]})
    df_ph.to_csv('/home/local/SAIL/parvezku01/Research/MigrationStudy/serialize/migrate_post_history.csv')
    print("Time required to read post histories: " + str(time.time() - start_time))

#print("Step-1: Collect user dict...")
#create_user_dict()
#print("Step-2: Collect user csv...")
#create_user_csv()
#print("Step-3: Collect vote csv...")
#create_vote_csv()
#print("Step-4: Collect post history dict...")
#create_migrate_post_history_dict()
print("Step-5: Collect post history csv..")
create_migrate_post_history_csv()
