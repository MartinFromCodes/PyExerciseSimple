#coding=utf-8
class Employ:
	'员工类'
	EmployCount=0;

	"""docstring for Employ"""
	def __init__(self, name,salary):
		 self.name=name;
		 self.salary=salary;
		 Employ.EmployCount+=1;

	def displayCount(self):
		print Employ.EmployCount;

	def displayEmploy(self):
		print "Name ",self.name,"Salary ",self.salary;

	def prts(self):
         print(self);
         print(self.__class__);
         
	
	

emp1=Employ("jack",2100);
emp2=Employ("tom",3100);
print Employ.EmployCount;
emp2.displayCount();
emp1.displayEmploy();
emp1.prts();
print "Employ.__doc__:", Employ.__doc__
print "Employ.__name__:", Employ.__name__
print "Employ.__module__:", Employ.__module__
print "Employ.__bases__:", Employ.__bases__
print "Employ.__dict__:", Employ.__dict__