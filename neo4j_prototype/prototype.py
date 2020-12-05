from flask import Flask, request, render_template, redirect
from neo4j import GraphDatabase

driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j","test"))
session = driver.session()

app = Flask(__name__)

# ===== USER CREATION / LOGIN =====
@app.route('/')
def login_page():
    return render_template("login.html")


@app.route('/home', methods=['POST'])
def show_friends():
    curUser = request.form['username']
    create_new_user_node(curUser)
    return redirect("/{}".format(curUser))

def create_new_user_node(curUser):
    # creates new user node when a new user log in
    query = """
    MERGE (n:User{name:$curUser}) return n.name as name
    """
    print(curUser)
    formatter = {"curUser": curUser}
    session.run(query, formatter)
    return

# ===== USER SIGNED IN =====
@app.route('/<string:username>')
def logged_in(username):
    followings = get_user_following(username)
    search_results = get_all_nonfollowed_users(username)
    print(followings, search_results)
    return render_template(
        "friends.html",
        current_user = username,
        followings = followings,
        search_results = search_results
    )


def get_user_following(username):
    query = """
    MATCH (c:User{name:$curUser})-[r:FOLLOWS]->(f:User)
    return f.name as name
    """
    print(query)

    formatter = {"curUser": username}
    results = session.run(query, formatter)

    following_names = []
    for result in results:
        print(result["name"])
        following_names.append(result["name"])
    
    return following_names

    
def get_all_nonfollowed_users(username):
    query = """
    MATCH (current_user:User{name:$curUser}), (other_users:User)
    WHERE NOT (current_user)-[:FOLLOWS]->(other_users) and current_user<>other_users
    RETURN other_users.name as name
    """
    print(query)

    formatter = {"curUser": username}
    results = session.run(query, formatter)

    result_names = []
    for result in results:
        print(result["name"])
        result_names.append(result["name"])
    
    return result_names

# ===== USER FOLLOWING OTHER USERS =====
@app.route('/follow', methods=['POST'])
def follow_user_handler():
    username = request.form['username']
    to_follow_username = request.form['to_follow']
    follow_user(username, to_follow_username)
    return redirect('/{}'.format(username))

def follow_user(username, to_follow_username):
    query = """
    MATCH (c:User{name:$curUser}), (f:User{name:$toFollow})
    CREATE (c)-[r:FOLLOWS]->(f)
    """

    formatter = {"curUser": username, "toFollow": to_follow_username}
    session.run(query, formatter)

# ===== USER UNFOLLOWING OTHER USERS ===== 
@app.route('/unfollow', methods=['POST'])
def unfollow_user_handler():
    username = request.form['username']
    to_unfollow_username = request.form['to_unfollow']
    unfollow_user(username, to_unfollow_username)
    return redirect('/{}'.format(username))

def unfollow_user(username, to_unfollow_username):
    query = """
    MATCH (c:User{name:$curUser})-[r:FOLLOWS]->(f:User{name:$toUnfollow})
    DELETE r
    """

    formatter = {"curUser": username, "toUnfollow": to_unfollow_username}
    session.run(query, formatter)

if __name__ == "__main__":
    app.run()