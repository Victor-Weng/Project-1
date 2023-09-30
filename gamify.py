def get_cur_hedons():
    '''
    return number of hedons that the user has accumulated so far.
    '''
    return hedons

def get_cur_health():
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
        health_points+=3*min(activity_duration, 180)
        if (duration>180):
            health_points+=activity_duration-180
        # Set latest run or textbook time to current
        run_or_textbook_time=time

        if (is_tired):
            hedons += -2*duration
        else:
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
        else:
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
    star_offered = "none"
    time = 0
    star_time = 0
    run_or_textbook_time = 120 #> 120 so you start not tired
    is_bored = False
    return None

if __name__ == "__main__":
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) # resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute()) # running
    perform_activity("textbooks", 30)
    print(get_cur_health()) # 150 = 90 + 30*2

    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute()) # running
    perform_activity("textbooks", 30)
    print(get_cur_health()) # 150 = 90 + 30*2
    print(get_cur_hedons()) # -80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health()) # 210 = 150 + 20 * 3
    print(get_cur_hedons()) # -90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    ################################ I GOT DIFFERENT ANSWER. CAN YOU CHECK LOGIC?
    print(get_cur_health()) # 700 = 210 + 160 * 3 + 10 * 1
    ################################ I GOT DIFFERENT ANSWER. CAN YOU CHECK LOGIC?
    print(get_cur_hedons()) # -430 = -90 + 170 * (-2)
