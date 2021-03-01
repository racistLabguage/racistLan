import json

try:
    # JSON data fetched with API requests
    with open("outputs/output4.json") as json_file:
        data = json.load(json_file)

    # Path to the output file
    f = open("outputs/formattedData2.txt", "a")
    for x in data:

        try:
            #print(x["retweeted_status"])
            if x["retweeted_status"]["truncated"]:
                f.write(str(x["retweeted_status"]['id']) + ',' +
                        x["retweeted_status"]["extended_tweet"]["full_text"] + "\n")
        except KeyError:
            if x["truncated"]:
                f.write(str(x['id']) + ',' + x["extended_tweet"]["full_text"] + "\n")
            else:
                f.write(str(x['id']) + ',' + x['text'] + "\n")

    f.close()
except ValueError:
    print('Decoding JSON has failed')


    #f = open("outputs/formattedData.txt", "a")
    #for x in data:
    #    f.write(str(x['id']) + ',' + x['text'] + "\n")
    #f.close()