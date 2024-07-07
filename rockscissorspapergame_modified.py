import random

print("게임을 시작합니다.")

option = ["가위", "바위", "보"]

def get_computer_choice():
    return random.choice(option)

def get_player_choice():
    while True:
        player_choice = input("가위, 바위, 보 중 하나를 입력하세요: ").strip()
        if player_choice in option:
            return player_choice
        else:
            print("입력이 올바르지 않습니다.")

def determine_winner(player_choice, computer_choice, win, lose, draw):
    if player_choice == computer_choice:
        draw += 1
        result = "무승부!"
    elif (
        (player_choice == "바위" and computer_choice == "가위")
        or (player_choice == "가위" and computer_choice == "보")
        or (player_choice == "보" and computer_choice == "바위")
    ):
        win += 1
        result = "이겼습니다!"
    else:
        lose += 1
        result = "졌습니다.."
    return result, win, lose, draw

def play_game(win, lose, draw):
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result, win, lose, draw = determine_winner(player_choice, computer_choice, win, lose, draw)
    print(f"나: {player_choice}, 컴퓨터: {computer_choice} \n{result}")
    return result, win, lose, draw

def main():
    win = 0
    lose = 0
    draw = 0

    while True:
        result, win, lose, draw = play_game(win, lose, draw)
        if result == "무승부!":
            print("한 판 더 진행합니다.")
            continue

        while True:
            play_again = input("한 판 더? (예/아니오): ").strip()
            if play_again in ["예", "ㅇ", "아니오", "ㄴ", "노"]:
                break
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")

        if play_again in ["아니오", "ㄴ", "노"]:
            break

    print("게임을 종료합니다!")
    print(f"결과: 승:{win}, 패:{lose}, 무승부:{draw}")

if __name__ == "__main__":
    main()
