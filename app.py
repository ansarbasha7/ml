from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def number_enter():
    return render_template('number.html')


@app.route('/num_verify', methods=['POST'])
def num_verify():
    if request.method == 'POST':
        form = request.form
        num = form['num']
        if num == '17':
            return render_template('logi.html')
        else:
            return render_template('number.html')


@app.route('/verify_signin', methods=['POST'])
def verify_signin():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        password = form['password']
        if name == 'gengulu' and password == 'nehaansar':
            return render_template('matter.html')
        else:
            return render_template('logi.html')

@app.route('/viedo', methods=['POST'])
def viedo():
    return render_template('viedo.html')

@app.route('/image_show', methods=['POST'])
def show_images():
    return render_template('full_images.html')


@app.route('/bye', methods=['POST'])
def bye_page():
    return render_template('by.html')

@app.route('/wishes', methods=['POST'])
def wishes():
    return render_template('wishes.html')


if __name__ == '__main__':
    app.run()
