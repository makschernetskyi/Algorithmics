def get_LU_decomposition(m: np.ndarray):
    n = m.shape[0]

    if len(m.shape) > 2:
        raise Exception("Given array does not represent a matrix")

    if not all(map(lambda s: s == n, m.shape)):
        raise Exception("Given matrix is not square")

    # after decomposition

    l = np.zeros((n, n), dtype=sp.Rational)  # lower triangular matrix
    u = np.zeros((n, n), dtype=sp.Rational)  # upper triangular matrix

    for j in range(n):
        u[0][j] = m[0][j]

    for i in range(1, n):
        l[i][0] = sp.Rational(m[i][0], u[0][0])

    for i in range(1, n):


        for j in range(1, i):

            if abs(u[j][j]) <= 10**(-8):
                raise Exception("Danger of division by zero encountered")

            l[i][j] = sp.Rational((m[i][j] - np.dot(l[i, :j], u[:j, j])), u[j][j])

        for j in range(i, n):
            u[i][j] = m[i][j] - np.dot(l[i, :i], u[:i, j])

        l[i, i] = 1


    return l, u