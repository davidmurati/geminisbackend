import google.generativeai as genai
from flask_cors import CORS
from flask import Flask, jsonify, render_template, request
from supabase import create_client, Client


#Configure API Key
genai.configure(api_key="AIzaSyCwy6pcO6JN64J8LQG0tZchO5GoY8YMHVI")

url: str = 'https://slddqnvyyutkuadhwrct.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNsZGRxbnZ5eXV0a3VhZGh3cmN0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDE1NTQ2MzAsImV4cCI6MjAxNzEzMDYzMH0.iDBjoANWnL1kMvovWAGfAzF8reQO4TIbjp0p1J1tTqY'
supabase: Client = create_client(url, key)

app = Flask (__name__)

# Settings
CORS(app)

@app.route('/resultado', methods=['POST'])
def run_automation():
    

    if request.method == 'POST':
         # search_key es lo capturado por el textbox
        data = request.get_json()

        if 'consulta' in data:  # Assuming 'consulta' is the key for captured text
            search_key = data['consulta'] 

        #search_key = data #borrar

        title = obtener_resultado(search_key)
        
        data = supabase.table('backendpythonmed').insert({"Respuesta": title}).execute()

        
    return jsonify({'msg': 'User Added Successfully!'})

#----------------------------------------



#----------------------------------------


@app.route('/')
def index():
    
    #return render_template('index.html')
    return '<h1> Hola soy el backend med </h1>'



def obtener_resultado( search_key):

    try:

        config = {
            "max_output_tokens": 2048,
            "temperature": 0.9,
            "top_p": 1
        }


       #List of models

        #for model in genai.list_models(): 
            #print(model.name)

        #Generate Text
        model = genai.GenerativeModel('models/gemini-pro')

        response = model.generate_content(search_key, generation_config=config)

        respuesta= (response.text)

    

    except:

        respuesta= ("Ha ocurrido un error, no se genero la respuesta. Vuelva a intentarlo") 

       

    return respuesta


if __name__ == '__main__':
    app.run(debug=True)