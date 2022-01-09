def add_score(difficulty):
    points_of_wining = (difficulty*3)+5
    with open("/Users/chenshapira/PycharmProjects/WorldOfGames/scores.txt", "r") as f:
        s = f.readlines()[0]
        previous_score = int(s)
        # print(type(previous_score))
    with open("/Users/chenshapira/PycharmProjects/WorldOfGames/scores.txt", "w") as f:
        score = previous_score + points_of_wining
        f.write(str(score))
