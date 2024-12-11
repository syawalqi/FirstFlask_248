from flask import Flask, render_template, request, redirect, url_for

app = Flask(
    __name__,
    template_folder='view',  # Folder untuk template
    static_folder='view'     # Folder untuk file statis
)

# Menyimpan data pengguna sementara (gunakan database untuk aplikasi nyata)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Simpan data register ke dalam dictionary
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

from flask import redirect

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Redirect ke YouTube
        else:
            return "Login gagal, coba lagi."
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
