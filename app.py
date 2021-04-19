from flask import Flask, request, Response

FILE = "webhooks.log"

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    try: 
        webhook = request.json
        with open(FILE, 'a') as f:
            f.writelines(webhook)

        return Response(status=200)

    except:
        return Response(status=403)

@app.route('/read', methods=['GET'])
def read():
    try:
        with open(FILE, 'r') as f:
            lines = f.readlines()
            return lines

    except:
        return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)