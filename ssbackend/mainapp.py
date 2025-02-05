from flask import url_for , request
from . import app , db, User , Post, Comment, Like, Message, Follow

def validate_user_info( get_msg = False ):
    username = request.args.get("username")
    password = request.args.get("password")
    user_info = User.query.filter_by(username=username).first()
    if user_info:
        if user_info.password == password:
            data = ("Login Completed.", username)
        else:
            data = ("Username Password Incorrect.", False)
    else:
        data = ("User Not found.", False)
    
    if get_msg:
        return { "message": data[0] }
    else:
        return data[1]

@app.route('/api/login', methods=["GET"])
def login():
    return validate_user_info( get_msg = True )

@app.route('/api/signup', methods=['POST'])
def signup():
    Users = User()
    Users.username = request.args.get("username")
    Users.password = request.args.get("password")
    Users.confirm_password = request.args.get("confirm_password")
    if Users.confirm_password == Users.password:
        Users.email = request.args.get("email")
        Users.image = request.args.get("image")
        db.session.add(Users)
        db.session.commit()
        del Users
        return {"message":"user created successfully."}
    else:
        return {"message":"Password and Confirm Password are not same."}

@app.route('/api/profile/<username>', methods = ["GET"])
def profile(username):

    user_info = validate_user_info()
    user_data = User.query.filter_by(username=username).first()

    if user_info:
        data = {
            "username" : user_data.username,
            "email" : user_data.email,
            "image" : user_data.image
        }
    else:
        data = {
            "message": "User Not found."
        }

    return data

@app.route('/api/post', methods = ["POST"])
def post():
    username = validate_user_info()
    if username:
        Posts = Post()
        Posts.username = username
        Posts.title = request.args.get("title")
        Posts.content = request.args.get("content")
        Posts.image = request.args.get("image")
        db.session.add(Posts)
        db.session.commit()
        del Posts
        return {"message":"Post Uploaded successfully."}
    else:
        return {"message": "User Not found."}


@app.route('/api/add_comment', methods = ["POST"])
def comment():
    username = validate_user_info()
    if username:
        Comments = Comment()
        Comments.username = username
        Comments.post_id = request.args.get("post_id")
        Comments.comment_content = request.args.get("comment_content")
        db.session.add(Comments)
        db.session.commit()
        del Comments
        return {"message":"Comment Uploaded successfully."}
    else:
        return {"message": "User Not found."}


@app.route('/api/like_post', methods = ["POST"])
def like():
    username = validate_user_info()
    if username:
        Likes = Like()
        Likes.username = username
        Likes.post_id = request.args.get("post_id")
        if request.args.get("like_status") == "true":
            Likes.like_status = True
        else:
            Likes.like_status = False
        db.session.add(Likes)
        db.session.commit()
        del Likes
        return {"message":"Liked."}
    else:
        return {"message": "User Not found."}

@app.route('/api/get_comments/<int:post_id>', methods = ["GET"])
def comments(post_id):

    username = validate_user_info()
    data = {"message":"Comment Not Found."}
    if username:
        db_info = Comment.query.filter_by( post_id = post_id ).all()
        data = {
            "count": len(db_info),
            "usernames": [ x.username for x in db_info ],
            "comments": [ x.comment_content for x in db_info ]
        }
    else:
        return {"message": "User Not found."}

    return data

@app.route('/api/get_likes/<int:post_id>', methods = ["GET"])
def likes(post_id):
    username = validate_user_info()
    if username:
        db_info = Like.query.filter_by( post_id = post_id ).all()
        data = {
            "count": len(db_info),
            "usernames": [ x.username for x in db_info ],
        }
    else:
        return {"message": "User Not found."}
    return data

@app.route('/search/<username>', methods = ["GET"])
def search(username):
    profile(username)

@app.route('/api/delete/post/<int:post_id>', methods = ["DELETE"])
def delete_post(post_id):
    username = validate_user_info()
    if username:
        post_info = Post.query.filter_by( id = post_id ).first()
        if post_info.username == username:
            db.session.delete(post_info)
            db.session.commit()
        else:
            return {"message": "You are trying to delete someone elses post."}
    else:
        return {"message": "User Not found."}

