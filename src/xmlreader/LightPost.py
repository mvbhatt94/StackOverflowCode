class LightPost:
    SITE = "Site"
    ID = "Id"
    POST_TYPE_ID = "PostTypeId"
    ACCEPTED_ANSWER_ID = "AcceptedAnswerId"
    PARENT_ID = "ParentId"
    CREATION_DATE = "CreationDate"
    SCORE = "Score"
    VIEW_COUNT = "ViewCount"
    OWNER_USER_ID = "OwnerUserId"
    TAGS = "Tags"
    ANSWER_COUNT = "AnswerCount"
    COMMENT_COUNT = "CommentCount"
    FAVORITE_COUNT = "FavoriteCount"
    CLOSED_DATE = "ClosedDate"
    COMMUNITY_OWNED_DATE = "CommunityOwnedDate"

    # Initializer / Instance Attributes
    def __init__(self):
        self.site = None
        self.id = -999
        self.postTypeId = -999
        self.acceptedAnswerId = -999
        self.parentId = -999
        self.creationDate = None
        self.score = 0
        self.viewCount = 0
        self.ownerUserId = -999
        self.tags = None
        self.answerCount = 0
        self.commentCount = 0
        self.favoriteCount = 0
        self.closedDate = None

    def get_site(self):
        return self.site

    def set_site(self, _site):
        self.site = _site

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = _id

    def get_postTypeId(self):
        return self.postTypeId

    def set_postTypeId(self, _postTypeId):
        self.postTypeId = _postTypeId

    def get_acceptedAnswerId(self):
        return self.acceptedAnswerId

    def set_acceptedAnswerId(self, _acceptedAnswerId):
        self.acceptedAnswerId = _acceptedAnswerId

    def get_parentId(self):
        return self.parentId

    def set_parentId(self, _parentId):
        self.parentId = _parentId

    def get_creationDate(self):
        return self.creationDate

    def set_creationDate(self, _creationDate):
        self.creationDate = _creationDate

    def get_score(self):
        return self.score

    def set_score(self, _score):
        self.score = _score

    def get_viewCount(self):
        return self.viewCount

    def set_viewCount(self, _viewCount):
        self.viewCount = _viewCount

    def get_ownerUserId(self):
        return self.ownerUserId

    def set_ownerUserId(self, _ownerUserId):
        self.ownerUserId = _ownerUserId

    def get_tags(self):
        return self.tags

    def set_tags(self, _tags):
        self.tags = _tags

    def get_answerCount(self):
        return self.answerCount

    def set_answerCount(self, _answerCount):
        self.answerCount = _answerCount

    def get_commentCount(self):
        return self.commentCount

    def set_commentCount(self, _commentCount):
        self.commentCount = _commentCount

    def get_favoriteCount(self):
        return self.favoriteCount

    def set_favoriteCount(self, _favoriteCount):
        self.favoriteCount = _favoriteCount

    def get_closedDate(self):
        return self.closedDate
    
    def set_closedDate(self, _closedDate):
        self.closedDate = _closedDate
        return self.closedDate

    def get_communituOwnedDate(self):
        return self.communituOwnedDate
    
    def set_communityOwnedDate(self, _communityOwnedDate):
        self.communituOwnedDate = _communityOwnedDate;
    
    def print_post(self):
        print("Id: "+str(self.id)+" PostTypeId: "+str(self.postTypeId)+" AcceptedAnswerId: "+str(self.acceptedAnswerId)
            + " ParentId: "+str(self.parentId) +" CreationDate: "+str(self.creationDate)+ " Score: "+str(self.score)+" ViewCount: "+str(self.viewCount)
            +" OwnerUserId: "+str(self.ownerUserId) +" Tags: "+str(self.tags)+" AnswerCount: "+str(self.answerCount)
            +" CommentCount: "+str(self.commentCount)+" FavoriteCount: "+str(self.favoriteCount) +" ClosedDate: "+str(self.closedDate)+" CommuniOwnedDate: "+str(self.communituOwnedDate))