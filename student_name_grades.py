continue_program = "y"
while continue_program == "y":
    student_name = input("Enter Your name: ")
    print("Enter Your grades in 3 subjects: ")
    grade1 = int(input())
    grade2 = int(input())
    grade3 = int(input())
    array = [grade1, grade2, grade3]

    average = round((grade1 + grade2 + grade3 / 3))
    arr = []
    if 0 < average <= 100:
        arr.append(student_name)
        arr.append(array)
        arr.append(average)
        print(arr)
        continue_program = input("Do you want to continue? ('y/n)")
        if continue_program == "y":
            continue
