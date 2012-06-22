from sidetask import app

@app.route('/')
@app.route('/landingpage')
def index():
        return 'Welcome to Sidetask!'
