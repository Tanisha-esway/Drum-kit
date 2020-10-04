def Ludecomposition(A):
    n=len(A);
    L=[];
    for i in range(n):
        B=[];
        for j in range(n):
            if i==j:
                B.append(1);
            else:
                B.append(0);
        L.append(B);
    # L=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]];
    for i in range(n):
        for j in range(i+1,n):
            mult=-A[j][i]/A[i][i];
            L[j][i]=-mult;
            for k in range(n):
                A[j][k]=A[i][k]*mult+A[j][k];
    u=[[A[j][i] for i in range(n)] for j in range(n)];

    return L,A,u;


if __name__=="__main__":
    size1=int(input("Enter the size of N*N matrix"));
    A=[];
    for i in range(size1):
        A.append(list(map(int,list((input("Enter the {i+1} row").split())))));
    print(A);
    L,B,U=Ludecomposition(A);
    print("L=\n");
    for item in L:
        print(item);
    print("U=\n");
    for item in U:
        print(item);
    print(A);