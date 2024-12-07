# Nardos Gebremedhin
# 12/5/24

import json


def class_list_output(class_list):
    for entry in class_list:
        print(f"{entry['F_Name']}, {entry['L_Name']}: ID = {entry['Student_ID']}, Email = {entry['Email']}")


def main():
    file_path = 'C:\csd\csd-325\module-8\studentjson.txt'

    # Output notification to the user that this is the original Student list.
    print("Original Student List ")

    with open(file_path, 'r') as file:
        class_list = json.load(file)

    # Call your print function
    class_list_output(class_list)

    new_student = {
        "F_Name": "Nardos",
        "L_Name": "Gebremedhin",
        "Student_ID": 44445,
        "Email": "fakeemail@gmail.com"
    }
    class_list.append(new_student)

    # Output notification to the user that this is the updated Student list.
    print("\nUpdated Student List:")

    # Call your print function.
    class_list_output(class_list)

    # Use the JSON dump() function to append the new data to the .json file.
    with open(file_path, 'w') as file:
        json.dump(class_list, file, indent=4)

    # Output notification to the user that the .json file was updated.
    print("\nThe .json file has been updated with the new student info.")


if __name__ == '__main__':
    main()
