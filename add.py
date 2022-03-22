from flask import Flask, render_templte

app = Flask(_name_)

@app.route("/")
def top_page():
    return render_templte("index.html")

    if_name_=="_main_":
        app.run(debug=True)
