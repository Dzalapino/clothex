TO SET UP:
It is recommended to set up python virtual environment with following command:

python -m venv myvenv

then activate with:

.\myenv\Scripts\activate

then install required packages with command:

pip install - r .\requirements.txt


OPTIONAL:
If you want to set up sample products and vendors databases (e.g. you do not have it or you accidentialy caused it to corrupt)to work with
you can use dedicated script with command:

python -m database_setup


TO RUN:
In order to run this API activate virtual environment with command:

.\myvenv\Scripts\activate

Then run API with:

uvicorn main:app --reload --port 8001

API will be available under address prompted out in the terminal -> just copy it and paste into 
browers (by specified command it is http://127.0.0.1:8001, but you can change it accoring to your needs), use <link>/docs to play with manually.


pssssst....!
your .env file should contain:
JWT_SECRET = "bardzosuperhipertajnyklucz"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1


and your credentials are:
login: your university login
passwords are: 
Summer 
or 
Outdoor


for mailing you need mailing.env file which cannot be shared here :D