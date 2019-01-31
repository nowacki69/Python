def sort_artists(listOfTuples):
    all_artists = []
    revenue = []

    for items in listOfTuples:
        index = 0
        for info in items:
            if index == 0:
                all_artists.append(info)
            else:
                revenue.append(info)
            index += 1
    all_artists.sort()
    revenue.sort(reverse=True)
    
    sortedTuple = (all_artists, revenue)
    return sortedTuple
 
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))
