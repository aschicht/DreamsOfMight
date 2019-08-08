DreamsOfMight

venv
-------
You can create a new environment with the pyvenv command. Here, we’ll call our new environment my_env, but you can call yours whatever you want.

    python3.6 -m venv dom
    
Activate the environment using the command below, where my_env is the name of your programming environment.

    source dom/bin/activate
    
Then exit the virtual environment:

    deactivate




tcod
-------
Linux (Debian-based)

On Linux python-tcod will need to be built from source. You can run this command to download python-tcod’s dependencies with apt:

sudo apt install build-essential python3-dev python3-pip python3-numpy libsdl2-dev libffi-dev libomp5

If your GCC version is less than 6.1, or your SDL version is less than 2.0.5, then you will need to perform a distribution upgrade before continuing.

Once dependences are resolved you can build and install python-tcod using pip in a user environment:

python3 -m pip install --user tcod

Upgrading python-tcod

python-tcod is updated often, you can re-run pip with the --upgrade flag to ensure you have the latest version, for example:

python3 -m pip install --upgrade tcod

Upgrading from libtcodpy to python-tcod

libtcodpy is no longer maintained and using it can make it difficult to collaborate with developers across multiple operating systems, or to distribute to those platforms. New API features are only available on python-tcod.

You can recognise a libtcodpy program because it includes this file structure:

libtcodpy/
libtcod.dll
SDL2.dll

First make sure your libtcodpy project works in Python 3. libtcodpy already supports both 2 and 3 so you don’t need to worry about updating it, but you will need to worry about bit-size. If you’re using a 32-bit version of Python 2 then you’ll need to upgrade to a 32-bit version of Python 3 until libtcodpy can be completely removed.

Once you’ve installed python-tcod you can safely delete the libtcodpy/ folder and all DLL files of a libtcodpy program, python-tcod will seamlessly take the place of libtcodpy’s API.

From then on anyone can follow the instructions to install python-tcod and your project will work for them regardless of their platform or bit-size.
Distributing

Once your project is finished, it can be distributed using PyInstaller.
