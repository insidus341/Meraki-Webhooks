from flask import Flask, request, Response
from pathlib import Path

FILE = "/logs/webhooks.log"

# Create the logs folder if it doesn't exist
Path("/logs").mkdir(parents=True, exist_ok=True)


app = Flask(__name__)

@app.route('/post', methods=['POST'])
def respond():
    try: 
        webhook = request.json
        print(webhook)
        with open(FILE, 'a') as f:
            f.writelines(webhook)

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
        return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)