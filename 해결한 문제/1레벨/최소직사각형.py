def solution(sizes):
    min_max_list = [ [] ,[]]

    for i in range( len(sizes) ):
        sizes[i] = sorted( sizes[i] )
        min_max_list[0].append( sizes[i][0] )
        min_max_list[1].append( sizes[i][1] )

    return max( min_max_list[0] ) * max( min_max_list[1] )

print( solution([[60, 50], [30, 70], [60, 30], [80, 40]]) )