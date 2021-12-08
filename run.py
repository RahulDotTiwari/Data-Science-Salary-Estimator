import glassdoor_scraper as gs
import pandas as pd

path='C:\\Users\\rahul\\Desktop\\MP\\drivers\\chromedriver.exe'
df = gs.get_jobs('data scientists', 15, False, path, 10)
df.to_csv("glassdoor_jobs.csv", index=False)

df.columns