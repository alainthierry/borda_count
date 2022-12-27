import pandas as pd
from collections import defaultdict

def borda_count_method(df, considered_columns = ['Accuracy', 'Precision', 'Recall', 'F1-Score']):
    """
    Implementation of borda count voting method. The first column of the dataframe must be the models' names
    The borda count voting method score is based on the metrics, columns in *considered_columns*
    
    Arg(s):
        df(DataFrame):The dataframe that contains the models to be ranked
        considered_columns(list):columns, metrics to be used for ranking.
    Return(s):
        DataFrame:The ranked models and their Borda count scores.

    """
    columns = df.columns
    
    num_voters = len(considered_columns)
    num_candidates = len(df[columns[0]])
    scores = defaultdict(int)
    
    df_voting = df[considered_columns]
    for i in range(num_candidates):
        for j in range(num_voters):
            
            scores[df[columns[0]][i]] +=df_voting.iloc[i, j]

    ranking = sorted(scores.items(), key=lambda i: i[1], reverse=True)
    return pd.DataFrame(data=ranking, columns=[columns[0], 'Borda_count_score'])

if __name__ == '__main__':
	df = pd.read_excel("ANFIS_DIABETES_ENS_SINGLES.xlsx",sheet_name="Sheet9")
	print(borda_count_method(df))