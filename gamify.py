def cur_hedons():
    '''
    return number of hedons that the user has accumulated so far.
    '''
    return hedons

def cur_health():
    '''
    return number of health points that the user has accumulated so far.
    '''
    return health_points

def offer_star(activity):
    '''
    Set star_offered variable to 0, 1, or 2 to indicate the offered activity
    '''
    if (activity == "running"): 
        star_offered = 0
        # running thing
    elif (activity == "textbooks"):
        star_offered = 1
        # thing
    elif (activity == "resting"):
        star_offered = 2
        # thing

def perform_activity(activity, duration):
    time=duration
    if (activity == "running"): 
        pass
        # running thing
    elif (activity == "textbooks"):
        pass
        # thing
    elif (activity == "resting"):
        pass
        # thing
    else:
        print("Activity is not valid")
    return None

def most_fun_activity_minute():
    return None

def initialize():
    '''
    Initialize global variables
    '''
    global health_points, hedons, star_offered
    health_points = 0
    hedons = 0
    star_offered = 0 # running = 0, textbooks = 1, resting = 2
    return None

if __name__ == "__main__":
    initialize()
    # Simulation 1
    initialize()
    # Simulation 2
    # hehe
    pass