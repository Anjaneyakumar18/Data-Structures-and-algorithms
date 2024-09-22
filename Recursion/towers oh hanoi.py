def TowerOfHanoi(source, Destination, Helper, n):
    if n == 1:
        print(f'Moving disk {n} from {source} to {Destination}')
        return
    
    TowerOfHanoi(source, Helper, Destination, n - 1)
    print(f'Moving disk {n} from {source} to {Destination}')
    TowerOfHanoi(Helper, Destination, source, n - 1)

TowerOfHanoi('A', 'C', 'B', 3)
