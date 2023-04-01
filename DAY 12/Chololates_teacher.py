child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates(chocolates_received):
    s=0
    s=sum(chocolates_received)
    print("Number of Chocolates =",s)

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates<1:
        print("Extra chocolates is less than one")
    elif child_id_rewarded not in child_id:
        print("Invalid Id")
    else:
        i=child_id.index(child_id_rewarded)
        chocolates_received[i]+=extra_chocolates
        
    
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
calculate_total_chocolates(chocolates_received)
reward_child(20,3)
calculate_total_chocolates(chocolates_received)
