#Question 4
'''
Consider that the human tower is to be performed on a stage
and the stage has a maximum weight limit.
Write a python program to find the maximum number of people
at the base level such that the total weight of tower does
not exceed the maximum weight limit of the stage.
Assume that:
1. Each person weighs 50 kg
2. There will always be odd number of men at the base level
of the human tower.
'''
def people(weight_of_stage):
        peep=1
        base=0
        while (peep*50)+base <= weight_of_stage:
                base+=peep*50
                peep+=2
        return peep-2

weight_of_stage=1000
print(people(weight_of_stage))
