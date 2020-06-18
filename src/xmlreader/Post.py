class Post:
    SITE = "Site"
    ID = "Id"
    POST_TYPE_ID = "PostTypeId"
    ACCEPTED_ANSWER_ID = "AcceptedAnswerId"
    PARENT_ID = "ParentId"
    CREATION_DATE = "CreationDate"
    DELETION_DATE = "DeletionDate"
    SCORE = "Score"
    VIEW_COUNT = "ViewCount"
    BODY = "Body"
    OWNER_USER_ID = "OwnerUserId"
    OWNER_DISPLAY_NAME = "OwnerDisplayName"
    LAST_EDITOR_USER_ID = "LastEditorUserId"
    LAST_EDITOR_DISPLAY_NAME = "LastEditorDisplayName"
    LAST_EDIT_DATE = "LastEditDate"
    LAST_ACTIVITY_DATE = "LastActivityDate"
    TITLE = "Title"
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
        self.deletionDate = None
        self.score = 0
        self.viewCount = 0
        self.body = None
        self.ownerUserId = -999
        self.ownerDisplayName = None
        self.lastEditorUserId = -999
        self.lastEditorDisplayName = None
        self.lastEditDate = None
        self.lastActivityDate = None
        self.title = None
        self.tags = None
        self.answerCount = 0
        self.commentCount = 0
        self.favoriteCount = 0
        self.closedDate = None
        self.communityOwnedDate = None

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

    def get_deletionDate(self):
        return self.deletionDate

    def set_deletionDate(self, _deletionDate):
        self.deletionDate = _deletionDate

    def get_score(self):
        return self.score

    def set_score(self, _score):
        self.score = _score

    def get_viewCount(self):
        return self.viewCount

    def set_viewCount(self, _viewCount):
        self.viewCount = _viewCount

    def get_body(self):
        return self.body

    def set_body(self, _body):
        self.body = _body

    def get_ownerUserId(self):
        return self.ownerUserId

    def set_ownerUserId(self, _ownerUserId):
        self.ownerUserId = _ownerUserId

    def get_ownerDisplayName(self):
        return self.ownerDisplayName

    def set_ownerDisplayName(self, _ownerDisplayName):
        self.ownerDisplayName = _ownerDisplayName

    def get_lastEditorUserId(self):
        return self.lastEditorUserId

    def set_lastEditorUserId(self, _lastEditorUserId):
        self.lastEditorUserId = _lastEditorUserId

    def get_lastEditorDisplayName(self):
        return self.lastEditorDisplayName

    def set_lastEditorDisplayName(self, _lastEditorDisplayName):
        self.lastEditorDisplayName = _lastEditorDisplayName

    def get_lastEditDate(self):
        return self.lastEditDate

    def set_lastEditDate(self, _lastEditDate):
        self.lastEditDate = _lastEditDate

    def get_lastActivityDate(self):
        return self.lastActivityDate

    def set_lastActivityDate(self, _lastActivityDate):
        self.lastActivityDate = _lastActivityDate

    def get_title(self):
        return self.title

    def set_title(self, _title):
        self.title = _title

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

    def set_closedDate(self, _closedDate):
        self.closedDate = _closedDate

    def get_closedDate(self):
        return self.closedDate

    def get_communityOwnedDate(self):
        return self.communityOwnedDate

    def set_communityOwnedDate(self, _communityOwnedDate):
        self.communityOwnedDate = _communityOwnedDate
    
    def print_post(self):
        print("Id: "+str(self.id)+" PostTypeId: "+str(self.postTypeId)+" AcceptedAnswerId: "+str(self.acceptedAnswerId)
            + " ParentId: "+str(self.parentId) +" CreationDate: "+str(self.creationDate)+" DeletionDate: "+str(self.deletionDate)
            + " Score: "+str(self.score)+" ViewCount: "+str(self.viewCount) +" Body: "+str(self.BODY)
            +" OwnerUserId: "+str(self.ownerUserId)+" OwnerDisplayName: " + str(self.ownerDisplayName)
            +" LastEditorUserId: "+str(self.lastEditorUserId)+" LastEditorDisplayName: "+str(self.lastEditorDisplayName)
            +" LastEditDate: "+str(self.lastEditDate)+" LastActivityDate: "+str(self.lastActivityDate)
            +" Title: "+str(self.title)+" Tags: "+str(self.tags)+" AnswerCount: "+str(self.answerCount)
            +" CommentCount: "+str(self.commentCount)+" FavoriteCount: "+str(self.favoriteCount)
            +" ClosedDate: "+str(self.closedDate)+ " CommunityOwnedDate: "+str(self.communityOwnedDate))