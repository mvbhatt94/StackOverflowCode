from xmlreader.LightUser import LightUser
from xmlreader.User import User
from xmlreader.PostHistory import PostHistory
from xmlreader.Vote import Vote
from xmlreader.Comment import Comment
from xmlreader.Post import Post
from xmlreader.LightPost import LightPost
from xmlreader.PostLink import PostLink
from xmlreader.Badge import Badge
from xmlreader.Tag import Tag
from Utility.SiteManager import SiteManager

class DataConverter:
    def __init__(self):
        pass
    @staticmethod
    def readUser(elem):
        user = User()
        id = int(elem.get(User.ID))
        reputation = int(elem.get(User.REPUTATION))
        creationDate = elem.get(User.CREATION_DATE)
        displayName = elem.get(User.DISPLAY_NAME)
        lastAccessDate = elem.get(User.LAST_ACCESS_DATE)
        websiteUrl = elem.get(User.WEBSITE_URL)
        location = elem.get(User.LOCATION)
        aboutMe = elem.get(User.ABOUT_ME)
        views = 0 if (elem.get(User.VIEWS) is None) else int(elem.get(User.VIEWS))
        upVotes = 0 if (elem.get(User.UP_VOTES) is None) else int(elem.get(User.UP_VOTES))
        downVotes = 0 if (elem.get(User.DOWN_VOTES) is None) else int(elem.get(User.DOWN_VOTES))
        profileImageUrl = elem.get(User.PROFILE_IMAGE_URL)
        accountId = -999 if (elem.get(User.ACCOUNT_ID) is None) else int(elem.get(User.ACCOUNT_ID))

        user.set_id(id)
        user.set_reputation(reputation)
        user.set_creationDate(creationDate)
        user.set_displayName(displayName)
        user.set_lastAccessDate(lastAccessDate)
        user.set_websiteUrl(websiteUrl)
        user.set_location(location)
        user.set_aboutMe(aboutMe)
        user.set_views(views)
        user.set_upVotes(upVotes)
        user.set_downVotes(downVotes)
        user.set_profileImageUrl(profileImageUrl)
        user.set_accountId(accountId)
        return user
    @staticmethod
    def readLightUser(elem):
        lightUser = LightUser()

        id = int(elem.get(LightUser.ID))
        reputation = int(elem.get(LightUser.REPUTATION))
        creationDate = elem.get(LightUser.CREATION_DATE)
        displayName = elem.get(LightUser.DISPLAY_NAME)
        views = 0 if (elem.get(LightUser.VIEWS) is None) else int(elem.get(LightUser.VIEWS))
        upVotes = 0 if (elem.get(LightUser.UP_VOTES) is None) else int(elem.get(LightUser.UP_VOTES))
        downVotes = 0 if (elem.get(LightUser.DOWN_VOTES) is None) else int(elem.get(LightUser.DOWN_VOTES))
        accountId = -999 if (elem.get(LightUser.ACCOUNT_ID) is None) else int(elem.get(LightUser.ACCOUNT_ID))

        lightUser.set_id(id)
        lightUser.set_reputation(reputation)
        lightUser.set_creationDate(creationDate)
        lightUser.set_displayName(displayName)
        lightUser.set_views(views)
        lightUser.set_upVotes(upVotes)
        lightUser.set_downVotes(downVotes)
        lightUser.set_accountId(accountId)
        return lightUser
    
    @staticmethod
    def readPost(elem):
        post = Post()
        id = int(elem.get(Post.ID))
        postTypeId = int(elem.get(Post.POST_TYPE_ID))
        acceptedAnswerId = -999 if(elem.get(Post.ACCEPTED_ANSWER_ID) is None) else int(elem.get(Post.ACCEPTED_ANSWER_ID))
        parentId = -999 if (elem.get(Post.PARENT_ID) is None) else int(elem.get(Post.PARENT_ID))
        creationDate = elem.get(Post.CREATION_DATE)
        deletionDate = elem.get(Post.DELETION_DATE)
        score = 0 if(elem.get(Post.SCORE) is None) else int(elem.get(Post.SCORE))
        viewCount = 0 if (elem.get(Post.VIEW_COUNT) is None) else int(elem.get(Post.VIEW_COUNT))
        body = elem.get(Post.BODY)
        ownerUserId = -999 if (elem.get(Post.OWNER_USER_ID) is None) else int(elem.get(Post.OWNER_USER_ID))
        ownerDisplayName =elem.get(Post.OWNER_DISPLAY_NAME)
        lastEditorUserId = -999 if (elem.get(Post.LAST_EDITOR_USER_ID) is None) else elem.get(Post.LAST_EDITOR_USER_ID)
        lastEditorDisplayName = elem.get(Post.LAST_EDITOR_DISPLAY_NAME)
        lastEditDate = elem.get(Post.LAST_EDIT_DATE)
        lastActivityDate =elem.get(Post.LAST_ACTIVITY_DATE)
        title = elem.get(Post.TITLE)
        tags = elem.get(Post.TAGS)
        answerCount = 0 if (elem.get(Post.ANSWER_COUNT) is None) else int(elem.get(Post.ANSWER_COUNT))
        commentCount = 0 if (elem.get(Post.COMMENT_COUNT) is None) else int(elem.get(Post.COMMENT_COUNT))
        favoriteCount = 0 if (elem.get(Post.FAVORITE_COUNT) is None) else int(elem.get(Post.FAVORITE_COUNT))
        closedDate = elem.get(Post.CLOSED_DATE)
        communityOwnedDate = elem.get(Post.COMMUNITY_OWNED_DATE)  

        post.set_id(id)
        post.set_postTypeId(postTypeId)
        post.set_acceptedAnswerId(acceptedAnswerId)
        post.set_parentId(parentId)
        post.set_creationDate(creationDate)
        post.set_deletionDate(deletionDate)
        post.set_score(score)
        post.set_viewCount(viewCount)
        post.set_body(body)
        post.set_ownerUserId(ownerUserId)
        post.set_ownerDisplayName(ownerDisplayName)
        post.set_lastEditorUserId(lastEditorUserId)
        post.set_lastEditorDisplayName(lastEditorDisplayName)
        post.set_lastEditDate(lastEditDate)
        post.set_lastActivityDate(lastActivityDate)
        post.set_title(title)
        post.set_tags(tags)
        post.set_answerCount(answerCount)
        post.set_commentCount(commentCount)
        post.set_favoriteCount(favoriteCount)
        post.set_closedDate(closedDate)
        post.set_communityOwnedDate(communityOwnedDate) 
        return post  
       
    @staticmethod
    def readLightPost(elem):
        lightPost = LightPost()

        id = int(elem.get(LightPost.ID))
        postTypeId = int(elem.get(LightPost.POST_TYPE_ID))
        acceptedAnswerId = -999 if(elem.get(LightPost.ACCEPTED_ANSWER_ID) is None) else int(elem.get(LightPost.ACCEPTED_ANSWER_ID))
        parentId = -999 if (elem.get(LightPost.PARENT_ID) is None) else int(elem.get(LightPost.PARENT_ID))
        creationDate = elem.get(LightPost.CREATION_DATE)
        score = 0 if(elem.get(Post.SCORE) is None) else int(elem.get(Post.SCORE))
        viewCount = 0 if (elem.get(Post.VIEW_COUNT) is None) else int(elem.get(Post.VIEW_COUNT))
        ownerUserId = -999 if (elem.get(Post.OWNER_USER_ID) is None) else int(elem.get(Post.OWNER_USER_ID))
        tags = elem.get(LightPost.TAGS)
        answerCount = 0 if (elem.get(LightPost.ANSWER_COUNT) is None) else int(elem.get(LightPost.ANSWER_COUNT))
        commentCount = 0 if (elem.get(LightPost.COMMENT_COUNT) is None) else int(elem.get(LightPost.COMMENT_COUNT))
        favoriteCount = 0 if (elem.get(LightPost.FAVORITE_COUNT) is None) else int(elem.get(LightPost.FAVORITE_COUNT))
        closedDate = elem.get(LightPost.CLOSED_DATE)
        communityOwnedDate = elem.get(LightPost.COMMUNITY_OWNED_DATE)  
      
        lightPost.set_id(id)
        lightPost.set_postTypeId(postTypeId)
        lightPost.set_acceptedAnswerId(acceptedAnswerId)
        lightPost.set_parentId(parentId)
        lightPost.set_creationDate(creationDate)
        lightPost.set_score(score)
        lightPost.set_viewCount(viewCount)
        lightPost.set_ownerUserId(ownerUserId)
        lightPost.set_tags(tags)
        lightPost.set_answerCount(answerCount)
        lightPost.set_commentCount(commentCount)
        lightPost.set_favoriteCount(favoriteCount)
        lightPost.set_closedDate(closedDate)
        lightPost.set_communityOwnedDate(communityOwnedDate)    
        return lightPost
    
    @staticmethod
    def readVote(elem):
        vote = Vote()
        id = int(elem.get(Vote.ID))
        postId = int(elem.get(Vote.POST_ID))
        voteTypeId = int(elem.get(Vote.VOTE_TYPE_ID))
        userId = -999 if (elem.get(Vote.USER_ID) is None) else int(elem.get(Vote.USER_ID))
        creationDate = elem.get(Vote.CREATION_DATE)
        bountyAmount = -999 if (elem.get(Vote.BOUNTY_AMOUNT) is None) else int(elem.get(Vote.BOUNTY_AMOUNT))

        vote.set_id(id)
        vote.set_postId(postId)
        vote.set_voteTypeId(voteTypeId)
        vote.set_userId(userId)
        vote.set_creationDate(creationDate)
        vote.set_bountyAmount(bountyAmount)
        return vote
    
    @staticmethod
    def readComment(elem):
        comment = Comment()
        id = int(elem.get(Comment.ID))
        postId = int(elem.get(Comment.POST_ID))
        score = 0 if(elem.get(Comment.SCORE) is None) else int(elem.get(Comment.SCORE))
        text = elem.get(Comment.TEXT)
        creationDate = elem.get(Comment.CREATION_DATE)
        userId = -999 if(elem.get(Comment.USER_ID) is None) else int(elem.get(Comment.USER_ID))
        userDisplayName = elem.get(Comment.USER_DIPLAY_NAME)

        comment.set_id(id)
        comment.set_postId(postId)
        comment.set_score(score)
        comment.set_text(text)
        comment.set_creationDate(creationDate)
        comment.set_userDisplayName(userDisplayName)
        comment.set_userId(userId)
        return comment
    
    @staticmethod
    def readPostHistory(elem, site_manager):

        postHistory = PostHistory()

        id = int(elem.get(PostHistory.ID))
        postHistoryTypeId = int(elem.get(PostHistory.POST_HISTORY_TYPE_ID))
        postId = -999 if (elem.get(PostHistory.POST_ID) is None) else int(elem.get(PostHistory.POST_ID))
        revisionGUID = elem.get(PostHistory.REVISION_GUID)
        creationDate = elem.get(PostHistory.CREATION_DATE)
        userId = -999 if (elem.get(PostHistory.USER_ID) is None) else int(elem.get(PostHistory.USER_ID))
        userDisplayName = elem.get(PostHistory.USER_DISPLAY_NAME)
        comment = elem.get(PostHistory.COMMENT)
        text = elem.get(PostHistory.TEXT)

        postHistory.set_id(id)
        postHistory.set_postHistoryTypeId(postHistoryTypeId)
        postHistory.set_postId(postId)
        postHistory.set_revisionGUID(revisionGUID)
        postHistory.set_creationDate(creationDate)
        postHistory.set_userId(userId)
        postHistory.set_userDisplayName(userDisplayName)
        postHistory.set_comment(comment)
        postHistory.set_text(text)
        if postHistoryTypeId==35 or postHistoryTypeId==36:
            try:
                if postHistory.comment is not None and (comment.startswith("from https://") or comment.startswith("from http://")):
                    site, post_id = DataConverter.get_migrate_data(postHistory.get_comment())
                    site_name = site_manager.getSiteName(site)
                    postHistory.set_origin(site_name)
                    postHistory.set_originId(post_id)

                elif postHistory.get_comment() is not None and (
                        comment.startswith("to https://") or comment.startswith("to http://")):
                    site, post_id = DataConverter.get_migrate_data(postHistory.get_comment())
                    site_name = site_manager.getSiteName(site)
                    postHistory.set_destination(site_name)
                    postHistory.set_destinationId(post_id)
            except Exception:
                print("Exception occur in "+comment)

        return postHistory
    
    @staticmethod
    def readTag(elem):
        tag = Tag()
        id = int(elem.get(Tag.ID))
        tagName = elem.get(Tag.TAG_NAME)
        count = int(elem.get(Tag.COUNT))
        excerptPostId = elem.get(Tag.EXCERPT_POST_ID)
        wikiPostId = elem.get(Tag.WIKI_POST_ID)

        tag.set_id(id)
        tag.set_tagName(tagName)
        tag.set_count(count)
        tag.set_excerptPostId(excerptPostId)
        tag.set_wikiPostId(wikiPostId)
        return tag
    
    @staticmethod
    def readPostLink(elem):
        postLink = PostLink()

        id = int(elem.get(PostLink.ID))
        linkTypeId = int(elem.get(PostLink.LINK_TYPE_ID))
        creationDate = elem.get(PostLink.CREATION_DATE)
        postId = int(elem.get(PostLink.POST_ID))
        relatedPostId = int(elem.get(PostLink.RELATED_POST_ID))

        postLink.set_id(id)
        postLink.set_linkTypeId(linkTypeId)
        postLink.set_creationDate(creationDate)
        postLink.set_postId(postId)
        postLink.set_relatedPostId(relatedPostId)
        return postLink
    @staticmethod
    def readBadge(elem):
        badge = Badge()
        id = int(elem.get(Badge.ID))
        date = elem.get(Badge.DATE)
        userId = -999 if (elem.get(Badge.USER_ID) is None) else int(elem.get(Badge.USER_ID))
        name = elem.get(Badge.NAME)
        tagBased = elem.get(Badge.TAG_BASED)
        badgeClass = elem.get(Badge.BADGE_CLASS)

        badge.set_id(id)
        badge.set_date(date)
        badge.set_userId(userId)
        badge.set_name(name)
        badge.set_tagBased(tagBased)
        badge.set_badgeClass(badgeClass)
        return badge

    @staticmethod
    def get_migrate_data(input):
        if input.startswith("from http://") or input.startswith("from https://"):
            index1 = input.index("://")+len("://")
            index2 = input.index("/",index1)
            site = input[index1:index2]

            index1 = input.index("/questions/") + len("/questions/")
            index2 = input.index("/", index1)
            post_id = input[index1:index2]
            return (site, int(post_id))
        elif input.startswith("to http://") or input.startswith("to https://"):
            index1 = input.index("://") + len("://")
            index2 = input.index("/", index1)
            site = input[index1:index2]

            index1 = input.index("/questions/") + len("/questions/")
            index2 = input.index("/", index1)
            post_id = input[index1:index2]
            return (site, int(post_id))
        else:
            return None

    light_user = LightUser()