# Password-Set-Generator
A Python script that generates a list of all possible combinations with a given length of a set of given characters

For example, with the inputs:  
_character_set = [a, b, c]  
length = 2_

It outputs:  
_aa  
ab  
ac  
ba  
bb  
bc  
ca  
cb  
cc_

> **Initialisation:**  

pws = PasswordList(character_set (_required_), length (_required_))  
**character_set** - list of valid characters  
**length** - length of passwords to be generated  


> **pws.amount**

_the amount of combinations possible with the password list_  


> **pws.write_to_file()**  

**arguments:** (directory (_required_), log_progress)  
_writes all possible combinations into a text file at the given directory_  
**directory** - location of text file to store password list in  
**log_progress** - a boolean. If true, the console will periodically print information with progress of the generation  

> **pws.display()**  

**arguments:** (log_progress)  
_prints out all possible combinations to the console_  
**log_progress** - a boolean. If true, the console will periodically print information with progress of the generation  

> **pws.set_log_interval()**  

**arguments:** (time (_required_) )  
_sets the time between progress logs (default: 1s)_  
**time** - new time interval (in seconds) between progress logs

> **pws.execute_each_pw()**  

**arguments:** (execute (_required_), log_progress)  
_calls the execute method on every password in the list. Each password is passed in as the only argument to the callable_  
**log_progress** - a boolean. If true, the console will periodically print information with progress of the generation  
