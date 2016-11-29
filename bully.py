def highest():
    high = 0
    ind = 0
    m = 0
    if m < num:
        if id[m] > high:
           if crash[m] == 0:
               high = id[m]
               ind = m
    return ind

def election(pro):
    newid = id.index('pro')
    q = newid + 1
    while q <= num:
        if id[newid] < id[q]:
            print "Election message sent to process with ID" + id[q] + "by process with ID" + id[newid]
        if crash[q] == 0 and id[newid] < id[q]:
            print "OK message received from Process with ID" + id[q]
        elif crash[q] == 1 and id[newid] < id[q]:
            print "Process with ID" + id[q] + "is not alive anymore"
            newid = newid + 1
            print "Processs with ID" + id[newid] + "is taking over the process"
        q = q + 1
    leaderr = newid - 1
    print "New elected leader is process with ID" + id[leaderr]

def crash():
    x = input("Enter id of process you want to crash:")
    crashind = id.index('x')
    crash[crashind] = 1
    print "Process with ID" + x + "has been crashed"
    i = 0
    while n <= num:
        if crash[n] == 0:
            print "Process with ID" + id[n] + "is alive"
        else:
            print "Process with ID" + id[n] + "is dead"
    if x == leader:
        newpro = input("Enter Process ID which should start the election:")
        election(newpro)

def rejuvenate():
    rejpro = input("Enter Process ID to be rejuvenated:")
    rej = id.index('rejpro')
    crash[rej] = 0
    election(rejpro)
    
def bully():
    leader = highest()
    print "Process witb ID" + leader + "is the leader. All Hail !!"
    p = input("Enter 1 to Crash; 2 to Rejuvenate; and 3 to Exit:")
    if p == 1:
        crash()
        return
    elif p == 2:
        rejuvenate()
    elif p == 3:
        return
    else:
        return
        
            
            

def main():
    global num
    id=[]
    crash=[]
    num = input("Enter number of processes:")
    while len(id) <= num :
        processid = input("Enter Process ID from low to high priority:")
        id.append(processid)
        crash.append(0)
    bully()
    
if __name__ == '__main__':
    main()