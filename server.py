from flask import Flask, render_template
import jinja2

app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def index():

    return render_template('home.html')


@app.route('/about')
def about():

    return render_template('about.html')


@app.route('/contact')
def contact():

    return render_template('contact.html')


@app.route('/shop')
def shop():

    return render_template('shop.html')


@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/favorites')
def favorites():

    return render_template('favorites.html')


@app.route('/settings')
def settings():

    return render_template('settings.html')


@app.route('/profile')
def profile():

    return render_template('profile.html')


if __name__ == "__main__":
    app.run(debug=True)
