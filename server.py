from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./database.txt', mode='a') as database:
        database.write('\n')
        database.write(f"{data['email']},{data['subject']},{data['message']}")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect('thankyou.html')
    else:
        return 'Something went wrong. Try again!'
