import os
import argparse

def create_files(lab, num):
    base_dir = os.getcwd()
    file_patterns = ["lab{}_{}.py", "test_lab{}_{}.py"]

    for i in range(1, num + 1):
        for pattern in file_patterns:
            file_name = pattern.format(lab, i)
            file_path = os.path.join(base_dir, file_name)

            if not os.path.exists(file_path):
                with open(file_path, "w") as file:
                    if pattern.startswith("lab"):
                        file.write("# Zadanie {}\n".format(i))
                    else:
                        file.write("# Testy - Zadanie {}\n".format(i))

    print("Files have been created.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create lab files.')
    parser.add_argument('lab', type=int, help='Lab number')
    parser.add_argument('--num', type=int, default=15, help='Number of files to create, default is 15')
    args = parser.parse_args()

    create_files(args.lab, args.num)
