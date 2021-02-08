from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from markupsafe import escape

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)

from models import *


@app.route('/')
def main():
    return "Welcome to Penn Club Review WHOOOHOOO!"

@app.route('/api')
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})
    # return jsonify("welcome to the api")

# returns the information assiciated with a username
@app.route('/api/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    user = User.query.get(username)
    if (user == None):
        return jsonify("User does not exist")
    return jsonify({"name": user.id, "email": user.email})

# Either GETS all clubs and their information, or POSTS a new club
@app.route('/api/clubs', methods=['GET', 'POST'])
def postClubs():
    # if GET, returns information for every club
    if (request.method == 'GET'):
        clubs = Club.query.all()
        ls = []
        for i in clubs:
            tags = []
            for j in i.tags:
                tags.append(j.id)
            dic = {'code': i.code, 'name': i.name, 'description': i.description, 
                'tags': tags, 'favorites': len(i.users)}
            ls.append(dic)
        return jsonify(ls)
    # if POST, creates a new club
    else:
        req = request.get_json()
        tags = []
        if not Club.query.get(req['code']) == None:
            return jsonify("club already exists")
        for i in req['tags']:
            tag = Tag.query.get(i)
            if tag != None:
                tags.append(tag)
            else:
                #create new tag if tag doesn't exist
                newTag = Tag(id=i)
                db.session.add(newTag)
                db.session.commit()
                tags.append(newTag)
        db.session.add(Club(code=req['code'], name=req['name'], 
            description=req['description'], tags=tags))
        db.session.commit()
        return jsonify("new club: " + req['name'] +  " created")

# returns all club names that match the case-insensitive search query
@app.route('/api/clubs/search=<QUERY>')
def searchClubs(QUERY):
    clubs = Club.query.all()
    filtered = []
    for i in clubs:
        # lowercasing the letters makes it case-insensitive
        c = i.name.lower()
        if c.find(QUERY.lower()) != -1:
            filtered.append(i.name)
    return jsonify(filtered)

# Allows users to favorite clubs, each user can only favorite each club once.
@app.route('/api/<club>/favorite', methods=['POST'])
def fav_club(club):
    clubs = Club.query.all()
    curUser = request.get_json()
    name = curUser['id']
    userObj = None
    allusers = User.query.all()
    # find the user that is favoriting
    for i in allusers:
        if i.id == name:
            userObj = i
            break
    if userObj == None:
        return jsonify("user does not exist")

    for i in clubs:
        if i.name == club:
            users = i.users
            # check if already favorited
            for j in users:
                if j.id == name:
                    return jsonify("Already favorited")
            i.users.append(userObj)
            db.session.commit()
            return jsonify("Favorited")
    return jsonify("club not found")

# Returns the number of clubs associated with each tag
@app.route('/api/tag_count')
def tag_cnt():
    clubs = Club.query.all()
    tags = {}
    for i in clubs:
        for j in i.tags:
            if j.id not in tags:
                tags[j.id] = 1
            else:
                tags[j.id] += 1
    return jsonify(tags)

# Modifies the specified club if it exists.
@app.route('/api/clubs/<code>', methods=['PATCH'])
def modify_club(code):
    clubObj = Club.query.get_or_404(code)
    input = request.get_json()
    changeMade = False
    if "name" in input:
        clubObj.name = input["name"]
        changeMade = True
    if "description" in input:
        clubObj.description = input["description"]
        changeMade = True
    if "tags" in input:
        clubObj.tags = []
        for i in input["tags"]:
            if Tag.query.get(i) == None:
                newTag = Tag(id=i)
                db.session.add(newTag)
                db.session.commit
                clubObj.tags.append(newTag)
            else:
                clubObj.tags.append(Tag.query.get(i))
        changeMade = True
    
    if changeMade:
        return jsonify(code + " updated")
    else:
        return jsonify("no changes made to " + code)



if __name__ == '__main__':
    app.run()
