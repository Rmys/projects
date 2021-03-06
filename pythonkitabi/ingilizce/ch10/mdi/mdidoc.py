"""
mdidoc.py - document or application model.

copyright: (C) 2001, Boudewijn Rempt
email:     boud@rempt.xs4all.nl

This framework is based on the template generated by KDevelop
"""
from qt import *
from resources import TRUE, FALSE

class MDIDoc(QObject):
    """
    The document represents the application model. The current
    document keeps a 'modified' state.

    signals: sigDocModified (boolean)
             sigDocTitleChanged (string)
             
    """
    def __init__(self, *args):
        apply(QObject.__init__, (self,)+args)
        self.newDocument()
        self._fileName="Untitled"
        self._title="Untitled"

    def setPathName(self, fileName):
        self._fileName=fileName
        self.setTitle(str(QFileInfo(fileName).fileName()))
    
    def pathName(self):
        return self._fileName

    def setTitle(self, title):
        self._title=title
        self.emit(PYSIGNAL("SigDocTitleChanged"),
                  (self._title,))

    def title(self):
        return self._title

    def newDocument(self):
        self.slotModify(FALSE)

    def openDocument(self, fileName, format=None):
        self.slotModify(FALSE)
        self.setPathName(fileName)

    def saveDocument(self, fileName, format=None):
        self.slotModify(FALSE)
        self.setPathName(fileName)
       
    def slotModify(self, value=None):
        if value==None:
            self._modified=not self._modified
        else:
            self._modified = value
        self.emit(PYSIGNAL("sigDocModified"),
                  (self._modified,))

    def isModified(self):
        return self._modified

    def closeDocument(self):
        pass
