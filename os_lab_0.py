import os, time, datetime

home_dir = os.path.expanduser('~') #user's home directory is founded.

os.chdir(home_dir) #directory changed to user's home directory.

os.mkdir('os_lab_0') #'os_lab_0' directory created.

os.chdir('os_lab_0') #directory changed to 'os_lab_0'.

os.open('1.py', os.O_CREAT) #'1.py' created.

os.open('2.txt', os.O_CREAT) #'2.txt' created.

os.open('3.txt', os.O_CREAT)

print("Last modified times in 'os_lab_0' ")
for i in os.listdir(os.getcwd()):
	all_modified_times = os.path.getmtime(i)
	print("- " + i + ": " + time.ctime(all_modified_times))

print("\n")

print("Txt files in 'os_lab_0'")
for i in os.listdir(os.getcwd()):
	if i.endswith('.txt'):
		print("- " + i)
