# requestモジュールとredirectモジュールを追加
from flask import Flask, render_template, request, redirect 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html') # usersはいったん消しておく 

# ユーザーが投稿すると、'/save'というURLにPOST形式でデータが送信される
@app.route('/save', methods=['POST'])
def saveView():
    # POSTで送信されたデータを受け取って、変数codeに入れる
    code = request.form['code']

    # 試しにコンソールにユーザーの入力したデータを表示してみる
    print('ユーザーの入力したデータ:' + code)

    # トップページにリダイレクト（強制的に移動）させる
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)