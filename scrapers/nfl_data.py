import pandas as pd
import nfl_data_py as nfl

# get list of columns to scrape
cols = nfl.see_pbp_cols()

# get list of games
print(cols[["home_team", "away_team"]])
# for item in cols:
#     print(item)
# print(nfl.import_combine_data("2020-2021", "WR"))
