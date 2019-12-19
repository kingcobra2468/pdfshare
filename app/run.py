from flask import Flask, redirect, url_for
from routes import feed_blueprint, download_blueprint

app = Flask(__name__)

app.register_blueprint(feed_blueprint)
app.register_blueprint(download_blueprint)

@app.route('/')
def home(): #root will be redirected to library page
    return redirect('library')

if __name__ == "__main__":
    app.run(host = '0.0.0.0')