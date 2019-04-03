import requests # Import du module requests
from flask import Flask 
from flask import render_template
app= Flask(__name__)

#response = requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')

#response.status_code # 200

#for val in response.json():
#    print(val['slug'])

@app.route('/')
def index():
    return render_template('index.html')



