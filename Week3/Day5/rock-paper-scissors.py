from game import Game

def get_user_menu_choice():
    while True:
        user_choice = input("Enter 'P' to play a new game, 'S' to show scores, or 'Q' to quit: ").upper()
        if user_choice in ['P', 'S', 'Q']:
            return user_choice
        else:
            print("Invalid input. Please try again.")

def print_results(results):
    print("Thank you for playing!")
    print(f"Results: Win - {results['win']}, Loss - {results['loss']}, Draw - {results['draw']}")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'P':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == 'S':
            print_results(results)
        elif choice == 'Q':
            print_results(results)
            break

if __name__ == '__main__':
    main()
