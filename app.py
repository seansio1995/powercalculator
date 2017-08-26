from flask import Flask, render_template, request
from math import pow
from wtforms import Form,FloatField, validators


app=Flask(__name__)

class InputForm(Form):
    n=FloatField(validators=[validators.InputRequired()])
    power=FloatField(validators=[validators.InputRequired()])


@app.route('/power',methods=["GET","POST"])

def index():
    form=InputForm(request.form)
    if request.method=="POST" and form.validate():
        n=form.n.data
        power=form.power.data
        result=pow(n,power)
        return render_template("output.html",form=form,result=result)
    else:
        return render_template("input.html",form=form)


if __name__=="__main__":
    app.run(debug=True)
