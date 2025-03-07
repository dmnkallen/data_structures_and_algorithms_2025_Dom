from flask import Flask, render_template

app = Flask(__name__)

@app.route("/about")
def about():
    name = "Dominik Allen"
    subtitle = "Hertie Student and aspiring data scientist"
    about_me = "I like traveling, learning, and staying active. In my previous courses I have learned R language, intermediate statistics, and introductory data science. In this course I hope to gain in depth knowledge in how to design and evaluate algorithms, as well as get hands on coding experience in this new language of python."
    photo_url = "static/dompic.jpeg"  
    social_link = "https://www.linkedin.com/in/dominik-allen-a28ab422a"  

    return render_template("about.html", name=name, subtitle=subtitle, about_me=about_me, photo_url=photo_url, social_link=social_link)

if __name__ == "__main__":
    app.run(debug=True)