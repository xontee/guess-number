import random

def get_guess():
    # """Запрашивает у пользователя число, пока он не введёт корректное."""
    while True: #бесконечный цикл
        value = input("Введи число: ")
        if value.isdigit():  #  возвращает True, если строка состоит только из цифр.
            return int(value)
        print (f"{value} не число!")

def play_game():
   
    secret=random.randint(1, 100) #Случайное целое от 0 -100
    attemps = 0
    print(f"Я загадал число от 1 до 100.")
    while True:
        guess=get_guess()
        attemps +=1
        if guess< secret:
            print(f"твое число меньше")
        elif guess> secret:
            print(f"твое число больше")
        else: 
            print(f"Ты угадал количество попыток {attemps}")
            return attemps


def main():
    # """Точка входа. Запускает игру и спрашивает, играть ли снова."""
    print("Добро пожаловать в игру «Угадай число»!")
    while True:
        play_game()
        answer= input("Сыграть ещё? (да/нет): ").strip().lower()
        if answer not in ["да", "д", "yes", "y"]:
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
