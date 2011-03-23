#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

def setup():
    autotools.configure("--disable-static\
                         --enable-metacity\
                         --disable-evolution\
                         --disable-evolution-ecal")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pythonmodules.fixCompiledPy()
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
