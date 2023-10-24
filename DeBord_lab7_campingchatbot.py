##Camping chatbot##
def getReply (line, words):
    waters = ["pool", "ocean", "lake", "river", "pools", "oceans", "lakes", "rivers"]
    outdoors = ["mountain","greenway", "beach", "park", "mountains", "greenways", "beaches", "parks"]
    # find a reply based on the words
    reply = ""
    if len(words) == 0:
        reply = "You have to talk to me. "
    elif line[-1] == '?':
        reply =  "Why do you want to know? "
    elif "where" in words:
        reply = "What do you like to do? "
    elif "swim" in words:
        reply = "Do you like pools, the ocean, lakes, or rivers? "
    elif "hike" in words or "walk" in words:
        reply = "Do you like the mountains, greenways, beaches, or parks? "
    elif words[0] == "i" and words[1] == "feel":
        reply = "Why do you feel that way? "
    elif words[0] == "i" and words[1] == "think":
        reply = "Do you really think so? "
    if reply == "":
        for water in waters:
            if water in words:
                reply = "What else do you like to do? "
                break
    if reply == "":
        for place in outdoors:
            if place in words:
                reply = "What is favorite time? "
                break
    if reply == "":
        return "Tell me more."
    return reply

name = input("Hello. Welcome to Camp Counseling. What is your name? ")
print("Type quit any time you want to finish.")
line = input("Well " + name + ". What can we do for you today? ")

while line != "quit":
    line = line.lower()
    reply = getReply(line, line.split())
    line = input(reply)