class User:
    SITE = "Site"
    ID = "Id"
    REPUTATION = "Reputation"
    CREATION_DATE = "CreationDate"
    DISPLAY_NAME = "DisplayName"
    LAST_ACCESS_DATE = "LastAccessDate"
    WEBSITE_URL = "WebsiteUrl"
    LOCATION = "Location"
    ABOUT_ME = "AboutMe"
    VIEWS = "Views"
    UP_VOTES = "UpVotes"
    DOWN_VOTES = "DownVotes"
    PROFILE_IMAGE_URL = "ProfileImageUrl"
    ACCOUNT_ID = "AccountId"

    # Initializer / Instance Attributes
    def __init__(self):
        self.site = None
        self.id = -999
        self.reputation = 1
        self.creationDate = None
        self.displayName = None
        self.lastAccessDate = None
        self.websiteUrl = None
        self.location = None
        self.aboutMe = None
        self.views = 0
        self.upVotes = 0
        self.downVotes = 0
        self.profileImageUrl = None
        self.accountId = -999

    def get_site(self):
        return self.site

    def set_site(self, _site):
        self.site = _site

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = _id

    def get_reputation(self):
        return self.reputation

    def set_reputation(self, _reputation):
        self.reputation = _reputation

    def get_creationDate(self):
        return self.creationDate

    def set_creationDate(self, _creationDate):
        self.creationDate = _creationDate

    def get_displayName(self):
        return self.displayName

    def set_displayName(self, _displayName):
        self.displayName = _displayName

    def get_lastAccessDate(self):
        return self.lastAccessDate

    def set_lastAccessDate(self, _lastAccessDate):
        self.lastAccessDate = _lastAccessDate

    def get_websiteUrl(self):
        return self.websiteUrl

    def set_websiteUrl(self, _websiteUrl):
        self.websiteUrl = _websiteUrl

    def get_location(self):
        return self.location

    def set_location(self, _location):
        self.location = _location

    def get_aboutMe(self):
        return self.aboutMe

    def set_aboutMe(self, _aboutMe):
        self.aboutMe = _aboutMe

    def get_views(self):
        return self.views

    def set_views(self, _views):
        self.views = _views

    def get_upVotes(self):
        return self.upVotes

    def set_upVotes(self, _upVotes):
        self.upVotes = _upVotes

    def get_downVotes(self):
        return self.downVotes

    def set_downVotes(self, _downVotes):
        self.downVotes = _downVotes

    def get_profileImageUrl(self):
        return self.profileImageUrl

    def set_profileImageUrl(self, _profileImageUrl):
        self.profileImageUrl = _profileImageUrl

    def get_accountId(self):
        return self.accountId

    def set_accountId(self, _accountId):
        self.accountId = _accountId
    def print_user(self):
        print("User Id: "+str(self.id)+" Reputation: "+str(self.reputation) 
        + " Creation Date: "+str(self.creationDate) + " DisplayName: "+str(self.displayName)
        +" LastAccessDate:"+str(self.lastAccessDate)+" WebsiteUrl: "+str(self.websiteUrl)+" Location: "+str(self.location)
        + " About Me: "+str(self.aboutMe)+" Views: "+str(self.views)
        +" Upvotes: "+str(self.upVotes) + " Downvotes: "+str(self.downVotes) +" ProfileImageUrl: "+str(self.profileImageUrl) 
        + " Account Id: "+str(self.accountId))