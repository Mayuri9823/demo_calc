from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calcultormain():
    result = 0
    resp = request.form
    a = resp.get('fnum')
    b = resp.get('snum')

    if resp.get('calc') == '1':
        try:
            result = int(a)+int(b)
        except:
            result = 'Please Enter Valid Inputs'

    elif resp.get('calc') == '2':
        try:
            result = int(a) - int(b)
        except:
            result = 'Please Enter Valid Inputs'

    elif resp.get('calc') == '3':
        try:
            result = int(a) * int(b)
        except:
            result = 'Please Enter Valid Inputs'

    elif resp.get('calc') == '4':
        try:
            result = int(a)/int(b)
        except:
            result = 'Please Enter Valid Inputs'

    return render_template("calci.html", abc=result)


if __name__ == '__main__':
    app.run(debug=True)