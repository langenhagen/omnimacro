# Omnimacro
A simple tool to record and replay keyboard macros.


## Prerequisites
`omnimacro` requires Python, at least version `3.6`, to be available on the system.  
`omnimacro` downloads further required packages during setup.


## Setup
To setup `omnimacro`, go to the project's root directory and call `setup.sh`. E.g., in bash, do:
```bash
bash setup.sh
```

Upon setup, `omnimacro` creates a virtual Python environment and installs the latest versions of its
dependencies. Find the list of dependencies in the file `requirements.txt`.

After the script installs the dependencies into the virtual environment, `omnimacro` is ready to
run.


## Usage
You can start `omnimacro` by calling `bash omnimacro.sh`.

To record keyboard events, call:
```bash
bash omnimacro.sh [<path/to/recording/file>]
```
To use a default path, call:
```bash
bash omnimacro.sh
```

After invocation, the command records all keyboard presses and releases, except for the `<cmd>` key.
Press `<cmd>` + `<p>` to stop recording.

To replay keyboard events from a file, call:
```bash
bash omnimacro.sh --play|-p [<path/to/recording/file>]
```
To replay keyboard events from the default file, call:
```bash
bash omnimacro.sh -p
```

### Using a Global Keyboard Shortcut
`omnimacro` becomes handy when you assign it to a global keyboard shortcut that you can trigger from
anywhere in your graphical user interface.

On `Ubuntu 18.04` and higher, you can go to:
`Settings` > `Devices` > `Keyboard` > `Keyboard Shortcuts` > `+`.
There you can set a command's name, the path to the `omnimacro.sh` executable and a key
combination.

Create 2 shortcuts: 1 shortcut for recording a macro and 1 shortcut for executing a macro.


## Contributing
Work on your stuff locally, branch, commit and modify to your heart's content.
If there is anything you can extend, fix or improve, please get in touch!
Happy coding!


## License
See LICENSE file.
