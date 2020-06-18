class Vote:
    SITE = "Site"
    ID = "Id"
    POST_ID = "PostId"
    VOTE_TYPE_ID = "VoteTypeId"
    USER_ID = "UserId"
    CREATION_DATE = "CreationDate"
    BOUNTY_AMOUNT = "BountyAmount"

    # Initializer / Instance Attributes
    def __init__(self):
        self.site = None
        self.id = -999
        self.postId = -999
        self.voteTypeId = -999
        self.userId = -999
        self.creationDate = None
        self.bountyAmount = 0

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

    def get_voteTypeId(self):
        return self.voteTypeId

    def set_voteTypeId(self, _voteTypeId):
        self.voteTypeId = _voteTypeId

    def get_userId(self):
        return self.userId

    def set_userId(self, _userId):
        self.userId = _userId

    def get_creationDate(self):
        return self.creationDate

    def set_creationDate(self, _creationDate):
        self.creationDate = _creationDate

    def get_bountyAmount(self):
        return self.bountyAmount

    def set_bountyAmount(self, _bountyAmount):
        self.bountyAmount = _bountyAmount
    
    def print_vote(self):
        print('Vote Id: '+str(self.id)+" PostId: "+str(self.postId)+" VoteTypeId: "+str(self.voteTypeId)+" UserId: "+str(self.userId) 
        + " CreationDate: "+str(self.creationDate) +" BountyAmount: "+str(self.bountyAmount))