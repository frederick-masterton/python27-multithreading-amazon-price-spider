'''
Python Multi Threading Example
Using the threading module to create a multi threaded,
url spider that uses queue to syncronize the threads.
To scan amazon for price updates.
on Ubuntu Linux OS 
'''

Prerequisites:
1.Python 2.7
2. threading module (Introduced post Python 2.4)

Note: Multi-threading bugs in Python are hard to reproduce, mainly because
thread execution is done differently each time the Python program is run.
(see nondeterministic).

Note:Multi-threading with Python is most efficent on low CPU based 
I/O operations(sending or receiving data). Anything super CPU intensive will not benefit from
multi-threading and more so will perform worse than a single thread.

Note: Threads are not processes. (Threads are lightweight and share resources.)

Note: To avoid errors when multiple threads share resources they need to be "aquire" a lock the resource 
or say "I'm using this resource right now, no one else use it". Once a thread 
is done using a resource you have to "release" the resource lock to make it available to
the rest of the program.

Note: Using Queues in Python in multithreaded Python applications is considered
best practice as locking is handled automatically by the queue,safer with a more
readable design pattern.
 

Start:
1.Define a new class inheriting from threading.Thread.
2.Override the __init__(self [,args]) method to add additional 
arguements that your thread may use.(A queue for instance)
3.Override the run(self [,args]) method to implement what 
the thread should do when started.(Read a webpage)
 


TODO: ADD refine readme and add either amazon or ebay support so 
I can tell what products are selling for what price and when. 


