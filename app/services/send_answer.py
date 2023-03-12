import requests
import json

def send_answer(TOKEN):
    TEXT = ""
    ID_QUESTION = ""
    NBR_ATTACK = ""
    
    if ID_QUESTION == "":
        ID_QUESTION = input("QUESTION_ID :\n> ")
    
    if TEXT == "":
        TEXT = input("WRITE SOMETHING :\n> ")
    
    if NBR_ATTACK == "":
        NBR_ATTACK = input("NUMBER OF ATTACK :\n> ")

    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    PAYLOAD = json.dumps({"text": TEXT})
    
    for _ in range(int(NBR_ATTACK)):
        requests.post(f"https://app.wooclap.com/api/questions/{ID_QUESTION}/push_answer", headers=HEADERS, data=PAYLOAD)
        print(f"\n'{TEXT}' IS SENDING...")
    