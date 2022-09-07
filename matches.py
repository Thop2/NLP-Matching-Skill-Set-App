from get_pairings import run

def pair():
    num = input("Enter how many people you would like to pair off: ")
    num = int(num)
    names = []
    knows = []
    wants = []
    for i in range(num):
        student_num = str(i + 1)
        student_name = input("Enter the name of employee " + student_num + ": ")
        names.append(student_name)
        know = input("Enter one or more sentences describing " + student_name + "'s skillset: ")
        knows.append(know)
        want = input("Enter one or more sentences describing " + student_name + "'s desired skillset: ")
        wants.append(want)
    pairs = run(knows, wants, names)
    print("Here are the pairings:")
    for i in range(len(pairs)):
        print(str(i + 1) + ": " + str(pairs[i][0]) + " and " + str(pairs[i][1]))

if __name__ == '__main__':
    pair()
