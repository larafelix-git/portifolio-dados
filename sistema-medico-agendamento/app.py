from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/novo_agendamento", methods=["GET", "POST"])
def novo_agendamento():
    if request.method == "POST":
        descricao = request.form.get("descricao")
        data = request.form.get("data")
        hora = request.form.get("hora")
        tutor = request.form.get("tutor")
        medicamento = request.form.get("medicamento")
        clinica = request.form.get("clinica")
        medico = request.form.get("medico")
        crm = request.form.get("crm")
        contato_medico = request.form.get("contato_medico")
        contato1 = request.form.get("contato1")
        contato2 = request.form.get("contato2")

        conexao = db.conectar()
        cursor = conexao.cursor()

        # tutor
        cursor.execute("INSERT INTO Tutor (nome, contato) VALUES (%s, %s)", (tutor, contato1))
        tutor_id = cursor.lastrowid

        # medicamento (pode ser vazio)
        if medicamento:
            cursor.execute("INSERT INTO Medicamento (nome, descricao) VALUES (%s, %s)", (medicamento, ''))
            medicamento_id = cursor.lastrowid
        else:
            medicamento_id = None

        # clinica (pode ser vazio)
        if clinica:
            cursor.execute("INSERT INTO Clinica (nome, endereco) VALUES (%s, %s)", (clinica, ''))
            clinica_id = cursor.lastrowid
        else:
            clinica_id = None

        # medico
        cursor.execute("INSERT INTO Medico (nome, crm, contato) VALUES (%s, %s, %s)", (medico, crm, contato_medico))
        medico_id = cursor.lastrowid

        # emergência 1
        cursor.execute("INSERT INTO Emergencia (nome, contato) VALUES (%s, %s)", ("Contato Emergência 1", contato1))
        emergencia1_id = cursor.lastrowid

        # emergência 2 (se existir)
        if contato2:
            cursor.execute("INSERT INTO Emergencia (nome, contato) VALUES (%s, %s)", ("Contato Emergência 2", contato2))
            emergencia2_id = cursor.lastrowid
        else:
            emergencia2_id = None

        # agendamento
        cursor.execute("""
            INSERT INTO Agendamento (
                descricao_alerta, data_agendamento, hora_agendamento, 
                tutor_id, medicamento_id, clinica_id, medico_id, emergencia1_id, emergencia2_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (descricao, data, hora, tutor_id, medicamento_id, clinica_id, medico_id, emergencia1_id, emergencia2_id))

        conexao.commit()
        cursor.close()
        conexao.close()

        return redirect(url_for("index"))
    
    # Se for GET
    return render_template("novo_agendamento.html")

#gerando uma pagina de visualizaçao dos dados armazenados
@app.route('/visualizacaodados')

def visualiza_dados():
    conexao = db.conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT a.id, a.descricao_alerta, a.data_agendamento, a.hora_agendamento,
               t.nome as tutor_nome, m.nome as medico_nome
        FROM Agendamento a
        LEFT JOIN Tutor t ON a.tutor_id = t.id
        LEFT JOIN Medico m ON a.medico_id = m.id
    """)
    agendamentos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template('visualiza_dados.html', agendamentos=agendamentos)

if __name__ == '__main__':
    app.run(debug=True)
