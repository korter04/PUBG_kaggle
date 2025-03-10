# Feature Engineering
#%%
import pandas as pd

# 팀 플레이어수
def team_player(df):
    df['team_player']=df.groupId.map(df.groupId.value_counts())
    return df['team_player']

# 총 플레이어 수
def player(df):
    df['player']=df.matchId.map(df.matchId.value_counts())
    return df['player']

# 총 이동 거리
def total_distance(df):
    df['total_distance']=df['rideDistance']+df['swimDistance']+df['walkDistance']
    return df['total_distance']
  
def scaling(df, scaler, col_list):
    scaler = scaler
    temp = scaler.fit_transform(df.loc[:, col_list])
    for i in range(len(col_list)):
        df[col_list[i]] = temp[:,i]
    return df

# 컬럼 place화(등수 나열)
def columns_place(list, X, df):
    for i in list:
        X[i + 'Place'] = df.groupby('matchId')[i].rank(method='max', ascending = False)
    
    return X

# matchType 분류
def matchType_classify(df):
    def classify(x):
        if 'flare' in x or 'crash' in x or 'normal' in x:
            return 'event'
        elif 'solo' in x:
            return 'solo'
        elif 'duo' in x:            
            return 'duo'
        else:
            return 'squad'
    
    new_df = df
    new_df['matchType'] = df['matchType'].apply(classify)
    return new_df

# matchType encoding
def matchType_encoding(df):
    df_OHE = pd.get_dummies(df, columns=['matchType'])
    return df_OHE


# 그룹아이디에 따라 그룹화 및 컬럼 평균값 대입.
def columns_grouped_mean(list, X, df):   
    for i in list :
        X['group'+i] = df.groupby('groupId')[i].transform('mean')
        
    return X

def average_weaponsAcquired(df):
    df['average_weaponsAcquired'] = df.weaponsAcquired / (df.matchDuration / 60)
    return df['average_weaponsAcquired']

def average_damage(df):
    df['average_damage'] = df.damageDealt / (df.matchDuration / 60)
    return df['average_damage']

