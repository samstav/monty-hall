import random
import time

def play(firstchoice, switch):
    goats = [1,2,3]
    options = [1,2,3]
    not_car_not_firstchoice = [1,2,3]
    car = random.randint(1,3)
    not_car_not_firstchoice.remove(car)
    if car != firstchoice:
        not_car_not_firstchoice.remove(firstchoice)
    #print "car: %s" % car
    #print "firstchoice: %s" % firstchoice
    goats.remove(car)
    options.remove(firstchoice)
    if firstchoice == car:
        hint = random.choice(goats)
    else:
        hint = random.choice(not_car_not_firstchoice)
        options.remove(hint)
    #print "HINT: Door %s is a goat" % (hint)
    secondchoice = firstchoice if not switch else options[0]
    #print "secondchoice: %s" % secondchoice
    if secondchoice == car:
        #print "WIN"
        #print "-----------------------"
        return True
    else:
        #print "goat fucker"
        #print "-----------------------"
        return False


if __name__ == '__main__':
    wins = 0
    losses = 0
    total = 10000000
    for x in range(total):
        firstchoice = random.randint(1,3)
        #switch = random.randint(0,1)
        switch = True
        #print "\n"
        #print "-----------------------"
        outcome = play(firstchoice, switch)
        if outcome:
            wins += 1
        else:
            losses += 1
    successrate = float(float(wins)/float(total))
    print "successrate: %s" % successrate
