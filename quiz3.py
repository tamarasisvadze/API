import requests
import json
import sqlite3


r = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations')
print(r.status_code)

# requests modulis metodebi

#print(r.text)
# print(r.headers)
#print(r.url)

#json failis dict tipad gardaqmna da failshi shenaxva

res = r.json()
#easy_js = json.dumps(res, indent=4)

#with open('corona_jsonFile.json', 'w') as f:
    #f.write(easy_js)

# informaciis wamogheba Canadaze

#country = res['locations'][47]
#easy_js = json.dumps(res['locations'][47], indent=4)

#with open('Canada_data.json', 'w') as f:
    #f.write(easy_js)


#DB-s sheqmna

conn = sqlite3.connect('canada_covid_db.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS covidInCanada 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        country VARCHAR(20),
        country_code VARCHAR(10),
        population INTEGER,
        confirmed INTEGER,
        deaths INTEGER,
        recovered INTEGER
        )''')

rows = []

for each in res['locations']:
    country = each['country']
    country_code = each['country_code']
    population = each['country_population']
    confirmed = each['latest']['confirmed']
    deaths = each['latest']['deaths']
    recovered = each['latest']['recovered']
    row = (country, country_code, population, confirmed, deaths,recovered)

rows.append(row)

#print(rows)
cur.executemany('INSERT INTO covidInCanada (country, country_code, population,confirmed, deaths,recovered) VALUES (?, ?, ?, ?, ?, ?)', rows)

conn.commit()







