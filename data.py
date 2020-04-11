from json import load

with open("headlines.json", "r") as f:
    headlines = load(f)

with open("dates.json", "r") as f:
    dates = load(f)

with open("pred.json", "r") as f:
    pred_json = load(f)

with open("real.json", "r") as f:
    real_json = load(f)

for data in [headlines, dates, pred_json, real_json]:
    data.reverse()

predicted, actual = ([{"date": d, "val": v} for d, v in zip(dates, vals)] for vals in (pred_json, real_json))

