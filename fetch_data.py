import json
import urllib2
import codecs

channels = ["fumao.word.live", "fumao.tw"]
dates = ["2014-03-2" + str(x) for x in range(4)]

base_url = "http://logbot.g0v.tw/channel/%s/%s/json"

data = []

for chan in channels:
    for date in dates:
        url = base_url % (chan, date)
        json_data = urllib2.urlopen(url).read()
        data.extend(json.loads(json_data))


outfile = codecs.open("Data/all.json", "w", "utf8")
json.dump(data, outfile, ensure_ascii=False, encoding='utf-8')
outfile.close()
