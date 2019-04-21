import requests

def impDino():
    resp= requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')
    return resp.json()

def dino_info(name):
    resp= requests.get('https://medusa.delahayeyourself.info/api/dinosaurs/')
    for dino in resp.json():
        if dino["slug"]==name :
            dinosaure = requests.get(dino["uri"])
    return dinosaure.json()