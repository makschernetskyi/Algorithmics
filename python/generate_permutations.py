def generate_permutations(n):
    perms = [[1]]


    for i in range(2,n+1):
        new_perms = []
        for perm in perms:
            for j in range(0,len(perm)):
                new_perm = perm + [perm[j]]
                new_perm[j] = i
                new_perms.append(new_perm)
        perms = list(map(lambda perm: perm + [i],perms)) + new_perms

    return perms