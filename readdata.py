def read_data(file_route):
    people_dict = {}
    project_dict = {}

    file1 = open(file_route, 'r')

    number_line = file1.readline()

    number_list = number_line.split(" ")

    for people_number in range(int(number_list[0])):
        people_list = file1.readline().split(" ")
        people_dict[people_list[0]] = {}
        for skill_number in range(int(people_list[1])):
            skill_info = file1.readline().split(" ")
            people_dict[people_list[0]][skill_info[0]] = int(skill_info[1])

    for people_number in range(int(number_list[1])):
        project_list = file1.readline().split(" ")
        project_dict[project_list[0]] = {}
        project_dict[project_list[0]]["rolls"] = {}
        project_dict[project_list[0]]["complete_dates"] = int(project_list[1])
        project_dict[project_list[0]]["score"] = int(project_list[2])
        project_dict[project_list[0]]["best_before"] = int(project_list[3])

        for req_skill_number in range(int(project_list[4])):
            req_skill_list = file1.readline().split(" ")
            project_dict[project_list[0]]["rolls"][req_skill_list[0]] = int(req_skill_list[1])

    return people_dict, project_dict


if __name__ == '__main__':
    ppl, prl = read_data(r"./input_data/a_an_example.in.txt")
    print(ppl)
    print(prl)
