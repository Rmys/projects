#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", "%s" % get.installDIR())

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --with-gtk=3.0 \
                         --enable-introspection=yes \
                         --enable-python")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "MAINTAINERS", "COPYING", "NEWS", "README")
