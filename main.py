from graph import Graph
import pandas as pd
def createGraph():
    df = pd.read_csv("synonyms.csv")
    adj_list = Graph()

    #Drop the first 275 rows since the data is numeric and not words
    df = df.iloc[275:]

    for index,row in df.iterrows():
        to = row["lemma"]
        try:
            seperate = str(row["synonyms"]).split("|")
        except Exception as e:
            print(e)
            print(row["synonyms"])
            continue
        words=[]
        for word in seperate:
            words.extend(word.split(";"))
        for word in words:
            adj_list.insertEdge(to,word)
    return adj_list
