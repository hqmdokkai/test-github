from flask import Flask, render_template, request
import sys
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    python_code = ""
    output = ""
    if request.method == 'POST':
        python_code = request.form['python_code']
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        try:
            exec(python_code)
        except Exception as e:
            output = str(e)
        finally:
            sys.stdout = old_stdout
            output = redirected_output.getvalue()
    return render_template('index.html', python_code=python_code, output=output)

if __name__ == '__main__':
    app.run(debug=True)
