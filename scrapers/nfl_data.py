import pandas as pd
import nfl_data_py as nfl

# get list of columns to scrape
cols = nfl.see_pbp_cols()
# gets play by play data for a 2021-2022 season
pbp = nfl.import_pbp_data([2020, 2021], ["qb_epa", "xpass"])
# get list of games
# print(cols)
# for item in cols:
#     print(item)
# print(nfl.import_combine_data("2020-2021", "WR"))
weekly = nfl.import_weekly_data([2021])

descs = nfl.import_team_desc()

print(pbp)
