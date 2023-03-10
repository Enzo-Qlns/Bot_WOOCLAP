from services.add_users import add_users
from services.get_answer import get_answer
from services.send_answer import send_answer
from components.core import generate_token
from components.core import starter

# main page

starter(1)
print("\nATTACK (1) || GET_ANSWER (2) || SEND_ANSWER(WordCloud) (3)")

TOKEN = generate_token()
WANT = ""

if WANT == "":
    WANT = input("\nWhat do you choose ? \n> ")

while (int(WANT) != 1 and int(WANT) != 2 and int(WANT) != 3):
    WANT = input("\nWhat do you choose ? \n> ")


match int(WANT):
    case 1:
        add_users(TOKEN)

    case 2: 
        get_answer(TOKEN)

    case 3:
        send_answer(TOKEN)

print("\nBYE!")