@app.route('/api/update_post/<int:post_id>', methods = ["POST"])
def post_update(post_id):
    username = validate_user_info()
    if username:
        Posts = Post.query.filter_by( id = post_id ).first()
        Posts.title = request.args.get("title")
        Posts.content = request.args.get("content")
        db.session.add(Posts)
        db.session.commit()
        del Posts
        return {"message":"Post Uploaded successfully."}
    else:
        return {"message": "User Not found."}

@app.route('/api/delete/comment/<int:comment_id>', methods = ["DELETE"])
def delete(comment_id):
    username = validate_user_info()
    if username:
        comment_info = Comment.query.filter_by( id = comment_id ).first()
        if comment_info.username == username:
            db.session.delete(comment_info)
            db.session.commit()
        else:
            return {"message": "You are trying to delete someone elses comment."}
    else:
        return {"message": "User Not found."}

@app.route('/api/send/message/<receiver_username>', methods = ["POST"])
def message(receiver_username):
    username = validate_user_info()
    if username:
        receiver = User.query.filter_by(username=receiver_username).first()
        if receiver:
            sender_username = username
            content = request.args.get("content")
            chat = Message.query.filter_by(sender_username=sender_username, receiver_username=receiver_username).first()
            if chat:
                message = f"{chat.content}\n{sender_username}: {content}"
                chat.content = message
            else:
                chat = Message()
                chat.sender_username = sender_username
                chat.receiver_username = receiver_username
                chat.content = f"{sender_username}: {content}"
            db.session.add(chat)
            db.session.commit()
            del chat
            return {"message":"Message Sent."}
        else:
            return {"message": "Receiver Not found."}
    else:
        return {"message": "Sender Not found."}

@app.route('/api/load/messages/<receiver_username>', methods = ["GET"])
def load_message(receiver_username):
    username = validate_user_info()
    if username:
        receiver = User.query.filter_by(username=receiver_username).first()
        if receiver:
            chat = Message.query.filter_by(sender_username=username, receiver_username=receiver_username).first()
            if chat:
                return { "data": chat.content }
            else:
                return {"message": "No Chat Has Done Yet"}
        else:
            return {"message": "Receiver Not found."}
    else:
        return {"message": "Sender Not found."}

@app.route('/api/follow/<username_to_follow>', methods = ["POST"])
def follow_api(username_to_follow):
    username = validate_user_info()
    if username:
        Follows = Follow()
        username_to_follow_in_db = User.query.filter_by(username=username_to_follow).first()
        if username_to_follow_in_db:
            if username_to_follow == username_to_follow_in_db.username:
                if username_to_follow != username:
                    if Follow.query.filter_by(username=username, following=username_to_follow).first():
                        data = { "message": "Already following this username." }
                    else:
                        Follows.username = username
                        Follows.following = username_to_follow
                        db.session.add(Follows)
                        db.session.commit()
                        del Follows
                        data = {"message" : "Follow Successfully Done."}
                else:
                    data = {"message": "Seems like you are trying to follow yourself."}
        else:
            data = {"message" : "Username To Follow Not Found."}
    else:
        data = {"message": "User Not found."}

    return data

@app.route('/api/get_followings/', methods = ["GET"])
def following():
    username = validate_user_info()
    if username:
        db_info = Follow.query.filter_by(username=username).all()
        data = {
            "count": len(db_info),
            "following_list": [ x.following for x in db_info ],
        }
    else:
        data = {"message": "User Not found."}

    return data

@app.route('/api/get_followers/', methods = ["GET"])
def followers():
    username = validate_user_info()
    if username:
        db_info = Follow.query.filter_by(following=username).all()
        data = {
            "count": len(db_info),
            "followers_list": [ x.username for x in db_info ],
        }
    else:
        data = {"message": "User Not found."}

    return data
