from flask import Flask, render_templte, request

app = Flask(__name__)

@app.route("/")
def top_page():
    return render_templte("index.html")

    if__name__=="__main__":
        app.run(debug=True)

@app.route("/square_input")
def square_input():
    return render_templte("square_input.html")

@app.route("/square_result")
def square_result():
    height = int(request.args.get("height"))
    bottom = int(request.args.get("bottom"))
    result = height * bottom
    return render_templte("square_result.html", result=result)