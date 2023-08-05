from graph import Graph
import pandas as pd
#This function when called will create a graph object, intilize it with the data from synonyms.csv, and return a object
def createGraph():
    #Dataframe to read the data
    df = pd.read_csv("synonyms.csv")
    #Create graph object
    adj_list = Graph()

    #Drop the first 275 rows since the data is numeric and not words
    df = df.iloc[275:]

    #Iterate through each row in the dataframe
    for index,row in df.iterrows():
        #This is the word which we find the synonyms
        to = row["lemma"]
        #Now try to seperate the synonyms words by first the | character
        try:
            seperate = str(row["synonyms"]).split("|")
        except Exception as e:
            continue
        #Get the list of synonyms by splitting using the ; character
        words=[]
        for word in seperate:
            words.extend(word.split(";"))

        #insert a directed edge where the synonym is adjacent to the word
        for word in words:
            #To prevent self loop since a word can not be a synonym of itself
            if word!=to:
                adj_list.insertEdge(to,word)
    return adj_list
