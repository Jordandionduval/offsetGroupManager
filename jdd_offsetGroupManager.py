#-----------------------------Tested for Maya 2022+-----------------------------#
#
#             jdd_offsetGroupManager.py 
#             v1.0.0, last modified 23/02/23
# 
# MIT License
# Copyright (c) 2023 Jordan Dion-Duval
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
#----------------------------------INSTALLATION---------------------------------#
# 1. Copy the "jdd_outlinerBuddy.py" to your Maya scripts directory:
#     > MyDocuments\Maya\scripts\
# 2. Then, within maya, use the following text as a python script to run the tool:
#    (without the apostrophes)
'''
import jdd_offsetGroupManager as scpt
scpt.execScript()
'''
# 3.(Optional) Alternatively, the text can be saved in the custom shelf using
# maya's script editor. This makes the script a small button in your current shelf
# so it can easily be accessed later.
#--------------------------------------------------------------------------------#

#Setup
import maya.cmds as cmds

def execScript():
    #Initialize Variables
    opCount = 0

    #Offset Group Manager
    itemList = cmds.ls(sl = True, sn = True)

    for item in itemList:

        offsetGroup = str(item + "_OffsetGroup")

        cmds.group(em = True, name = offsetGroup, w = True)
        cmds.matchTransform(offsetGroup, item )
        cmds.parent(item, offsetGroup)
        opCount += 1

    #Operations feedback
    if opCount == 1:
        print("Placed " + str(opCount) + " object in an offset group.")
    else:
        print("Placed " + str(opCount) + " objects in an offset group.")

execScript()