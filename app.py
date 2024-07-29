from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Use uma chave secreta segura em produção

# Configurações do banco de dados a partir das variáveis de ambiente
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 3306),
    'database': os.getenv('DB_NAME', 'login_db'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'rootpassword')
}

# Função para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Função para criar a tabela de usuários, se não existir
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE usuario = %s', (usuario,))
        if cursor.fetchone():
            flash('Nome de usuário já existe. Tente novamente.')
        else:
            cursor.execute('INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)', (usuario, senha))
            conn.commit()
            flash('Registro concluído com sucesso!')
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE usuario = %s AND senha = %s', (usuario, senha))
        if cursor.fetchone():
            flash('Login bem-sucedido!')
        else:
            flash('Nome de usuário ou senha incorretos. Tente novamente.')
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('login.html')

if __name__ == "__main__":
    create_table()
    app.run(host='0.0.0.0', port=5000)

