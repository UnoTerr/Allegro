from flask import Flask, request, render_template, send_file
import image, os 

app = Flask(__name__)

@app.route('/upload', methods=['GET'])
def index():
    #return "Hello World!"
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        image.rotation(file)
        try:
            return send_file('fin.png', mimetype='image/png')
        except:
            return('204 No content')
        os.remove('fin.png') 
    except Exception as err:
        print('Error occurred')
        print(err)
        return('Error, image not received.')

# curl -X POST -F "file=@a.png" http://127.0.0.1:5000/upload >> fin.png