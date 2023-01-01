from flask import Flask, render_template, request
from pymongo import MongoClient

def router(NAME):
    return render_template("{}.html".format(NAME))

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

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        if request.form['id'] == 'admin' and request.form['password'] == 'password':
            print(request.form['id'])
            print(request.form['password'])
            return render_template('admin.html')
        else:
            return "<script>window.location = document.referrer;</script>"

if __name__ == '__main__':
    app.run()