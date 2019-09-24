import re
import os

def regex_tutorial():
    data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "part1", "headlines.txt")
    file = open(data_dir, 'r')
    regexp = re.compile(r"(?P<last>[-a-zA-Z]+),"
                        r" (?P<first>[-a-zA-Z]+)"
                        r"( (?P<middle>([-a-zA-Z]+)))?"
                        r": (?P<phone>(\(\d{3}-)?\d{3}-\d{4})"
                       )
    firstname, middlename, lastname, phonenumber = None, None, None, None
    for line in file.readlines():
        result = regexp.search(line)
        if result == None:
            print("Oops, I don't think this is a record")
        else:
            lastname = result.group('last')
            firstname = result.group('first')
            middlename = result.group('middle')
            if middlename == None:
                      middlename = ""
            phonenumber = result.group('phone')
        print('Name:', firstname, middlename, lastname,' Number:', phonenumber)
    file.close()




if __name__ == "__main__":
    regex_tutorial()