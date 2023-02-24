# offsetGroupManager
A maya script to quickly put controllers in offset groups without moving them.

![image](https://user-images.githubusercontent.com/84198946/221065092-804e21db-28f4-4aa7-9370-fc6d0c178353.png)

###### Table of content
- [Overview](https://github.com/Jordandionduval/offsetGroupManager#overview "Overview")
- [Installation](https://github.com/Jordandionduval/offsetGroupManager#installation "Installation")
- [Known Issues](https://github.com/Jordandionduval/offsetGroupManager#known-issues "Known Issues")

<!-- This is a comment -->
<!--###### Other Pages
- [Patch Notes](../offsetGroupManager/blob/main/PATCHNOTES.md "Go to Patch Notes page")-->

## Overview

I initially made this script to make the rigging process easier. I ended up writting a small script in the afternoon in the form of a simple script to execute once when all my controllers are in place.

The tool works by creating an offset group for a selected controller and matching it's transformation attributes. The controller is then parented to the offset group. This process is repeated for all selected items and respects controller hierarchy.

Offset groups are also named using the following rule: `[objectname]_OffsetGroup`

![image](https://user-images.githubusercontent.com/84198946/221066140-5047f1ff-98cf-401f-8a66-8e51ab59e722.png)


---

## Installation
1. Copy the "jdd_offsetGroupManager.py" to your Maya scripts directory:
>MyDocuments\Maya\scripts\

2. Then, within maya, use the following text as a python script to run the tool:
```
import jdd_offsetGroupManager as scpt
scpt.execScript()
```
3. *(Optional)* Alternatively, the text can be saved in the custom shelf using maya's script editor. This makes the script a small button in your current shelf so it can easily be accessed later.

---

## Known Issues
- Cannot put an object in an offset group if it's already in an offset group named `[objectname]_OffsetGroup`
