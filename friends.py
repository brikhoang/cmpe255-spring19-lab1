users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    return len(user["friends"])

def sort_by_num_friends(friends_totals):
    '''README.md
    Sort from "most friends" to "least friends"
    '''    
    return sorted(friends_totals, key=lambda id: id[1], reverse = True)
    
    
def main():
    for user in users:
        user ["friends"] = []
    
    for x, y in friendship:
        users[x]["friends"].append(users[y])
        users[y]["friends"].append(users[x])

    friends_totals = [(user["id"], num_friends(user))
                     for user in users]
    
    #print(friends_totals)
    print(sort_by_num_friends(friends_totals))
          
if __name__ == "__main__":
    main()

