# DINPortal
Flask app to interact with [DNI](https://github.com/richmcateer/DIN) contract.

Current DNI Contract Address: `0xcee847df50cf2a798e33e5a7282684255869eccf`

### Run Locally
 1. `export FLASK_APP=dinport.py`
 2. `flask run`
 
 ### Routes

| Route     | Scheme                                  |
|-----------|-----------------------------------------|
| Get Owner | `http://127.0.0.1:5000/din/<DIN NUMBER>`|
