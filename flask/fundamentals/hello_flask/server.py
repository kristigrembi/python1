
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def init_checkerboard():
    return render_template("index.html",number_rows=8,number_colums=8,color1="black",color2="red")

@app.route('/<int:rows>',methods=['GET'])
def change_rows(rows):
    return render_template("index.html",number_rows=rows,number_colums=8,color1="black",color2="red")
    
@app.route('/<int:rows>/<int:colums>',methods=['GET'])
def change_rows_colums(rows,colums):
    return render_template("index.html",number_rows=rows,number_colums=colums,color1="black",color2="red")

@app.route('/<int:rows>/<int:colums>/<string:color1>',methods=['GET'])
def change_rows_colums_color(rows,colums,color1):
    return render_template("index.html",number_rows=rows,number_colums=colums,color1=color1,color2="red")

@app.route('/<int:rows>/<int:colums>/<string:color1>/<string:color2>',methods=['GET'])
def change_rows_colums_colors(rows,colums,color1,color2):
    return render_template("index.html",number_rows=rows,number_colums=colums,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)