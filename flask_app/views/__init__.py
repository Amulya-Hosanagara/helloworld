from config.app import app

@app.route('/')
@app.route('/user')
def index():
    return "Hello, World!"
