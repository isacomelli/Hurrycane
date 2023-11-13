import os

class Ranking:
    def __init__(self):
        self.txt = f"{os.path.abspath('.')}\\Ranking.txt"
        self.ranking = self.read_ranking()

    def read_ranking(self):
        ranking = []
        with open(self.txt, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, score = line.strip().split(';')
                ranking.append((name, int(score)))

        ranking.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return ranking

    def write_ranking(self, username, final_score):
        with open(self.txt, 'a') as file:
            file.write(f'\n{username};{final_score}')
    
    def get_fifth_highest_score(self):
        sorted_data = sorted(self.ranking, key=lambda x: x[1], reverse=True)
        if len(sorted_data) >= 5:
            return sorted_data[4][1]
        else:
            return None
    