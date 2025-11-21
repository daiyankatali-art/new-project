from flask import Flask, render_template
import os
app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def welcome():
    print("Serving welcome.html")
    return render_template("welcome.html")

@app.route("/home")
def home_page():
    return render_template("home.html")




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port , debug=True)
