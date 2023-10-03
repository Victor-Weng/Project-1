import math

def get_cur_health():
    global health
    return health

def get_cur_hedons():
    global hedons
    return hedons

def offer_star(activity):
    global latest_star_value, time, prev_star_time, prev_prev_star_time, is_bored
    latest_star_value=activity
    if (time-prev_prev_star_time<120):
        is_bored=True
    else:
        prev_prev_star_time, prev_star_time = prev_star_time, time


def perform_activity(activity, duration):
    global health, hedons, time, latest_star_value, prev_run_duration, prev_text_duration, prev_run_text_time
    print(prev_run_duration)

    # Health gain for running
    run_health_before=3
    run_health_after=1
    run_health_limit=180

    # Hedon gain for running (non tired)
    run_hedons_before=2
    run_hedons_after=-2
    run_hedons_limit=10

    # Hedon gain for running (tired)
    run_hedons_tired=-2

    # Health gain for textbook
    text_health = 2

    # Hedon gain for textbook (non tired)
    text_hedons_before=1
    text_hedons_after=-1
    text_hedons_limit=20

    # Hedon gain for textbook (tired)
    text_hedons_tired=-2

    # Hedon gain for star
    star_hedons_before=3
    star_hedons_after=0
    star_hedons_limit=10
    
    
    is_tired = (time-prev_run_text_time)<120

    if (activity=="running"):
        if (is_tired):
            health+=calculate_value(run_health_before, run_health_after, max(run_health_limit-prev_run_duration,0), duration)
            hedons+=run_hedons_tired*duration
        else:
            health+=calculate_value(run_health_before, run_health_after, max(run_health_limit-prev_run_duration,0), duration)
            hedons+=calculate_value(run_hedons_before, run_hedons_after, max(run_hedons_limit-prev_run_duration,0), duration)
        prev_run_text_time=time+duration
        prev_run_duration+=duration
        prev_text_duration=0
    elif (activity=="textbooks"):
        if (is_tired):
            health+=text_health*duration
            hedons+=text_hedons_tired*duration
        else:
            health+=text_health*duration
            hedons+=calculate_value(text_hedons_before, text_hedons_after, max(text_hedons_limit-prev_text_duration,0), duration)
        prev_run_text_time=time+duration
        prev_run_duration=0
        prev_text_duration+=duration
    elif (activity=="resting"):
        prev_run_duration=0
        prev_text_duration=0    
    if (star_can_be_taken(activity)):
        hedons+=calculate_value(star_hedons_before, star_hedons_after, star_hedons_limit, duration)

    time+=duration

    latest_star_value="" #Resets after action

def star_can_be_taken(activity):
    global is_bored, latest_star_value

    if (activity==latest_star_value and not is_bored):
        return True
    else:
        return False
    
    


def most_fun_activity_minute():
    global is_bored, latest_star_value, prev_run_text_time, time

    res_score = 0
    run_score = 0
    tex_score = 0
    is_tired = time-prev_run_text_time < 120

    if (not is_bored) and (latest_star_value != ""):
        if latest_star_value == "resting":
            res_score+=0
            pass
        elif latest_star_value == "running":
            run_score+=3
            pass
        elif latest_star_value == "textbooks":
            tex_score+=3
            
    if (not is_tired):
        res_score += 0
        run_score += 2
        tex_score += 1
    elif (latest_star_value == "resting"):
        run_score -= 2
        tex_score -= 2
    elif (latest_star_value == "running"):
        run_score += 0
        tex_score -= 2
    elif (latest_star_value == "textbooks"):
        run_score -= 2
        tex_score += 0

    activity_array = ["resting", "running", "textbooks"]
    score_array = [res_score, run_score, tex_score]

    return activity_array[score_array.index(max(score_array))]
    # return the activity in the index in score_array with the max (highest) score


def initialize():
    global health, hedons, time, is_tired, is_bored, latest_star_value, prev_star_time, prev_prev_star_time, prev_run_text_time, prev_run_duration, prev_text_duration
    health, hedons = 0, 0
    time=0
    is_bored=False
    is_tired=False
    latest_star_value=""
    prev_star_time=-math.inf
    prev_prev_star_time=-math.inf
    prev_run_text_time=-math.inf
    prev_run_duration, prev_text_duration = 0,0
def calculate_value(before_speed, after_speed, limit, duration):
    if duration>limit:
        return (before_speed*limit)+(after_speed*(duration-limit))
    else:
        return before_speed*duration

if __name__=="__main__":

    initialize()
    perform_activity("running", 100)
    perform_activity("running", 100)
    perform_activity("running", 200)
    print(get_cur_hedons())
    print(get_cur_health())