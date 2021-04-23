source .venv/bin/activate
pip install -r requirements.txt

flask run
curl -X POST -F "file=@a.png" http://127.0.0.1:5000/upload >> fin.png