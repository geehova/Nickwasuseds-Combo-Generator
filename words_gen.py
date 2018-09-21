from pandas import read_html, DataFrame, concat
import json

colors = read_html('https://simple.wikipedia.org/wiki/List_of_colors')[0][0][1:]
countries = read_html('https://simple.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')[0][1][3:].str.replace(" ", "")
years = DataFrame([str(x) for x in range(1940, 2020)])
animals = read_html('https://en.wikipedia.org/wiki/Chinese_zodiac')[4][5][2:]
frames = [colors, countries, years, animals]
result = concat(frames)
result.dropna(inplace=True)

with open('words.json', 'w') as outfile:
    json.dump(result[0].tolist(), outfile)