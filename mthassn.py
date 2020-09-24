
def transpose(A):
    #returns the transpose of a matrix A
    m=len(A)
    n=len(A[0])
    B = [[0 for x in range(m)] for y in range(n)]
    for i in range(n): 
        for j in range(m): 
            B[i][j] = A[j][i]
    return B 

def multiply(X,Y):
    #returns the product of matrices X and Y= X.Y
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

def generate_ColumnVectors(A):
    #returns the matrix in column major form
    return transpose(A)

def sc_multiply(c,v):
    #returns the scalar multiplication of a scalar c and vector v
    w=v[:]
    for i in range(len(v)):
        w[i]=c*v[i]
    return w

def dot_prod(v1,v2):
    #returns the dot product of vectors v1 and v2
    n=len(v1)
    vsum=0
    for i in range(n):
        vsum+=v1[i]*v2[i]
    return vsum

def projection(v1,v2):
    #returns projection of vector v1 on v2
    proj= sc_multiply(dot_prod(v1,v2)/dot_prod(v2,v2),v2)
    return proj

def subtract(v1,v2):
    #returns the subtraction of vector v2 from v1
    vsub=[]
    for i in range(len(v1)):
        vsub.append(v1[i]-v2[i])
    return vsub

def add(v1,v2):
    #returns the addition of vectors v1 and v2
    vadd=[]
    for i in range(len(v1)):
        vadd.append(v1[i]+v2[i])
    return vadd

def value(v):
    #returns the magnitude of vector v
    mag=0
    for i in range(len(v)):
        mag+=v[i]**2
    mag=mag**0.5
    return mag

def QR_factorize(A):
    #prints the matrices Q and R generated by the factorization of A[A=QR]
    A_col=generate_ColumnVectors(A)
    m=len(A)
    n=len(A[0])
    Q=A_col
    Q[0]=normalise(Q[0])
    for i in range(1,n):
        for j in range(i):
            d_p=dot_prod(A_col[i],Q[j])
            s_m=sc_multiply(d_p,Q[j])
            Q[i]=subtract(Q[i],s_m)
            Q[i]=normalise(Q[i])
    Q=transpose(Q)
    R=multiply(transpose(Q),A)
    
    print('Q:')
    for i in Q:
        print(i)

    print('R:')
    for j in R:
        print(j)

    
def normalise(v):
    #returns the unit vector in the direction of v
    mag=value(v)
    for i in range(len(v)):
        v[i]=v[i]/mag
    return v

# =============================================================================
m=int(input('Enter number of rows:'))
n=int(input('Enter number of columns:'))
print('Enter entries of the matrix in row major form:')
A=[]
for i in range(m): 
     a =[]
     for j in range(n): 
         print('Enter entry',(i+1,j+1),':',end='')
         a.append(int(input()))
     A.append(a)

QR_factorize(A)
 
# =============================================================================
