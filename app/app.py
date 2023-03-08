from services.attack import attack
from services.get_answer import get_answer
from services.send_answer import send_answer
from components.core import starter

print("\nATTACK (1) || GET_ANSWER (2) || SEND_ANSWER(WordCloud) (3)")

WANT = ""
if WANT == "":
    WANT = input("\nWhat do you choose ? \n> ")

while (int(WANT) != 1 and int(WANT) != 2 and int(WANT) != 3):
    WANT = input("\nWhat do you choose ? \n> ")

if int(WANT) == 1:
    attack()

elif int(WANT) == 2:
    get_answer()

elif int(WANT) == 3:
    send_answer()

print("\nDONE!")