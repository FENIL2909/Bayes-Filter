actions = ['do_nothing','do_nothing','push','do_nothing','push','do_nothing']  # given list of actions
measurements = ['closed','closed','closed','closed','open','open'] # given list of measurements

#### intial belief that the door is open and closed is 0.5 as the robot lacks the knowledge of state of the door at the beggining ####
bel_open = 0.5
bel_closed = 0.5

print('initial bel_open:' + str(bel_open))
print('initial bel_closed:' + str(bel_closed))



#### initializing all the measurement probabilities ####
def measurement_probability(measurement,state):
    if (measurement == 'open') and (state == 'open'):
        prob = 0.6
    elif (measurement == 'closed') and (state == 'open'):
        prob = 0.4
    elif (measurement == 'open') and (state == 'closed'):
        prob = 0.2
    elif (measurement == 'closed') and (state == 'closed'):
        prob = 0.8
    return prob


#### initializing all the action probabilities ####
def action_probability(next_state,action,state):
    if (next_state == 'open') and (action == 'push') and (state == 'open'):
        prob = 1
    elif (next_state == 'closed') and (action == 'push') and (state == 'open'):
        prob = 0
    elif (next_state == 'open') and (action == 'push') and (state == 'closed'):
        prob = 0.8
    elif (next_state == 'closed') and (action == 'push') and (state == 'closed'):
        prob = 0.2
    elif (next_state == 'open') and (action == 'do_nothing') and (state == 'open'):
        prob = 1
    elif (next_state == 'closed') and (action == 'do_nothing') and (state == 'open'):
        prob = 0
    elif (next_state == 'open') and (action == 'do_nothing') and (state == 'closed'):
        prob = 0
    elif (next_state == 'closed') and (action == 'do_nothing') and (state == 'closed'):
        prob = 1
    return prob



#### function definition for action step and calculation bel_bar ####
def action_step(action, prev_bel_open, prev_bel_closed):
    bel_open = action_probability('open',action,'open')*(prev_bel_open) + action_probability('open',action,'closed')*(prev_bel_closed)
    bel_closed = action_probability('closed', action, 'open') * (prev_bel_open) + action_probability('closed', action,'closed') * (prev_bel_closed)
    return bel_open, bel_closed


#### function definition for measurement step and calculation bel ####
def measurement_step(measurement, bel_open_bar, bel_closed_bar):
    temp_bel_open = measurement_probability(measurement,'open')*(bel_open_bar)
    temp_bel_closed = measurement_probability(measurement, 'closed') * (bel_closed_bar)
    bel_open = temp_bel_open/(temp_bel_closed+temp_bel_open)
    bel_closed = temp_bel_closed/(temp_bel_closed+temp_bel_open)
    return bel_open, bel_closed


##### final Bayes Filter Implementation #####
for i in range(len(actions)):
    print('')
    bel_open_bar, bel_closed_bar = action_step(actions[i], bel_open, bel_closed)
    print('%%%%%%%%%%%%%%%%% Iteration_No:' + str(i + 1) + ' %%%%%%%%%%%%%%%%%')
    print('bel_open_bar:' + str(bel_open_bar))
    print('bel_closed_bar:' + str(bel_closed_bar))
    bel_open, bel_closed = measurement_step(measurements[i], bel_open_bar, bel_closed_bar)

    print('------------')
    print('bel_open:' + str(bel_open))
    print('bel_closed:' + str(bel_closed))







