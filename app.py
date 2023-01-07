from flask import Flask, render_template, request
from pymongo import MongoClient

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    content = StringField('콘텐츠', validators=[DataRequired()])
    src = StringField('URL 주소', validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
connection = MongoClient('mongodb+srv://carl1350:pcRfM3Rm6ryaf9TX@cluster0.96iktkk.mongodb.net/?retryWrites=true&w=majority')
db = connection.classicMusic
music = db.musics

# 에러 처리
@app.errorhandler(404)
def error_404(error):
    return render_template('page_404.html')

# 메인
@app.route('/')
def main_page():
    musics = music.find().sort("order")
    return render_template('index.html', musics=musics)

musiclist = music.find().sort("order")

@app.route('/beethoven')
def beethoven_music():
    index = music.find({"href": "beethoven"})[0]["order"] - 1
    title = musiclist[index]["title"]
    intro = musiclist[index]["intro2"]
    href = musiclist[index]["href"]
    content = musiclist[index]["content"]
    src = musiclist[index]["src"]
    return render_template('beethoven.html', title=title, intro=intro, href=href, content=content, src=src, zip=zip)

@app.route('/mozart')
def mozart_music():
    index = music.find({"href": "mozart"})[0]["order"] - 1
    title = musiclist[index]["title"]
    intro = musiclist[index]["intro2"]
    href = musiclist[index]["href"]
    content = musiclist[index]["content"]
    src = musiclist[index]["src"]
    return render_template('mozart.html', title=title, intro=intro, href=href, content=content, src=src, zip=zip)

@app.route('/bach')
def bach_music():
    index = music.find({"href": "bach"})[0]["order"] - 1
    title = musiclist[index]["title"]
    intro = musiclist[index]["intro2"]
    href = musiclist[index]["href"]
    content = musiclist[index]["content"]
    src = musiclist[index]["src"]
    return render_template('bach.html', title=title, intro=intro, href=href, content=content, src=src, zip=zip)

@app.route('/chopin')
def chopin_music():
    index = music.find({"href": "chopin"})[0]["order"] - 1
    title = musiclist[index]["title"]
    intro = musiclist[index]["intro2"]
    href = musiclist[index]["href"]
    content = musiclist[index]["content"]
    src = musiclist[index]["src"]
    return render_template('chopin.html', title=title, intro=intro, href=href, content=content, src=src, zip=zip)

@app.route('/vivaldi')
def vivaldi_music():
    index = music.find({"href": "vivaldi"})[0]["order"] - 1
    title = musiclist[index]["title"]
    intro = musiclist[index]["intro2"]
    href = musiclist[index]["href"]
    content = musiclist[index]["content"]
    src = musiclist[index]["src"]
    return render_template('vivaldi.html', title=title, intro=intro, href=href, content=content, src=src, zip=zip)

@app.route('/liszt')
def liszt_music():
    index = music.find({"href": "liszt"})[0]["order"] - 1
    title = musiclist[index]["title"]
    intro = musiclist[index]["intro2"]
    href = musiclist[index]["href"]
    content = musiclist[index]["content"]
    src = musiclist[index]["src"]
    return render_template('liszt.html', title=title, intro=intro, href=href, content=content, src=src, zip=zip)

@app.route('/admin', methods=['POST'])
def admin_page():
    if request.form['id'] == 'admin' and request.form['password'] == 'password':
        return render_template('admin.html')
    else:
        return "<script>window.location = document.referrer;</script>"

@app.route('/admin/add', methods=['POST'])
def add_music_page():
    form = TextForm()
    musics = music.find().sort("order")
    return render_template('add_music.html', musics=musics, form=form)

@app.route('/admin/add/action', methods=['GET', 'POST'])
def add_music():
    form = TextForm()
    if form.validate_on_submit():
        content = request.form['content']
        src = request.form['src']
        title = request.values.get('title')
        index = music.find({"title": f"{title}"})[0]["order"] - 1
        list_content = list(musiclist[index]['content'])
        list_src =  list(musiclist[index]['src'])
        list_content.append(content)
        list_src.append(src)
        music.update_one({"title": f"{title}"}, {"$set": {"content": list_content, "src": list_src}})
    return "<script type='text/javascript'>location.href='/';</script>"

if __name__ == '__main__':
    app.run()