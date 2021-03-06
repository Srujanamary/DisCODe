#! /usr/bin/env python

# Copyright (c) 2012 Warsaw Univeristy of Technology
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import os
import logging
import yaml
import pwd
import tempfile
import shutil

logging.basicConfig(level=logging.DEBUG)

from discode_helper import *

########################################################################

if __name__ == '__main__':  
	if (len(sys.argv) != 3) or (sys.argv[1] == "--help"):
		# stop the program and print an error message
		sys.exit("Usage: " + os.path.basename(sys.argv[0]) + " DCL_NAME COMPONENT_NAME")

	dcl_name = sys.argv[1]
	dcl_path = getDclDir(dcl_name)
	if (dcl_path == ""):
		logging.error("DCL [{}] doesn'n exist!".format(dcl_name))
		sys.exit()
	dcl_name = os.path.basename(dcl_path)
	cmp_name = sys.argv[2]

	dic = {}
	yml_name = cmp_name+".yml"
	if (os.path.exists(yml_name)):
		dic = prepareDicFromFile(yml_name)
	else:
		dic = prepareDefaultDic(cmp_name)

	createComponent(cmp_name, dcl_name, dcl_path, dic)
