import requests

def get_bike_data():
    # Clé API JCDecaux
    api_key = "e0a1bf2c844edb9084efc764c089dd748676cc14"
    url = f"https://api.jcdecaux.com/vls/v3/stations?apiKey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        bike_data = response.json()
        return bike_data
    else:
        print("Erreur lors de la récupération des données:", response.status_code)
        return None

def analyze_bike_data(bike_data):
    if bike_data:
        total_bikes = len(bike_data)
        mechanical_bikes = sum(1 for bike in bike_data if 'type' in bike and bike['type'] == 'mechanical')
        electric_bikes = sum(1 for bike in bike_data if 'type' in bike and bike['type'] == 'electric')
        mechanical_percentage = (mechanical_bikes / total_bikes) * 100 if total_bikes > 0 else 0
        electric_percentage = (electric_bikes / total_bikes) * 100 if total_bikes > 0 else 0

        print("Statistiques sur les vélos :")
        print("Nombre total de vélos :", total_bikes)
        print("Nombre de vélos mécaniques :", mechanical_bikes)
        print("Nombre de vélos électriques :", electric_bikes)
        print("Pourcentage de vélos mécaniques :", mechanical_percentage)
        print("Pourcentage de vélos électriques :", electric_percentage)
    else:
        print("Aucune donnée à analyser.")

bike_data = get_bike_data()
analyze_bike_data(bike_data)
