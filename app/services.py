import requests
from app.models import HistoricoConsulta

def consultar_cep_e_clima(cep):
    cep_limpo ="".join(filter(str.isdigit, cep))
    
    if len(cep_limpo) != 8:
        return {"erro": "CEP inválido. O CEP deve conter 8 dígitos."}, 400
    
    url_brasilapi = f"https://brasilapi.com.br/api/cep/v2/{cep_limpo}"
    response_cep = requests.get(url_brasilapi)
    
    if response_cep.status_code != 200:
        return {"erro": "Não foi possível consultar o CEP."}, 404
    
    dados = response_cep.json()
    
    state = dados.get("state")
    city = dados.get("city")
    
  
    clima_dados={ }
    temp_c = None
    
    if city:
        api_key_weather = "91968b0a97214258ae1214317262908"
        query = f"{city},{state}, Brasil"
        url_weather = f"https://api.weatherapi.com/v1/current.json?key={api_key_weather}&q={query}&lang=pt"
        
        response_weather = requests.get(url_weather)
       
        if response_weather.status_code == 200:
            weather_json = response_weather.json()
            current_weather = weather_json.get ("current", {})
            condition = current_weather.get("condition", {})
            
            clima_dados = {
                "Temperatura_c": current_weather.get("temp_c"),
                "Condicao": condition.get("text"),
                "Umidade": current_weather.get("humidity"),
                "Sensação_termica_c": current_weather.get ("feelslike_c"),               
            }
            
            HistoricoConsulta.objects.create(
        cep=dados.get("cep"),
        state=state,
        city=city,
        temperatura=temp_c  )

    resultado={
       "cep" : dados.get("cep"),
       "state" :state,
       "city" : city,
       "street" : dados.get("street"),
        "neighborhood" : dados.get("neighborhood"),
        "clima" :clima_dados
    }
    
    return resultado,200