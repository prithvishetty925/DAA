from collections import defaultdict
class Graph:
    def __init__(self, subjects):
        self.subjects, self.graph = subjects, defaultdict(list)
    def addedge(self, s1, s2):
        self.graph[s1].append(s2)
        self.graph[s2].append(s1)
    def coloring(self):
        cm, ac = {}, set(range(1, len(self.subjects) + 1))
        for i in self.subjects:
            uc = {cm[n] for n in self.graph[i] if n in cm}
            acolor = ac - uc
            cm[i]=min(acolor) if acolor else len(ac)+1
            ac.add(cm[i])
        return cm
    def timeslots(self):
        return max(self.coloring().values())
n = int(input("Enter the number of subjects: "))
sub, stu= [], {}
for i in range(n):
    subject = input(f"Enter subject {i + 1}: ")
    sub.append(subject)
    n_st = int(input(f"Enter the number of students for {subject}: "))
    st_list = [input(f"Enter student {j + 1} for {subject}: ") for j in range(n_st)]
    stu[subject] = st_list
g=Graph(sub)
for _ in range(int(input("Enter the number of edges: "))):
    e = input("Enter edge (subject1 subject2): ").split()
    g.addedge(e[0], e[1])
print(f"\nMinimum time slots needed: {g.timeslots()}")

/*OUTPUT

Enter the number of subjects: 4
Enter subject 1: MATHS
Enter the number of students for MATHS: 4
Enter student 1 for MATHS: SMITHA
Enter student 2 for MATHS: PRITHVI
Enter student 3 for MATHS: SANJANA
Enter student 4 for MATHS: ABHI
Enter subject 2: DAA
Enter the number of students for DAA: 2
Enter student 1 for DAA: SURABHI
Enter student 2 for DAA: RAKSHI
Enter subject 3: BIO
Enter the number of students for BIO: 3
Enter student 1 for BIO: KRITI
Enter student 2 for BIO: SONALI
Enter student 3 for BIO: ASHIKA
Enter subject 4: OS
Enter the number of students for OS: 4
Enter student 1 for OS: DEVIKA
Enter student 2 for OS: AISHU
Enter student 3 for OS: NISARGA
Enter student 4 for OS: SONIYA
Enter the number of edges: 4
Enter edge (subject1 subject2): MATHS DAA
Enter edge (subject1 subject2): DAA BIO
Enter edge (subject1 subject2): BIO OS
Enter edge (subject1 subject2): OS MATHS

Minimum time slots needed: 2  */
