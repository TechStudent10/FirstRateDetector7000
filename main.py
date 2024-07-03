import requests, json

# originally written by Prevter in JS, translated to Python by ~~me~~ chatgpt
def parse_key_map(key_map):
    keys_values = key_map.split(":")
    return {keys_values[i]: keys_values[i + 1] for i in range(0, len(keys_values), 2)}

def getAwardedLevels(page=0):
    headers = {
        "User-Agent": ""
    }

    data = {
        "secret": "Wmfd2893gb7",
        "type": 11,
        "page": page
    }

    res = requests.post("http://www.boomlings.com/database/getGJLevels21.php", data=data, headers=headers) \
            .text \
            .split("#")[0] \
            .split("|")

    levels = {}
    for level in res:
        level = parse_key_map(level)
        levels[level["1"]] = level

    return levels


awardedLevels = getAwardedLevels()
allLevels = {}
last_id = ""
with open("last_id.txt", "r") as f:
    last_id = f.read()

page = 0

while last_id not in awardedLevels:
    awardedLevels = getAwardedLevels(page)

    allLevels = allLevels | awardedLevels # merges them together

    page += 1

del allLevels[last_id]
print(json.dumps(allLevels, indent=4))
print(len(allLevels.keys()))
# TODO: remove all responses after the last_id. loop over all responses and check if that is the users first rate (by checking if the feature level of the level, so feature, epic, rate-only, etc., matches the amount of CP they have) and printing out the level data.
