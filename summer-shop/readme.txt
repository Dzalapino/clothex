to install dependencies, use the following command in the root directory of the project:
pip install -r requirements.txt

to run web api, use the following command in the root directory of the project:
uvicorn main:app --host 127.0.0.1 --port 9000

to install frontend dependencies, use the following command in the frontend directory:
npm install

to run frontend, use the following command in the frontend directory:
npm run dev -- --open

to run tests use the following command in the root directory of the project:
python -m pytest