# -*- coding: utf-8 -*-

from flask import Flask, request, session, render_template
from flask import redirect, url_for
import datetime

# Flaskのアプリケーション オブジェクトを作成
app = Flask(__name__)


# http://localhost:5000/でアクセスされる関数
@app.route('/')
def index_html():
    today = datetime.datetime.today()
    import cProfile
    cProfile.runctx("""render_template('index.html', dt=today)""",
            locals(),globals())
    return render_template('index.html', dt=today)

# /message_formでアクセスされる関数
@app.route('/message_form')
def message_form():
    # テンプレートファイル templates/message_form.htmlを表示
    import pdb; pdb.set_trace()
    return render_template('message_form.html')


# /add_messageでリクエストのメッセージを登録
@app.route('/add_message', methods=['POST'])
def add_message():
    # Sessionにメッセージを登録
    msgs = session.get('messages', [])
    if len(msgs) > 16:
        return redirect(url_for('show_messages'))
    msgs.append(request.form['message'])
    session['messages'] = msgs[-10:]
    return redirect(url_for('show_messages'))


# /showでリクエストのメッセージを登録
@app.route('/show')
def show_messages():
    # テンプレートファイル templates/show_messages.htmlを表示
    #return render_template('show_messages.html',
    #                       messages=reversed(session['messages']))
    import cProfile
    import logging
    app.logger.setLevel(40) # => logging.ERROR
    app.logger.debug('debug')
    app.logger.error('error msg')
    cProfile.runctx("""ret = render_template('show_messages.html',
                           messages=reversed(session['messages']))""",
                           locals(), globals(),sort='cumulative')
    return ret

def main():
    app.secret_key = "secret"
    app.run(debug = True, port=9999)

if __name__ == '__main__':
    main()
