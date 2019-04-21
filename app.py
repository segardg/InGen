import requests # Import du module requests
from flask import Flask 
from flask import render_template
app= Flask(__name__)
from jp.function import impDino
from jp.function import dino_info


#response = requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')

#response.status_code # 200

#for val in response.json():
#    print(val['slug'])

@app.route('/')
def index():
        return render_template('index.html', resp=impDino())

@app.route('/dinosaur/<name>')
def detail(name):
    return render_template('dino.html', resp=dino_info(name))    

