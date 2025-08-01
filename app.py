# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# 建議資料庫
def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS todos(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL)
              ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM todos')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('INSERT INTO todos(task) VALUES(?)',(task,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('DELETE FROM todos WHERE id=?',(task_id,))
    conn.commit()
    conn.close()
    return redirect('/')
    
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
    
    
    
    
    
    
    
    
    
    