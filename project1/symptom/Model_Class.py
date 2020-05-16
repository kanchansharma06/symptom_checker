from typing import Any


class Modeldiag():
    def __init__(self, name,icd,pname):
        ## private varibale or property in Python
        self.__name = name
        self.__icd = icd
        self.__pname = pname

    def get_name(self):
        return self.__name

    def get_icd(self):
        return self.__icd

    def get_pname(self):
        return self.__pname

class Modelissue():
    def __init__(self, synonyms,medicalcondition,treatmentdescription) :
        ## private varibale or property in Python
        self.__synonyms = synonyms
        self.__medicalcondition = medicalcondition

        self.__treatmentdescription= treatmentdescription

    def get_synonyms(self):
        return self.__synonyms
    def get_medicalcondition (self):
        return self.___medicalcondition

    def get_treatmentdescription(self):
        return self.__treatmentdescription


class Modeldat():
    def __init__(self, id,name):
        ## private varibale or property in Python
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

