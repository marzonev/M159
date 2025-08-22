import os
from flask import Flask, render_template
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'randomkey'

# Credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

ACCESS_TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
AUTHORIZE_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"

# OAuth Setup
oauth = OAuth(app)
oauth.register(
    name='entra',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    access_token_url=ACCESS_TOKEN_URL,
    authorize_url=AUTHORIZE_URL,
    client_kwargs={
        'scope': 'User.Read'
    },
)

@app.route('/')
def login():
    redirect_url = "http://localhost:5000/callback"
    return oauth.entra.authorize_redirect(redirect_url)

@app.route('/callback')
def callback():
    token = oauth.entra.authorize_access_token()
    resp = oauth.entra.get('https://graph.microsoft.com/v1.0/me')
    resp.raise_for_status()
    profile = resp.json()

    # Übergabe an ein Template
    return render_template('profile.html', profile=profile)

if __name__ == "__main__":
    app.run(debug=True)
