from douglas.department import department
from douglas.faculty import faculty
from createData import postData
def main():
    #d = department("https://www.douglascollege.ca/programs-courses/catalogue/programs")
    teachers= faculty("https://www.douglascollege.ca/programs-courses/faculties/commerce-business-administration/computing-studies-and-information-systems/faculty")
    data = teachers.parse()
    postData(data).post()
if __name__=="__main__":
    main()