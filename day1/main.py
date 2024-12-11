import sys

def main():
    lst1 = []
    lst2 = []
    with open("AOC1_input.txt", "r") as file:
        for line in file:
            a, b = map(int, line.split())
            lst1.append(a)
            lst2.append(b)
    lst1.sort()
    lst2.sort()
    print(lst1)
    print(lst2)

    differences = [abs(a - b) for a, b in zip(lst1, lst2)]

    result = sum(differences)
    print(result)

if __name__ == "__main__":
	main()
