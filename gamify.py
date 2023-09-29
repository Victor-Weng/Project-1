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
    global star_offered # set the star_offered variable to the activity that corresponds with it
    if (activity == "running"): 
        star_offered = "running"
        # running thing
    elif (activity == "textbooks"):
        star_offered = "textbooks"
        # thing
    elif (activity == "resting"):
        star_offered = "resting"
        # thing

def perform_activity(activity, duration):
    '''
    '''
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
    '''
    '''
    return None

def star_can_be_taken(activity):
    '''
    return true iff star can be taken for current activity
    If no time passed between the star’s being offered and the activity, and the user is not bored with
    stars, and the star was offered for activity activity.
    '''
    global star_offered # activity that was offered by the star

    if (activity == star_offered) and ()
    else:
        return False

def initialize():
    '''
    Initialize global variables
    '''
    global health_points, hedons, star_offered, current_activity, time, star_time
    health_points = 0
    hedons = 0
    star_offered = "running"
    time = 0
    star_time = 0
    return None

if __name__ == "__main__":
    initialize()
    # Simulation 1
    initialize()
    # Simulation 2
    pass