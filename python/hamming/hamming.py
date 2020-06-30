def distance(strand_a, strand_b):
    length_a = len(strand_a)
    length_b = len(strand_b)

    distance = 0

    if length_a != length_b:
        raise ValueError('Tamanhos diferentes')

    else:
        count = 0

        for item in strand_a:
            if strand_b[count] != item:
                distance += 1
            
            count += 1

    return distance
