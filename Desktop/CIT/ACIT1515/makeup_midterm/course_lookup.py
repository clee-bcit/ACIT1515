# Chris Chanwoo Lee
# ACIT1515 - SET B
# A01016225

"""Get a course ID and return the course title and semster 

Hints:
    Logical and: https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/5/section/5?content_resource_id=53222676
    Conditional Statement and Membership operator: in - https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/5/section/9?content_resource_id=49219380
    Dictionary index and retrival -  https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/8/section/12  
"""

from typing import Tuple

CIT_COURSES = {
    "ACIT1420": ("Introduction to System Admin", 1),
    "ACIT1515": ("Scripting for IT", 1),
    "ACIT1620": ("Fundamental Web Technologies", 1),
    "ACIT1630": ("Database Systems", 1),
    "COMM1116": ("Business Communications 1", 1),
    "MATH1310": ("Technical Math for IT", 1),
    "ORGB1100": ("Organizational Behaviour", 1),
    "ACIT2420": ("Linux System Administration", 2),
    "ACIT2515": ("Object Oriented Programming", 2),
    "ACIT2520": ("Developing Web Applications", 2),
    "ACIT2620": ("Principles of Enterprise Networking", 2),
    "ACIT2831": ("Business Systems Analysis", 2),
    "COMM2216": ("Business Communications 2", 2),
    "MATH1350": ("Statistics for IT", 2),
    "ACIT2811": ("UX/UI Development", 2.5),
    "ACIT2911": ("Agile Development Project", 2.5),
    "ACIT4770": ("Legal and Ethical Issues in IT", 2.5),
    "ACIT3420": ("Windows Server Administration", 3),
    "ACIT3475": ("Web Server Administration", 3),
    "ACIT3640": ("Cloud Computing", 3),
    "ACIT3771": ("IT Service & Project Mgmt", 3),
    "ACIT3896": ("Applied Algorithms", 3),
    "ACIT3900": ("Industry Projects for IT", 3),
    "ACIT3910": ("Database Structure and Mgmt", 3),
    "ACIT3495": ("Advanced Topics in IT Infrastructure", 4),
    "ACIT3855": ("Service Oriented Architectures", 4),
    "ACIT4630": ("Information Assurance and Security", 4),
    "ACIT4640": ("IT System and Network Provisioning", 4),
    "ACIT4850": ("Enterprise System Integration", 4),
    "ACIT4880": ("Introduction to Data Analytics", 4),
    "ACIT4900": ("IT Project Practicum 2", 4),
}


# Add course_lookup function, the docstring is below
"""This function looks up the course id returning the course title and its term

Valid course ID's are made of 4 letters and 4 digits, e.g. ACIT1630

if the course id is invalid,
    the title is an error message set to: {course_id} is an invalid course ID
    the semster is set to 0

if the course id is offered in the CIT program:
    the title is set to: {course_id}: {course_title} runs in semster {semester}
    the semster is set to 0

If the course id is not offered in the CIT program:
    the title is an error message set to: {course_id} is not a CIT course
    the semster is set to 0

Args:
    course_id (str): the course ID to lookup, must be in the form AAAANNNN
                        where AAAA indicates a capital letter and
                        NNNN represents a number

Returns:
    Tuple[str, float]: The string course title or error message, and the
                        semster the course runs or 0

Examples:
    >>> course_lookup('CMP370')
    ('CMP370 is an invalid course ID', 0)

    >>> course_lookup('ACIT1515')
    ('Scripting for IT', 1)

    >>> course_lookup('ACIT4640')
    ('IT System and Network Provisioning', 4)

    >>> course_lookup('COMP1516')
    ('COMP1516 is not a CIT course', 0)

"""
def course_lookup(course_id):
    letter = course_id[0:4]
    number = course_id[4:7]
    semester = 0
    title = 'error'
    if len(course_id) == 8:
        if letter.isalpha() and number.isdigit():
            if course_id not in CIT_COURSES:
                print(course_id, 'is not a CIT course,', semester)
            elif course_id in CIT_COURSES:
                semester = CIT_COURSES[course_id][1]
                title = course_id
                print(CIT_COURSES[course_id])
    else:
        print(course_id, 'is an invalid course ID,', semester)

    return (title, semester)

def main():
    """Get course ID from the user and print the course title and semster

    If course isn't in CIT or is invalid, print the error message
    """

    course_id = input("Please enter course ID: ").upper().replace(" ", "")
    title, semester = course_lookup(course_id)

    # Add logic to output the appropriate user message
    #
    # if the course is a CIT course display
    #    {course_id}: {title} runs in semester {semester}
    # if the course isn't a CIT course or the course ID is invalid
    #   the error message returned from course_lookup


if __name__ == "__main__":
    main()

