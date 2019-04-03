import requests

def impDino():
    resp= requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')
    return resp