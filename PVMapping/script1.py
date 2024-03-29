from flask import Flask, render_template
from folium.plugins import FloatImage
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

if __name__=="__main__":
    app.run(debug=True)