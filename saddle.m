function indices = saddle(M)
    
    indices = [];           % pre-allocating a matrix to fill saddle points.
    n = 1;                  % This is the index value of number of saddle points.
    
    [row,cols] = size(M);
    
    row_max = max(M,[],2);           % Row matrix representing the maximum number from each row.
    col_min = min(M,[],1);                      % Row matrix representing the minimum from each coloumn. 
    
    for i = 1:1:row
        for j = 1:1:cols
            if((row_max(i,1) == M(i,j)) & (M(i,j) == col_min(1,j)))
                indices(n,1) = i;
                indices(n,2) = j;
                n = n+1;
            end
        end
    end
    
end
