1. Initialize virtual environment and activate it 
virtualenv .venv
source .venv/bin/activate

2. Install all the dependencies 
pip install -r requirements.txt


flask run
curl -X POST -F "file=@a.png" http://127.0.0.1:5000/upload >> fin.png