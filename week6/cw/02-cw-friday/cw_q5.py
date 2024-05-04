import random
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        return f'name{self.name},age {self.age}'


class FootballPlayer(Human):
    def __init__(self, name: str, age: int, performance_score: float or int, salary: float or int, position: str,
                 number: int):
        super().__init__(name, age)
        self.performance_score = performance_score
        self.salary = salary
        self.position = position
        self.number = number
        self.goalcount = 0

    def goal_score(self, goal):
        self.goalcount += goal


class Coach(Human):
    def __init__(self, name: str, age: int, salary: float, exprience: int):
        super().__init__(name, age)
        self.salary = salary
        self.exprience = exprience


class Team:

    def __init__(self, name: str, coach: Coach, score: int, balance: float):
        self.name = name
        self.captain = None
        self.players = []
        self.coach = coach
        self.score = score
        self.balance = balance

    def assign_captain(self, player: FootballPlayer):
        if player in self.players:
            self.captain = player
        else:
            return f'player{player}not in team,cant set captain out of team'

    def add_player(self, new_player: FootballPlayer):
        self.players.append(new_player)

    # def remove_player(self,player:FootballPlayer):
    #     if player in self.players:
    #         self.players.remove(player)
    #     else:
    #         raise Exception('player not in team!')
    def __delitem__(self, player: FootballPlayer):
        if player in self.players:
            self.players.remove(player)
        else:
            raise Exception('player not in team!')

    def display_players(self):
        # listdictplay (list(i.__dict__ for i in self.players))
        return self.players

    def has_enough_players(self):
        if len(self.players) == 11:
            return True
        return False

    def buy_player(self, player: FootballPlayer, teamforoshande, price: float):
        if price > self.balance:
            return f'cant afford'
        if player in teamforoshande.players:
            self.balance -= price
            teamforoshande.balance += price
            self.players.append(player)
            teamforoshande.players.remove(player)
            return "succecfully added"


class league:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, new_team: Team):
        self.teams.append(new_team)
        return f'team added to league{self.name}'

    def remove_team(self, removed_team):
        if removed_team in self.teams:
            self.teams.remove(removed_team)
            return f'team removed from league{self.name}'
        return f'team not in league{self.name}'

    @staticmethod
    def simulate_match(home: Team, away: Team, result: str):
        homeresult, awayresult = map(int, result.split('-'))

        if homeresult > awayresult:
            home.score += 3
        elif homeresult < awayresult:
            away.score += 3
        else:
            home.score += 1
            away.score += 1

    def standing(self):
        standingtable = (sorted(self.teams, key=lambda x: x.score, reverse=True))
        return standingtable
    def display_team_by_score(self):
        scoretable = (sorted(self.teams, key=lambda x: x.score, reverse=True))
        return scoretable
    def select_random_team(self):
        teamnames=self.teams
        selectedteam1=random.choice(teamnames)
        teamnames.remove(selectedteam1)
        selectedteam2=random.choice(teamnames)
        return f'{selectedteam1.name} and {selectedteam2.name} are matching'


p1 = FootballPlayer('mohammad', 31, 10.0, 50000, 'atack', 7)
p2 = FootballPlayer('mahdi', 30, 10.0, 50000, 'atack', 7)
p3 = FootballPlayer('mohammadreza', 29, 10.0, 50000, 'defence', 7)
p4 = FootballPlayer('mammadali', 30, 10.0, 50000, 'atack', 7)
p6 = FootballPlayer('mammadmahdio', 30, 10.0, 50000, 'goaler', 7)
p5 = FootballPlayer('mammadnazanin', 30, 10.0, 50000, 'atack', 7)

coach1 = Coach('zeidan', 54, 20000, 90)
barsa = Team('barsa', coach1, 0, 5)
barsa.add_player(p1)
barsa.add_player(p2)
barsa.add_player(p3)
barsa.add_player(p4)
barsa.add_player(p5)
barsa.add_player(p6)
barsa.assign_captain(p3)

display = barsa.display_players()
for i in display:
    print(i.__dict__)

p12 = FootballPlayer('mohammad', 31.0, 10.0, 50000, 'atack', 7)
p8 = FootballPlayer('mahdi', 30.0, 10.0, 50000, 'atack', 7)
p9 = FootballPlayer('mohammadreza', 29.0, 10.0, 50000, 'defence', 7)
p10 = FootballPlayer('mammadali', 30.0, 10.0, 50000, 'atack', 7)
p7 = FootballPlayer('mammadmahdio', 30.0, 10.0, 50000, 'goaler', 7)
p11 = FootballPlayer('mammadnazanin', 30.0, 10.0, 50000, 'atack', 7)

coach1 = Coach('zeidan2', 54, 20000, 90)
real = Team('real', coach1, 0, 2000)
real.add_player(p11)
real.add_player(p9)
real.add_player(p8)
real.add_player(p7)
real.add_player(p10)
real.add_player(p12)
real.assign_captain(p3)
print(real.buy_player(p2, barsa, 10))
display = barsa.display_players()
for i in display:
    print(i.__dict__)

laliga=league('laliga')
laliga.add_team(barsa)
laliga.add_team(real)
laliga.simulate_match(barsa,real,'3-4')
laliga.simulate_match(barsa,real,'5-2')
laligastanding=laliga.standing()#cleancode
for i in laligastanding:
    print(i.name,i.score)

for i,j in enumerate(laligastanding,1):
    print(f"{i}: {j.name} ,{j.score}")


p15 = FootballPlayer('mohammad', 31.0, 10.0, 50000, 'atack', 7)
p16 = FootballPlayer('mahdi', 30.0, 10.0, 50000, 'atack', 7)
p17 = FootballPlayer('mohammadreza', 29.0, 10.0, 50000, 'defence', 7)
p18 = FootballPlayer('mammadali', 30.0, 10.0, 50000, 'atack', 7)
p19= FootballPlayer('mammadmahdio', 30.0, 10.0, 50000, 'goaler', 7)
p20 = FootballPlayer('mammadnazanin', 30.0, 10.0, 50000, 'atack', 7)
coach1 = Coach('meysam', 54, 20000, 90)
perspolis = Team('perspolis', coach1, 0, 2000)
perspolis.add_player(p15)
perspolis.add_player(p16)
perspolis.add_player(p18)
perspolis.add_player(p17)
perspolis.add_player(p19)
perspolis.add_player(p20)
perspolis.assign_captain(p20)
laliga.add_team(perspolis)
print(laliga.select_random_team())