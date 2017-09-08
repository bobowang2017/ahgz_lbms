# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import jpype
from jpype import *
jvmPath = jpype.getDefaultJVMPath()
if not jpype.isJVMStarted():
    jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % ("../jar/ReadExcel.jar"))
jpype.java.lang.System.out.println("hello world!")
JDClass = JClass("com.test.ReadExcel")
jd = JDClass()
result = jd.read("wangbo")
print(result)
jpype.shutdownJVM()
