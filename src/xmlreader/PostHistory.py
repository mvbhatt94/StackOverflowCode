class PostHistory:
    SITE = "Site"
    ID = "Id"
    POST_HISTORY_TYPE_ID = "PostHistoryTypeId"
    POST_ID = "PostId"
    REVISION_GUID = "RevisionGUID"
    CREATION_DATE = "CreationDate"
    USER_ID = "UserId"
    USER_DISPLAY_NAME = "UserDisplayName"
    COMMENT = "Comment"
    TEXT = "Text"
    ORIGIN = "Origin"
    ORIGIN_ID = "OriginId"
    DESTINATION = "Destination"
    DESTINATION_ID = "DestinationId"

    # Initializer / Instance Attributes
    def __init__(self):
        self.site = None
        self.id = -999
        self.postHistoryTypeId = -999
        self.postId = -999
        self.revisionGUID = None
        self.creationDate = None
        self.userId = -999
        self.userDisplayName = None
        self.comment = None
        self.text = None
        self.origin = None
        self.originId = -999
        self.destination = None
        self.destinationId = -999

    def get_site(self):
        return self.site

    def set_site(self, _site):
        self.site = _site

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = _id

    def get_postHistoryTypeId(self):
        return self.postHistoryTypeId

    def set_postHistoryTypeId(self, _postHistoryTypeId):
        self.postHistoryTypeId = _postHistoryTypeId

    def get_postId(self):
        return self.postId

    def set_postId(self, _postId):
        self.postId = _postId

    def get_revisionGUID(self):
        return self.revisionGUID

    def set_revisionGUID(self, _revisionGUID):
        self.revisionGUID = _revisionGUID

    def get_creationDate(self):
        return self.creationDate

    def set_creationDate(self, _creationDate):
        self.creationDate = _creationDate

    def get_userId(self):
        return self.userId

    def set_userId(self, _userId):
        self.userId = _userId

    def get_userDisplayName(self):
        return self.userDisplayName

    def set_userDisplayName(self, _userDisplayName):
        self.userDisplayName = _userDisplayName

    def get_comment(self):
        return self.comment

    def set_comment(self, _comment):
        self.comment = _comment

    def get_text(self):
        return self.text

    def set_text(self, _text):
        self.text = _text

    def get_origin(self):
        return self.origin

    def set_origin(self, _origin):
        self.origin = _origin

    def get_originId(self):
        return self.originId

    def set_originId(self, _originId):
        self.originId = _originId

    def get_destination(self):
        return self.destination

    def set_destination(self, _destination):
        self.destination =_destination

    def get_destinationId(self):
        return self.destinationId

    def set_destinationId(self, _destinationId):
        self.destinationId = _destinationId
    def print_postHistory(self):
        print("Site: "+str(self.site)+" Post History Id: "+str(self.id)+" PostHistoryTypeId: "+str(self.postHistoryTypeId)+" PostId: "+str(self.postId)
            +" RevisionGUID: "+str(self.revisionGUID)+" CreationDate: "+str(self.creationDate)+" UserId: "
            +str(self.userId)+" UserDisplayName: "+str(self.userDisplayName)+ " Comment: "+str(self.comment)+" Text: "+str(self.text)+
              " Destination: "+str(self.destination)+" DestinationId: "+str(self.destinationId)+" Origin: "+str(self.origin)+" OriginId: "+str(self.originId))