class Tag:
    SITE = "Site"
    ID = "Id"
    TAG_NAME = "TagName"
    COUNT = "Count"
    EXCERPT_POST_ID = "ExcerptPostId"
    WIKI_POST_ID = "WikiPostId"

    # Initializer / Instance Attributes
    def __init__(self):
        self.site = None
        self.id = -999
        self.tagName = None
        self.count = -999
        self.excerptPostId = -999
        self.wikiPostId = -999

    def get_site(self):
        return self.site

    def set_site(self, _site):
        self.site = _site

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = _id

    def get_tagName(self):
        return self.tagName

    def set_tagName(self, _tagName):
        self.tagName = _tagName

    def get_count(self):
        return self.count

    def set_count(self, _count):
        self.count = _count

    def get_excerptPostId(self):
        return self.excerptPostId

    def set_excerptPostId(self, _excerptPostId):
        self.excerptPostId = _excerptPostId

    def get_wikiPostId(self):
        return self.wikiPostId

    def set_wikiPostId (self, _wikiPostId):
        self.wikiPostId = _wikiPostId
    
    def print_tag(self):
        print("Tag Id: "+str(self.id)+" TagName: "+str(self.tagName)+" Count: "+str(self.count)+" ExcerptPostId: "+str(self.excerptPostId)
            + " WikiPostId: "+str(self.wikiPostId))