from flask import Flask, request, Response, render_template
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
            f.writelines(json.dumps(webhook) + "\n")

        return Response(status=200)

    except Exception as e:
        print(e)
        return Response(status=403)

@app.route('/get', methods=['GET'])
def read():
    try:
        lines = None
        # with open(FILE, 'r') as f:
        #     lines = f.readlines()

        lines = [
            {"version": "0.1", "sharedSecret": "", "sentAt": "2021-04-19T16:10:12.595753Z", "organizationId": "811478", "organizationName": "James Earl - original", "organizationUrl": "https://n146.meraki.com/o/2APjxb/manage/organization/overview", "networkId": "L_645140646620825042", "networkName": "Home", "networkUrl": "https://n146.meraki.com/Home-appliance/n/pHbVWdsc/manage/nodes/wired_status", "networkTags": [], "deviceSerial": "Q2FY-2CZG-UDZG", "deviceMac": "2c:3f:0b:b5:da:15", "deviceName": "Don S Davis", "deviceUrl": "https://n146.meraki.com/Home-appliance/n/pHbVWdsc/manage/nodes/new_wired_status", "deviceTags": [], "deviceModel": "MX67", "alertId": "", "alertType": "Power supply went down", "alertTypeId": "power_supply_down", "alertLevel": "critical", "occurredAt": "2021-04-19T16:10:12.594180Z", "alertData": {}},
            {"version": "0.1", "sharedSecret": "", "sentAt": "2021-04-19T16:10:31.286884Z", "organizationId": "811478", "organizationName": "James Earl - original", "organizationUrl": "https://n146.meraki.com/o/2APjxb/manage/organization/overview", "networkId": "L_645140646620825042", "networkName": "Home", "networkUrl": "https://n146.meraki.com/Home-appliance/n/pHbVWdsc/manage/nodes/wired_status", "networkTags": [], "deviceSerial": "Q2FY-2CZG-UDZG", "deviceMac": "2c:3f:0b:b5:da:15", "deviceName": "Don S Davis", "deviceUrl": "https://n146.meraki.com/Home-appliance/n/pHbVWdsc/manage/nodes/new_wired_status", "deviceTags": [], "deviceModel": "MX67", "alertId": "", "alertType": "Power supply went down", "alertTypeId": "power_supply_down", "alertLevel": "critical", "occurredAt": "2021-04-19T16:10:30.980006Z", "alertData": {}}
        ]
        
        response = []
        for line in lines:

            # line_json = json.load(line)
            response.append(str(json.dumps(line, sort_keys = False, indent = 2)))
        
        response.reverse()
        return render_template('get.html', webhooks=response)

        # return response


    except Exception as e:
        print(e)
        return "unable to read webhooks"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)