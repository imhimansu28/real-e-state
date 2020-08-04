# Building a Real E-State Application

## Creating	an	isolated	Python environment

```console
pip install virtualenv
```
After you install virtualenv, create an isolated enviroment with the following command:

```console
virtualenv my_env
```
This	will	create	a	my_env/	directory,	including	your	Python environment.	Any	Python	libraries	you	install	while	your	virtual environment	is	active	will	go	into	the	
**my_env/
     lib/
      python3.6/
         site-packages directory.**


Create the virtualenv for Project  with following Command:

__for Windows User__

```console
python -m venv env 
```

__for Linux  User__

```console
python3 -m venv env 
```

Run	the	following	command	to	activate	your	virtual	environment:

__for Windows User__

```console
source	my_env/Scripts/Activate
```

__for Linux  User__

```console
source	my_env/bin/activate 
```

