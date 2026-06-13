from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def home():

    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except:
        contacts = []

    return render_template('index.html', contacts=contacts)


@app.route('/add', methods=['GET', 'POST'])
def add_contact():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        contact = {
            "name": name,
            "email": email,
            "phone": phone
        }

        try:
            with open('contacts.json', 'r') as file:
                contacts = json.load(file)
        except:
            contacts = []

        contacts.append(contact)

        with open('contacts.json', 'w') as file:
            json.dump(contacts, file, indent=4)

        return redirect('/')

    return render_template('add_contact.html')


if __name__ == '__main__':
    app.run(debug=True)