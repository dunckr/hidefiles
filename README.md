HideFiles plugin for Sublime Text 2
=====================================

Show and hide specific files easily.

Installation
------------

1. Using Package Control, install "HideFiles"

Or:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. Clone this repo

Configuration
------------

Change the **hidefiles.sublime-settings**:

    {
      "coffee": ["*.js","*.md","*.json","*.txt"],
      "js": ["*.coffee","*.html","*.css"]
    }

Where each property specifies the files in an array that are to be hidden when activated.

Commands
------------

`hide_files`: Hides the files for the currently opened file type

`show_files`: Shows the files for the currently opened file type

Default Keymap
------------

hide_files
`ctrl+shift+-`

show_files
`ctrl+shift+=`


____

