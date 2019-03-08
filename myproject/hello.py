from flask import Flask, url_for, 
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/page1")
def page1():
    return 'Page 1'
    
@app.route('/page2')
def page2():
    # show the subpath after /path/
    return "Yo, Yo, Yo!"

@app.route("/user/<username>")
def show_user_profile(username):
    return 'User {}'.format(username)

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "Subpath {}".format(subpath)

# URL CREATOR????
# # with app.test_request_context():
# #     print(url_for('page1'))
# #     print(url_for('page2'))
# #     print(url_for('show_user_profile'))
# #     print(url_for('show_subpath'))

if __name__ == "__main__":
    app.run(debug=True)