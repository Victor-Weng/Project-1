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
    global star_offered, star_time, time # set the star_offered variable to the activity that corresponds with it
    if (activity == "running"): 
        star_offered = "running"
        # running thing
    elif (activity == "textbooks"):
        star_offered = "textbooks"
        # thing
    elif (activity == "resting"):
        star_offered = "resting"
        # thing
    star_time = time

def perform_activity(activity, duration):
    '''
    '''
    global health_points, hedons, star_offered, time, star_time, run_or_textbook_time, is_bored

    # Local boolean is tired if less than 2 hours since last finishing running/textbook
    is_tired = run_or_textbook_time-time < 120


    # Progressing time (So that time accessed throughout function is time at end of activity)
    time+=duration


    activity_duration=duration
    if (activity == "running"):
        # Adding health from run
        health_points+=min(3*activity_duration, 180)
        if (time>180):
            health_points+=activity_duration-180
        # Set latest run or textbook time to current
        run_or_textbook_time=time

        if (is_tired and not star_offered=="running"):
            hedons += -2*duration
        elif (not is_tired and not star_offered=="running"):
            if duration<=10:
                hedons += 2*duration
            elif duration>10:
                hedons += 20-(2*(duration-10))
        if (star_offered=="running"):
            hedons+=3*min(duration, 10)
        # running thing
    elif (activity == "textbooks"):
        health_points+=2*activity_duration

        # Set latest run or textbook time to current
        run_or_textbook_time=time

        if (is_tired):
            hedons += -2*duration
        elif (not is_tired):
            if duration<=20:
                hedons += duration
            elif duration>20:
                hedons += 20-(2*(duration-20))
        if (star_offered=="textbooks"):
            hedons+=3*min(duration, 10)
    elif (activity == "resting"):
        if (star_offered=="resting"):
            hedons+=3*min(duration, 10)
    else:
        print("Activity is not valid")
    
    # Because the star only works for the next action, otherwise, it expires.
    star_offered = "Star Expired"

    
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

    if (activity == star_offered) and (star_time == time) and (not is_bored):
        return True
    else:
        return False

def initialize():
    '''
    Initialize global variables
    '''
    global health_points, hedons, star_offered, time, star_time, run_or_textbook_time, is_bored
    health_points = 0
    hedons = 0
    star_offered = "running"
    time = 0
    star_time = 0
    run_or_textbook_time = 0
    is_bored = False
    return None

if __name__ == "__main__":
    initialize()
    # Simulation 1