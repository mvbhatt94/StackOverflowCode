class Comment:
    SITE = "Site"
    ID = "Id"
    POST_ID = "PostId"
    SCORE = "Score"
    TEXT = "Text"
    CREATION_DATE = "CreationDate"
    USER_ID = "UserId"
    USER_DIPLAY_NAME = "UserDisplayName"

    # Initializer / Instance Attributes
    def __init__(self):
        self.site = None
        self.id = -999
        self.postId = -999
        self.score = -999
        self.text = None
        self.creationDate = None
        self.userDisplayName = None
        self.userId = -999

    def get_site(self):
        return self.site

    def set_site(self, _site):
        self.site = _site

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = _id

    def get_postId(self):
        return self.postId

    def set_postId(self, _postId):
        self.postId = _postId

    def get_score(self):
        return self.score

    def set_score(self, _score):
        self.score = _score

    def get_text(self):
        return self.text

    def set_text(self, _text):
        self.text = _text

    def get_creationDate(self):
        return self.creationDate

    def set_creationDate(self, _creationDate):
        self.creationDate = _creationDate

    def get_userDisplayName(self):
        return self.userDisplayName

    def set_userDisplayName(self, _userDisplayName):
        self.userDisplayName = _userDisplayName

    def get_userId(self):
        return self.userId

    def set_userId(self, _userId):
        self.userId = _userId
    def print_comment(self):
        print("Comment Id: "+str(self.id)+" PostId: "+str(self.postId)+" Score: "+str(self.score)+" CreationDate: "+str(self.creationDate)+" Text: "+str(self.text) +" UserId: "+str(self.userId)+" UserDisplayName: "+str(self.userDisplayName))