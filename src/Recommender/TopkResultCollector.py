class TopkResultCollector:
    def __init__(self):
        self.total_cases = 0
        self.recommendation_made =0
        self.recommendation_not_made =0
        self.top1=0
        self.top3=0
        self.top5=0
        self.top10=0
        self.top100=0
        self.top1000 = 0
        self.top10000=0

    def add(self, correct_site, list_recommendations):
        self.total_cases = self.total_cases + 1
        if len(list_recommendations) == 0:
            self.recommendation_not_made = self.recommendation_not_made + 1
        else:
            self.recommendation_made = self.recommendation_made + 1
            rank = -1
            found = False
            for i in range(len(list_recommendations)):
                if list_recommendations[i] == correct_site:
                    rank = i
                    found = True
                    break
            if found is True:
                if (rank == 0):
                    self.top1 = self.top1 + 1
                if rank < 3:
                    self.top3 = self.top3 + 1
                if rank < 5:
                    self.top5 = self.top5 + 1
                if rank < 10:
                    self.top10 = self.top10 + 1
                if rank < 100:
                    self.top100 = self.top100 + 1
                if rank < 1000:
                    self.top1000 = self.top1000 + 1
                if rank < 10000:
                    self.top10000 = self.top10000 + 1

    def print(self):
        print("Total Test Cases: {} Recommendation Made: {} Recommendation Not Made: {}".format(self.total_cases,self.recommendation_made,self.recommendation_not_made))
        print("Top1: {} Top3: {} Top5: {} Top10:{} Top100:{} Top1000: {} Top10000:{}".format(self.top1,self.top3,self.top5,self.top10,self.top100,self.top1000,self.top10000))

rc = TopkResultCollector()
rc.print()