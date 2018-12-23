# render_templateを追加
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    # render_templateでindex.htmlを読み込んで、表示する
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(debug=True)