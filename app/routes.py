from flask import render_template, request, redirect, url_for
from app import app

posts = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       name = request.form['name']
       city = request.form['city']
       hobby = request.form['hobby']
       year = request.form['year']
       if name and city and hobby and year:
           posts.append({'name': name, 'city': city, 'hobby': hobby, 'year':year})
           return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)


