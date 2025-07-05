from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hook():
    print(request)
    print(request.data)
    return "hello world"

if __name__ == "__main__":
    app.run()
