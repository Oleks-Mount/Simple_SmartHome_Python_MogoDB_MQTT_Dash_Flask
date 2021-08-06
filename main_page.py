import json
import  paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import smtplib, ssl

broker_address = '169.254.5.221'
mqtt_client  = mqtt.Client("P1")
mqtt_client.connect(broker_address)
mqtt_client.loop_start()



def write_data(message):
    new_data = dict(message)
    print(new_data)
    water_leakage = new_data['water']


def on_message_problems(client,userdata,message):
    on_data = str(message.payload.decode("utf-8"))
    data = json.loads(on_data)
    water_leakage = data['water']
    #print(water_leakage)
    if water_leakage == 1:
        client_email = 'ooleksiienko1@gmail.com'
        company_email = 'olleksii112@gmail.com'
        password_company_email = 'mountkante'
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.login(client_email, password_company_email)
            subject = 'Небезпека затоплення'
            body = 'Перекрийте воду'
            name_feedback = 'SmartHome'
            msg = f'Subject: {subject}\n\n{name_feedback}\n\n{body}'.encode('utf-8')

            server.sendmail(client_email, company_email, msg)

subscribe.callback(on_message_problems, '/test', hostname= broker_address)

mqtt_client.loop_stop()








