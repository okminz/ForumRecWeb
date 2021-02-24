import flask
# import requests_oauthlib
import requests
import pickle

# Use pickle to load in model
# with open(f'model/first_model.pkl', 'rb') as f:
#     model = pickle.load(f)

AUTH_BASE_URL = "https://stackexchange.com/oauth/dialog?client_id=19673&scope=&redirect_uri=http://localhost:5000/"

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    return """
        <a href="/login">Login with SuperUser</a>
    """

    # if flask.request.method == 'GET':
    #     return(flask.render_template('main.html'))
    
    # if flask.request.method == 'POST':
    #     returnVal = requests.get('').content
    #     print(returnVal)
        

    # return(flask.render_template('main.html'))

@app.route('/', methods=['GET', 'POST'])
def get_data():
    returnVal = requests.get('https://stackexchange.com/oauth/dialog?client_id=19673&scope=&redirect_uri=http://localhost:5000/').content
    print(returnVal)
    return returnVal

if __name__ == '__main__':
    app.run(debug=True)
