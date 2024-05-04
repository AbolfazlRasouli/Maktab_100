
class Team:
    teams = {}

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.count_match = 0
        self.win = 0
        self.losses = 0
        self.egual = 0
        Team.teams[name] = self


    def update_score(self):
        self.score = self.win * 3 + self.egual



    def play_match(self, result) :
        
        self.count_match += 1
        if result == "win":
            self.win += 1
        elif result == "loss":
            self.losses += 1
        elif result == "egual":
            self.egual += 1
        print('The score was recorded')
        self.update_score()

    
    @classmethod
    def display_table(cls):
        sorted_teams = sorted(cls.teams.values(), key=lambda x: x.score, reverse=True)
        print(sorted_teams)
        if len(sorted_teams) == 0:
            print('There is no team')
        else :
            for team in sorted_teams:
                print(f"Team: {team.name}")
                print(f"Score: {team.score}")
                print(f"count_match: {team.count_match}")
                print(f"Wins: {team.win}")
                print(f"Losses: {team.losses}")
                print(f"Egual: {team.egual}")
    


while True:
    print("Main Menu:")
    print("1. Create Team")
    print("2. Enter Match Results")
    print("3. Display Table")
    print("4. Exit")
    choice = input("Enter your choice: ")
    print('-' * 50)


    if choice == '1':
        name = input("Enter team name: ")
        Team(name)
        print('-' * 50)


    elif choice == '2':
        team_name = input("Enter team name: ")
        result = input("Enter match result (win/loss/equal): ")
        if result in ['win', 'loss', 'egual']:
            try :
                Team.teams[team_name].play_match(result)
            except KeyError as e:
                print(f'Invalid team_name {e}')
            print('-' * 50)

        else:
            print("Invalid match result!")
            print('-' * 50)


    elif choice == '3':
        Team.display_table()
        print('-' * 50)

    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")









