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
    global star_offered, star_time, time, is_bored # set the star_offered variable to the activity that corresponds with it
    temp = [] # used to shift star_time array down
    
    if (activity == "running"): 
        star_offered = "running"
        # running thing
    elif (activity == "textbooks"):
        star_offered = "textbooks"
        # thing
    elif (activity == "resting"):
        star_offered = "resting"
        # thing
    
    temp = star_time

    star_time[0] = temp[1]
    star_time[1] = temp[2]
    star_time[2] = time

    if (time-star_time[0]) < 120:
        is_bored = True

def perform_activity(activity, duration):
    '''
    '''
    global health_points, hedons, star_offered, time, star_time, run_or_textbook_time, is_bored
    # Local boolean is tired if less than 2 hours since last finishing running/textbook
    is_tired = run_or_textbook_time-time < 120

    # Progressing time (So that time accessed throughout function is time at end of activity)
    time+=duration

    if star_can_be_taken(activity) and not is_bored:
        if duration >= 10:
            hedons+=30
        elif duration < 10:
            hedons+=3*duration

    if (activity == "running"):
        # Adding health from run
        health_points+=3*min(duration, 180)
        if (duration>180):
            health_points+=duration-180
        # Set latest run or textbook time to current
        run_or_textbook_time=time

        if (is_tired):
            hedons += -2*duration
        else:
            if duration<=10:
                hedons += 2*duration
            elif duration>10:
                hedons += 20-(2*(duration-10))
        # running thing
    elif (activity == "textbooks"):
        health_points+=2*duration

        # Set latest run or textbook time to current
        run_or_textbook_time=time

        if (is_tired):
            hedons += -2*duration
        else:
            if duration<=20:
                hedons += duration
            elif duration>20:
                hedons += 20-(2*(duration-20))

    elif (activity == "resting"):
        pass
    else:
        print("Activity is not valid")
    
    # Because the star only works for the next action, otherwise, it expires.
    star_offered = "Star Expired"

    return None

def most_fun_activity_minute():
    '''
    Return activity ("resting", "running", "textbooks") that gives the most
    hedons if person performed it for one minute at the current time
    '''
    global is_bored, star_offered, run_or_textbook_time, time

    res_score = 0
    run_score = 0
    tex_score = 0
    is_tired = run_or_textbook_time-time < 120

    if (not is_bored) and (star_offered != "Star Expired"):
        if star_offered == "resting":
            res_score+=0
            pass
        elif star_offered == "running":
            run_score+=3
            pass
        elif star_offered == "textbooks":
            tex_score+=3
            
    if (not is_tired):
        res_score += 0
        run_score += 2
        tex_score += 1
    elif (star_offered == "resting"):
        run_score -= 2
        tex_score -= 2
    elif (star_offered == "running"):
        run_score += 0
        tex_score -= 2
    elif (star_offered == "textbooks"):
        run_score -= 2
        tex_score += 0

    activity_array = ["resting", "running", "textbooks"]
    score_array = [res_score, run_score, tex_score]

    return activity_array[score_array.index(max(score_array))]
    # return the activity in the index in score_array with the max (highest) score

def star_can_be_taken(activity):
    '''
    return true iff star can be taken for current activity
    If no time passed between the star’s being offered and the activity, and the user is not bored with
    stars, and the star was offered for activity activity.
    '''
    global star_offered # activity that was offered by the star

    if (activity == star_offered) and (not is_bored):
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
    star_time = [-120,-120,-120]
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
