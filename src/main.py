from flask import Flask
name = 'dowolna_APKA'
app = Flask(name)

@app.route("/")
def hello():
    return "JESTEM I DZIALAM 2\n"

if __name__=="__main__":
    app.run(host="0.0.0.0")
