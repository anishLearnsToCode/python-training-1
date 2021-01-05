[![readme](https://img.shields.io/badge/quick%20link-Back%20To%20Main%20Readme%20File-1f72ff.svg)](README.md)

## Python Environment Setup
We need to install and configure a few things before we can write and run any Python code. To write Python code we 
need the Python interpreter on our machine.

### 1. Install the Python 3 Interpreter
To write python programs on your machine we need the Python interpreter. There are 2 popular versions of Python 
out there right now Python 2 and Python 3. There are breaking changes between these versions and this course will be 
taught in Version 3. So as long as you have python version 3.{something}.{something} you're good to go 🙂

Download python from [this website](https://www.python.org/downloads/) 🌐. 

To check that python has been correctly installed on your machine run the following command on your terminal:
```shell script
python --version
```

It should have an output akin to:
```shell script
Python 3.8.3 
```

Once that Python has been successfully installed, we need to install a code editor or IDE so that we can write 
programs and run them. I suggest using __VS Code__ if you prefer a Code editor over an IDE (or if you don't know the
difference between Code editor and IDE 😉). using a code editor will aso be less intensive on computing resources.

I personally prefer the __JetBrains PyCharm__, but warning ⚠ it is a heavy software and might not run properly on 
all machines (especially laptops that are constrained for resources).

### 2. Installing VS Code (or go to step 3 - Installing PyCharm)
1. Download the setup from [here](https://code.visualstudio.com/).
2. Run the setup which is pretty straight forward. Just click next like 10 times and voila!

### 3. Installing JetBrains PyCharm
1. You can either install the educational edition (free) from [here](https://www.jetbrains.com/pycharm-edu/).
2. Or you can create an account on JetBrains if you have a university email address and then install the 
    [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/).
3. You can easily manage JetBrains IDE's and projects using the ToolBox app. From the ToolBox app you can now install
    either IntelliJ PyCharm Edu Edition or Ultimate Edition.    

### 4. Installing git (Optional - Only required for Windows users)
This is an optional step of your getting started guide and can be skipped. Although installing git and using it
in your projects is highly recommended. For a learning path to learn git have a look at the 
[Future Path + Scope](#future-scope-and-path) section.

Install git from the [git-scm](https://git-scm.com/downloads) website. Run the setup and click next like 10 times
and use the recommended settings for installation. 

There will be a section when it will ask the standard text editor and gie you an option between _Vim_ and _nano_. 
If you are not familiar with _Vim_ then opt for _nano_.

__IMPORTANT__ Opt for _nano_ if not familiar with _Vim_.

To check your installation of git check that git bash has been intalled and run the following command on your 
terminal.
```shell script
git --version
```

The output should be akin to 
```shell script
git version 2.24.1.windows.2
```

### 5. Writing your first Python Program
Open your text editor/IDE and create a new file `hello_world.py` and in that file copy paste the following code 
snippet.
```python
print('hello world !')
```

To run the code navigate to file in terminal and run the following commands.

```shell script
python hello_world.py
>>> hello world !
```
