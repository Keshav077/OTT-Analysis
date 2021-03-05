from termcolor import colored


class HandlingMissingValues:
    def __init__(self, df):
        self.df = df

    def showDataSetInfo(self):
        print(colored("There are {} rows and {} columns in the data set.".format(self.df.shape[0], self.df.shape[1]),
                      attrs=['bold']))
        print("Columns:")
        for i in self.df.columns:
            print(i)

    def showMissingDataPercentage(self):
        for i in self.df.columns:
            null_rate = self.df[i].isna().sum() / len(self.df) * 100
            if null_rate > 0:
                print("{}'s null rate :{}%".format(i, round(null_rate, 2)))

    def handleMissingValues(self, columns):
        self.df = self.df.drop(columns=columns)
        self.df = self.df.fillna(value={'country': 'United States', 'cast': 'No Data'})
        self.df = self.df.dropna()
