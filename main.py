import requests, json
""" Mode of transport can be fastest, shortest, pedestrian, bicycle """

""" By Deafult - mode of transport is fastest """

def mainfunc(from_val=" " , to_val= " ", mode_transport = "fastest"):

    url = f"https://www.mapquestapi.com/directions/v2/route?key=UbH7DkjS05mBLP5lrTcqEiAGtsvq7tA6&from={from_val}&to={to_val}&outFormat=json&ambiguities=ignore&routeType={mode_transport}&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false"
    r = requests.get(url)
    result =(r.json())

    try:

        distance = result['route']['distance']
        print(distance)
        print("\n")
        
        blank_text=  " "
        blank_text += "distance is  "+str(distance) +" KMs."
        blank_text += "\n"

        narratives = (result['route']['legs'][0]["maneuvers"])

        for row in narratives:
            blank_text+= (row['narrative'])
            blank_text+="\n"

        return blank_text


    except Exception as e:
        err = ("Please check your locations or, the way you sent your messages, NOTICE that the messages have to sent in the fashion of ORIGIN to DESTINATION \n")
        return err
