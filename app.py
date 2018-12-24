from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    # ユーザー名をリストusersに格納する
    users = ['Flask太郎', 'Python一郎', 'Jinja次郎']
    # render_templateの第2引数に、users=usersを追加
    return render_template('index.html', users=users) 

if __name__ == "__main__":
    app.run(debug=True)