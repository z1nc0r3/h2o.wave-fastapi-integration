## H2O Wave + FastAPI Integration (Testing)


## Running the app

### 1. Clone the repository:

``` bash
git clone https://github.com/z1nc0r3/Car-Price-Predictor-using-H2O-wave
```

### 2. Create a virtual environment:

``` bash
python3 -m venv venv
```

### 3. Activate the virtual environment:
``` bash
source venv/bin/activate
```

**windows**
``` bash
venv\Scripts\activate.bat
```
To deactivate the virtual environment use ```deactivate``` command.

### 4. Install dependencies:

``` bash
(venv) pip3 install -r requirements.txt 
```

### 5. Run the app:
``` bash
(venv) wave run app
```

### 6. View the app:
Point your favorite web browser to http://localhost:10101/predictor


### 7. Test API endpoints
```curl --location 'http://0.0.0.0:8008/health'```

