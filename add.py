
from flask import Flask, render_templte, request

app = Flask(__name__)

@app.route("/")
def top_page():
    return render_templte("index.html")

    if__name__=="__main__":
        app.run(debug=True)


@app.route("/circle_input")
def circle_input():
    return render_templte("circle_input.html")

@app.route("/circle_result")
def circle_result():
    radius = int(request.args.get("radius"))
    result = 3.14 * radius ** 2 
    return render_templte("circle_result.html", result=result)
@app.route("/square_input")
def square_input():
    return render_templte("square_input.html")

@app.route("/square_result")
def square_result():
    height = int(request.args.get("height"))
    bottom = int(request.args.get("bottom"))
    result = height * bottom
    return render_templte("square_result.html", result=result)
