#%% import packages
import pandas as pd
import numpy as np

#%% interpret txt file as a DataFrame

rps_schema = pd.read_csv("C:/Users/Adam Hinthorne/Desktop/Advent2022Local/adventcode2022/2022_12_02/daytwo_input.txt",delim_whitespace=True)
rps_schema

#%%
### Opponent - A:ROCK, B:PAPER, C:SCISSORS
### Player - X:ROCK, Y:PAPER, Z:SCISSORS
### Scoring: W = 6, D = 3, L = 0, X = 1, Y = 2, Z = 3
### looking up a case statement in python, https://www.statology.org/case-statement-pandas/

rps_schema['result'] = np.where((rps_schema['Opponent']=='A') & (rps_schema['Player']=='Y'), 'W',
                        np.where((rps_schema['Opponent']=='B') & (rps_schema['Player']=='Z'), 'W',
                        np.where((rps_schema['Opponent']=='C') & (rps_schema['Player']=='X'), 'W',
                        np.where((rps_schema['Opponent']=='A') & (rps_schema['Player']=='X'), 'D',
                        np.where((rps_schema['Opponent']=='B') & (rps_schema['Player']=='Y'), 'D',
                        np.where((rps_schema['Opponent']=='C') & (rps_schema['Player']=='Z'), 'D','L'
                        ))))))

rps_schema['play_score'] = np.where(rps_schema['Player'] == 'Z',3,
                            np.where(rps_schema['Player'] == 'Y',2,
                            np.where(rps_schema['Player'] == 'X',1,0)))

rps_schema['result_score'] = np.where(rps_schema['result'] == 'W',6,
                                np.where(rps_schema['result'] == 'D',3,0))

rps_schema['total_score'] = rps_schema['play_score'] + rps_schema['result_score']

rps_schema

###checking some data figures to see if we are missing any data
#%%
##check size
np.shape(rps_schema)
##check results
rps_schema['result'].groupby(rps_schema['result']).count()
###check that all losses are scored 0
rps_schema[rps_schema['result'] == 'L']['result_score'].sum()
###check all results are scored properly
rps_schema[['result','result_score']].groupby(['result']).mean()

###check that all losses are resulted properly
rps_schema[rps_schema['result'] == 'L'].groupby(['Opponent','Player']).count()


###finding the total score of our game
# %%
rps_schema['total_score'].sum()

###13009 is our total score - correct!


###Part Two the strategy changes....
###Part Two: X: Lose, Y: Draw, Z: Win
### Now the "Player" column effectively doubles as a "Strategy" column

rps_schema['strategy_score'] = np.where(rps_schema['Player'] == 'Z',6,
                            np.where(rps_schema['Player'] == 'Y',3,0))

rps_schema['strategy_shape'] = np.where((rps_schema['Opponent']=='A') & (rps_schema['Player']=='Z'), 'B',
                        np.where((rps_schema['Opponent']=='B') & (rps_schema['Player']=='Z'), 'C',
                        np.where((rps_schema['Opponent']=='C') & (rps_schema['Player']=='Z'), 'A',
                        np.where((rps_schema['Opponent']=='A') & (rps_schema['Player']=='X'), 'C',
                        np.where((rps_schema['Opponent']=='B') & (rps_schema['Player']=='X'), 'A',
                        np.where((rps_schema['Opponent']=='C') & (rps_schema['Player']=='X'), 'B',rps_schema['Opponent']
                        ))))))

rps_schema['strategy_play_score'] = np.where(rps_schema['strategy_shape'] == 'C',3,
                            np.where(rps_schema['strategy_shape'] == 'B',2,
                            np.where(rps_schema['strategy_shape'] == 'A', 1, 0)))                       

rps_schema['total_strategy_score'] = rps_schema['strategy_score'] + rps_schema['strategy_play_score']

#%%
###checking we scored correctly

###strategy shapes are scored correctly
rps_schema[['strategy_shape','strategy_play_score']].groupby(['strategy_shape']).mean()

###strategy shapes match player strategy
rps_schema[['Opponent','Player','strategy_shape']].groupby(['Opponent','Player','strategy_shape']).count()

###finding our total strategy score of our game
# %%
rps_schema['total_strategy_score'].sum()

