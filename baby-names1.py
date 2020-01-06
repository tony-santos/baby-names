import pandas as pd

names1880 = pd.read_csv('~/git-repos/baby-names/data/names/yob1880.txt')

years = range(1880, 2019)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = '~/git-repos/baby-names/data/names/yob%d.txt' % year
    #print(path)
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)
    names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_births