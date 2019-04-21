import requests # Import du module requests

response = requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')

response.status_code # 200

response.text # Corps de la réponse en texte brut

response.json() # Corps de la réponse transcripté en objets

resp= requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')
for dino in resp.json():
    if dino["slug"] == "dilophosaurus" :
        dinosaure = requests.get(dino["uri"])
print(dinosaure.text)

