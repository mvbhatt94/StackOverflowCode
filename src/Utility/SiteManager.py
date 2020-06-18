import csv

class SiteManager:
    nameToIdDict = {}
    idToNameDict = {}
    idToCategoryDict = {}
    def __init__(self, path):
        with open(path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(csv_reader)
            for row in csv_reader:
                self.nameToIdDict[row[0]] = int(row[1])
                self.idToNameDict[int(row[1])] = row[0]
                self.idToCategoryDict[int(row[1])] = row[2]

    def getSiteName(self,siteName):
        if siteName in self.nameToIdDict.keys():
            pass
        elif siteName.lower()=="programmers.stackexchange.com":
            siteName = "softwareengineering.stackexchange.com"
        elif siteName.lower()=="meta.programmers.stackexchange.com":
            siteName = "softwareengineering.meta.stackexchange.com"

        elif siteName.lower()=="alcohol.stackexchange.com":
            siteName = "beer.stackexchange.com"

        elif siteName.lower()=="nothingtoinstall.com":
            siteName = "webapps.stackexchange.com"
        elif siteName.lower()=="ubuntu.stackexchange.com":
            siteName = "askubuntu.com"
        elif siteName.lower()=="writing.stackexchange.com":
            sitename = "writers.stackexchange.com"
        elif siteName.lower()=="video.stackexchange.com":
            siteName = "avp.stackexchange.com"
        elif siteName.lower()=="ui.stackexchange.com":
            siteName = "ux.stackexchange.com"
        elif siteName.lower()=="psychology.stackexchange.com":
            siteName = "cogsci.stackexchange.com"
        elif siteName.lower()=="facebook.stackoverflow.com":
            siteName = "stackoverflow.com"

        elif siteName.lower().startswith("meta."):
            # in some cases I found that meta.dba.stackexchange.com changed to dba.meta.stackexchange.com
            start_index = len("meta.")
            end_index   = start_index + siteName[start_index:].index('.')
            alternate_name = siteName[start_index:end_index]+".meta"+siteName[end_index:]
            if(alternate_name.lower() in self.nameToIdDict.keys()):
                siteName = alternate_name
            else:
                raise Exception("Cannot find the site name " + alternate_name)
        else:
            raise Exception("Cannot find the site name "+siteName)
        return siteName

site_manager = SiteManager("/media/parvez/SamsungOneTB/MigrationRecom/data/sites_category.csv")
print(site_manager.getSiteName("stackoverflow.com"))
print(site_manager.getSiteName("psychology.stackexchange.com"))
print(site_manager.getSiteName("meta.dba.stackexchange.com"))