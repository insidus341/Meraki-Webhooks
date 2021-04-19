from flask import Flask, request, Response
from pathlib import Path
import json

FILE = "/app/logs/webhooks.log"

# Create the logs folder if it doesn't exist
Path("/app/logs").mkdir(parents=True, exist_ok=True)


app = Flask(__name__)

@app.route('/post', methods=['POST'])
def respond():
    try: 
        webhook = request.json
        print(webhook)
        with open(FILE, 'a') as f:
            f.writelines(json.dumps(webhook))

        return Response(status=200)

    except Exception as e:
        print(e)
        return Response(status=403)

@app.route('/get', methods=['GET'])
def read():
    try:
        with open(FILE, 'r') as f:
            lines = f.readlines()
            return lines

    except Exception as e:
        print(e)
        return "unable to read webhooks"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)