# Run the following commands in PyCharm's terminal to build the virtual environment (change the folder path as needed)

#.....Below creates the virtual environment
# py -3 -m venv _268_Portfolio_Site

#.....Below activates the virtual environment
# C:\Users\ryanganshert\PycharmProjects\Python_Zero_to_Master\_268_Portfolio_Site\Scripts\activate.bat
#.\\_256_Web_Development\server\Scripts\activate.bat

#.....Below installs Flast within the new virtual environment
# pip3 install Flask

# IMPORTANT: use cd to naviage terminal to the correct folder folder
# PS C:\Users\ryanganshert\PycharmProjects\Python_Zero_to_Master\_256_Web_Development\server>

#.....Below initiates our .py file and begins running it on the server
# $env:FLASK_APP="_256_Web_Dev.py"

# Next isOPTIONAL
# $env:FLASK_ENV="development"

#.....Run server locally
# flask run

#.....Run server open for other devices to find
# flask run --host="0.0.0.0"

from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        #write_to_form_data(data)
        write_to_form_data_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'

def write_to_form_data(data):
    try:
        with open('form_data.txt', mode='a') as form_data:
            # mode defaults to R (read)
            # Use W for write (write - deletes what's already there
            #       write also create a new file if it doesn't already exist)
            # Use R+ for read/write (seems to function the same as append?)
            # Use A for append (append to the end)

            email = data['email']
            subject = data['subject']
            message = data['message']

            form_data.write(f"\n{email},{subject},{message}")

    except FileNotFoundError as err:
        return f"The requested file was not found. {err}"
    except IOError as err:
        return f"IO error. {err}"

def write_to_form_data_csv(data):
    try:
        with open('form_data.csv', mode='a', newline='') as form_data:
            # mode defaults to R (read)
            # Use W for write (write - deletes what's already there
            #       write also create a new file if it doesn't already exist)
            # Use R+ for read/write (seems to function the same as append?)
            # Use A for append (append to the end)

            email = data['email']
            subject = data['subject']
            message = data['message']

            csv_writer = csv.writer(form_data, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])

    except FileNotFoundError as err:
        return f"The requested file was not found. {err}"
    except IOError as err:
        return f"IO error. {err}"
