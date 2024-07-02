import random


def up_down_game():
    return random.randint(1, 100)


total_attempts = []

print("UpDown 게임을 시작합니다.")

while True:
    attempts = 0
    game_number = up_down_game()

    while True:
        try:
            guess_number = int(input("1에서 100 사이의 숫자를 입력하세요: "))

            if guess_number < 1 or guess_number > 100:
                print("숫자가 1에서 100 사이에 있지 않습니다.")
                continue

            attempts += 1

            if guess_number < game_number:
                print("UP")
            elif guess_number > game_number:
                print("DOWN")
            else:
                print(f"정답입니다! {attempts}번 만에 정답을 맞히셨습니다!")
                total_attempts.append(attempts)
                break

        except ValueError:
            print("숫자가 아닙니다.")

    end_question = input("게임을 계속 하고 싶으면 y, 종료하고 싶으면 n 을 입력하세요: ").strip().lower()
    if end_question == 'n':
        break
    elif end_question != 'y':
        print("잘못된 입력입니다. 게임을 종료합니다.")
        break

    if total_attempts:
        last_attempt = total_attempts[-1]
        print(f"전 라운드 시도 횟수: {last_attempt}번! 이번 라운드도 화이팅입니다!")

if total_attempts:
    last_attempt = total_attempts[-1]
    print(f"마지막 라운드 시도 횟수: {last_attempt}번! 다음에 또 만나요!")
