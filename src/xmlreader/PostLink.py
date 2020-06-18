class PostLink:
    SITE = "Site"
    ID = "Id"
    CREATION_DATE = "CreationDate"
    POST_ID = "PostId"
    RELATED_POST_ID = "RelatedPostId"
    LINK_TYPE_ID = "LinkTypeId"

    # Initializer / Instance Attributes
    def __init__(self):
        self.site = None
        self.id = -999
        self.creationDate = None
        self.postId = -999
        self.relatedPostId = -999
        self.linkTypeId = -999

    def get_site(self):
        return self.site

    def set_site(self, _site):
        self.site = _site

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = int(_id)

    def get_creationDate(self):
        return self.creationDate

    def set_creationDate(self, _creationDate):
        self.creationDate = _creationDate

    def get_postId(self):
        return self.postId

    def set_postId(self, _postId):
        self.postId = _postId

    def get_relatedPostId(self):
        return self.relatedPostId

    def set_relatedPostId (self, _relatedPostId):
        self.relatedPostId = _relatedPostId

    def get_linkTypeId(self):
        return self.linkTypeId

    def set_linkTypeId (self, _linkTypeId):
        self.linkTypeId = _linkTypeId
    
    def print_postLink(self):
        print("Post Link Id: "+str(self.id)+" CreationDate: "+str(self.creationDate)+" PostId: "+str(self.postId)+" RelatedPostId: "+str(self.relatedPostId)
           +" LinkTypeId: "+str(self.linkTypeId))