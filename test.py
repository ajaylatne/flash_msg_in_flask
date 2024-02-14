from flask import Flask, render_template, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 's4545sdcsdc'


@app.route('/fwoc')
def flash_messages_without_category():
    flash('first message')
    flash('second message')
    flash('third message')
    return render_template('fwoc.html')


@app.route('/fwc')
def flash_messages_with_category():
    flash('info message', 'info')
    flash('warning message', 'warning')
    flash('error message', 'error')
    return render_template('fwc.html')


if __name__ == "__main__":
    app.run(debug=True)
