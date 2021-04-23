1. Initialize virtual environment and activate it 
python3 -m venv .venv
source .venv/bin/activate

2. Install all the dependencies 
pip3 install -r requirements.txt

3. Run Flas server
flask run
(If there is an error such as "ImportError: libGL.so.1: cannot open shared object file"
    you should run "apt-get install -y python3-opencv")

4. Upload picture either via curl command, or by goint to "http://127.0.0.1:5000/upload" in web browser. 
curl -X POST -F "file=@image.png" http://127.0.0.1:5000/upload >> final.png