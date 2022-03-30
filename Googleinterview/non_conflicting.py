def findNonConflictingJobsLength(jobs):
    jobs.sort(key=lambda x: x[0])
    #Sorted List based on starting time
    print(jobs)

    L = []
    L = [0] * len(jobs)
    d= {}
    for i in range(len(jobs)):
        print("XXX")
        for j in range(i):
            if jobs[j][1] <= jobs[i][0] :
                print(jobs[i])
                d[jobs[i][0]]= jobs[i] 
                L[i] = L[j]
        L[i]=L[i] + 1            
    print(L)    
    print(d)
                    





if __name__ == '__main__':
 
    # Each pair stores the start and the finish time of a job
    jobs = [
        (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (7, 9),
        (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)
    ]
 
    print('The maximum number of non-conflicting jobs is',findNonConflictingJobsLength(jobs))