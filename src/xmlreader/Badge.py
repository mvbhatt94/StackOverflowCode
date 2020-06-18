class Badge:
    SITE = "Site"
    ID = "Id"
    USER_ID = "UserId"
    NAME = "Name"
    DATE = "Date"
    BADGE_CLASS = "Class"
    TAG_BASED = "TagBased"

    # Initializer / Instance Attributes
    def __init__(self):
        self.site = None
        self.id = -999
        self.userId = -999
        self.name = None
        self.date = None
        self.badgeClass = None
        self.tagBased = None

    def get_site(self):
        return self.site

    def set_site(self, _site):
        self.site = _site

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = _id

    def get_userId(self):
        return self.userId

    def set_userId(self, _userId):
        self.userId = _userId

    def get_name(self):
        return self.name

    def set_name(self, _name):
        self.name = _name

    def get_date(self):
        return self.date

    def set_date(self, _date):
        self.date = _date

    def get_badgeClass(self):
        return self.badgeClass

    def set_badgeClass(self, _badgeClass):
        self.badgeClass = _badgeClass

    def get_tagBased(self):
        return self.tagBased

    def set_tagBased(self, _tagBased):
        self.tagBased = _tagBased
    
    def print_badge(self):
        print("Badge Id: "+str(self.id)+" UserId: "+str(self.userId)+" Name: "+str(self.name)+" Date: "+str(self.date)
            + " Class: "+str(self.badgeClass)+" TagBased: "+ str(self.tagBased))