
from app import create_app
app = create_app()

@app.route("/")
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True,port=81)