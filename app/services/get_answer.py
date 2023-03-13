import requests

def get_answer(TOKEN):
    
    WOOCLAP_ID = ""
    QUESTIONTITLE = ""

    if WOOCLAP_ID == "":
        WOOCLAP_ID = input("WOOCLAP_ID ?\n> ")

    if QUESTIONTITLE == "":
        QUESTIONTITLE = input("QUESTIONTITLE QUESTION ? \n> ")

    URL = f"https://app.wooclap.com/api/events/{WOOCLAP_ID}"
    HEADERS = { 'Authorization': f'Bearer {TOKEN}' }

    RESPONSES = requests.get(URL, headers=HEADERS).json()
    QUESTIONS = RESPONSES["questions"]

    for i in range(1, len(QUESTIONS)):
        if (QUESTIONTITLE == QUESTIONS[i]["QUESTIONtitle"]):

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