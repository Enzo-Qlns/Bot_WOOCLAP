import requests
from components.core import generate_token


def get_answer():
    
    WOOCLAP_ID = ""
    TITLE = ""
    TOKEN = ""

    if WOOCLAP_ID == "":
        WOOCLAP_ID = input("WOOCLAP_ID ?\n> ")

    if TITLE == "":
        TITLE = input("TITLE QUESTION ? \n> ")

    if TOKEN == "":
        TOKEN = generate_token()
    
    URL = f"https://app.wooclap.com/api/events/{WOOCLAP_ID}"
    HEADERS = { 'Authorization': f'Bearer {TOKEN}' }

    RESPONSES = requests.get(URL, headers=HEADERS).json()
    QUESTIONS = RESPONSES["questions"]

    for i in range(1, len(QUESTIONS)):
        if (TITLE == QUESTIONS[i]["title"]):

            if (QUESTIONS[i]["__t"] == "GuessNumber"):
                CORRECT_ANSWER = QUESTIONS[i]["correctAnswer"]

            elif (QUESTIONS[i]["__t"] == "OpenQuestion"):
                CORRECT_ANSWER = QUESTIONS[i]["allExpectedAnswers"]
            
            elif (QUESTIONS[i]["__t"] == "MCQ"):
                for y in range(len(QUESTIONS[i]["choices"])):
                    if QUESTIONS[i]["choices"][y]["isCorrect"]:
                        CORRECT_ANSWER = QUESTIONS[i]["choices"][y]["choice"]

            elif (QUESTIONS[i]["__t"] == "FillInTheBlanks"):
                CORRECT_ANSWER = []
                for y in range(len(QUESTIONS[i]["choices"])):
                    CORRECT_ANSWER.append(QUESTIONS[i]["choices"][y]["text"])
          
    print(f"\n> GOOD ANSWER: {CORRECT_ANSWER}")