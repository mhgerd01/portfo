from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home(username=None, post_id=None):
    return render_template('index.html')

@app.route("/portfoliows")
def portfoliows():
    return render_template('portfoliows.html')

@app.route("/portfoliobm")
def portfoliobm():
    return render_template('portfoliobm.html')

@app.route("/portfoliowd")
def portfoliowd():
    return render_template('portfoliowd.html')

@app.route("/portfoliodv")
def portfoliodv():
    return render_template('portfoliodv.html')

@app.route("/portfoliodsml")
def portfoliodsml():
    return render_template('portfoliodsml.html')

@app.route("/portfoliota")
def portfoliota():
    return render_template('portfoliota.html')

@app.route("/thankyou")
def thankyou():
    return render_template('thankyou.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        file = database.write(f'\n{name},{email},{message}')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou#contact')
        except:
            return 'did not save to database'
        else:
            return "something went wrong please try again"

