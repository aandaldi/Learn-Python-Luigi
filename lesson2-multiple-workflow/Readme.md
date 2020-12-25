### What is Luigi?

Luigi is batch workflow system.

## Install Luigi
    pip install luigi


### Luigi Basic


Tasks are defined as python classes that subclass the luigi.Task super class. 
Each task has methods that the workflow designer is supposed to implement:

- requires() - should return one or more instantiated tasks that the current task depends on.
- output() - return one or more targets objects, typically representing files, the the current task will produce when run.
- run() - Here goes all the code that the task should run as its job.


To run the script, there are only two things you have to specify; 
A scheduler host to use, and the name of the task to run. For now, 
lets just use the "--local-scheduler" option, so that we don't need to start a new scheduler, 
and of course, we specify the "HelloWorld" that we have defined above:

example: `python <pythonfile> --localsheduler <classTaskName>`


###visualizing running workflows
typing on terminal `luigid` then go to `http://localhost:8082`

Then, in a separate terminal window, start the luigi workflow we created above, 
now specifying "localhost" as our "--scheduler-host":


source <i>(https://rillabs.com/posts/luigi-tutorial)</i>