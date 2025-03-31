from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    symptom = request.form.get('symptom')
    if not symptom:
        return render_template('index.html', error="Por favor, descreva seu sintoma")
    
    symptom_responses = {
        "DOR DE CABEÇA": "TOMA DIPIRONA",
        "VOMITO": "FAZ CHÁ",
        "DILATAÇÃO OCULAR": "TÁ FICANDO CEGO, CONSULTE UM MÉDICO",
        "DORMÊNCIA": "FALTA DE DORMIR NÉ SEU BURRO",
        "AINDA NÃO SEI": "ALZHAIMER"
    }
    
    selected_message = symptom_responses.get(symptom.upper())
    if not selected_message:
        messages = [
            "Tem que ver isso ai",
            "Consulte um responsável",
            "Se cuida ai",
            "Eu não consigo processar isso, desculpa",
            "Meu médico responsável não aprendeu isso ainda"
        ]
        selected_message = random.choice(messages)
    return render_template('index.html', message=selected_message)

if __name__ == '__main__':
    app.run(debug=True)