
#project {ProjectName : [people]
project = {}
for work in project.keys():
    isSatisfied = False
    poplist = {}
    while (not isSatisfied):
        for people in peoples.keys():
            workNeedthispeople,skillname = workNeedthispeople(work[roles],people[skills])
            if workNeedthispeople:
                person = peopels.pop(people)
                poplist[person[0]] = person[1]
                work[roles].pop(skillname)
                if not work[roles]:
                    isSatisfied = True
                    project[work] = poplist.keys()
                    project.pop()

        people += roles
        break



#return needOrNot,skiilname.
def workNeedthispeople(workrequirement:dict,skills:dict):
    for skill in skills.keys():
        if workrequirement.contains(skill) and workrequirement[skill] < skills[skill]:
            return True,skill
    return False,None







