#!/usr/bin/env python3

import sys, subprocess, os, shutil, time
from pathlib import Path

from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QButtonGroup,
    QWidget,
    QFileDialog
)
from basicui import Ui_Widget

is_win = sys.platform.startswith('win')

class DefaultHousiniPath():
    def __init__(self):        
        self.houdiniVersion = "18.5.696"
    
    def getHFS(self):
        if is_win:
            p = Path("C:/Program Files/Side Effects Software/Houdini {}".format(self.houdiniVersion))
            return p if p.exists() else ""

    def getHENV(self):
        if is_win:
            import ctypes
            from ctypes.wintypes import MAX_PATH
            dll = ctypes.windll.shell32
            buf = ctypes.create_unicode_buffer(MAX_PATH +1)
            if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
                p = Path(buf.value+"/houdini"+self.houdiniVersion[:-4])
                print(p)
                return p if p.exists() else ""

hroot = DefaultHousiniPath()

class FixHoudiniPlugin(QObject):
    beforeCamekBuild = pyqtSignal()
    cmakeBuildDone = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.HENV = str(hroot.getHENV())
        self.beforeCamekBuild.connect(self.fixENV)
        self.cmakeBuildDone.connect(self.restoreENV)
        self.packagesFolder = Path(self.HENV+"/packages")
        self.houdinienvFile = Path(self.HENV+"/houdini.env")
        print(self.packagesFolder, self.houdinienvFile)
        
    def fixENV(self):
        if self.packagesFolder.exists():
            try:
                self.packagesFolder.rename(str(self.packagesFolder)+"_back")
            except: pass
        if self.houdinienvFile.exists():
            try:
                self.houdinienvFile.rename(str(self.houdinienvFile)+"_back")
            except: pass

    def restoreENV(self):
        rePackage = Path(str(self.packagesFolder)+"_back")
        reHouEnv = Path(str(self.houdinienvFile)+"_back")
        if rePackage.exists():
            try:
                rePackage.rename(str(self.packagesFolder))
            except: pass
        if reHouEnv.exists():
            try:
                reHouEnv.rename(str(self.houdinienvFile))
            except:
                if (self.houdinienvFile.exists() and reHouEnv.exists()):
                    try:
                        os.remove(reHouEnv)
                    except: pass


class BuildCMake():
    def __init__(self, fixHoudiniPlugin):
        self.env = os.environ.copy()
        self.env["HFS"] = str(hroot.getHFS())
        self.HDKPATH = ""
        self.fix = fixHoudiniPlugin

    def setHDKPATH(self, path):
        self.HDKPATH = path

    def preBuild(self):
        self.buildPath = Path(self.HDKPATH+"/build")
        self.program = ["cmake", "-G" "Visual Studio 15 2017", "-A", "x64", ".."]
        if self.buildPath.exists():
            try:
                shutil.rmtree(self.buildPath)
            except:
                pass
        if not self.buildPath.exists():
            self.buildPath.mkdir()

    def build(self):
        self.preBuild()
        self.fix.beforeCamekBuild.emit()
        time.sleep(2)
        subprocess.call(self.program, env=self.env, cwd=self.buildPath)
        self.fix.cmakeBuildDone.emit()

class HDKCMakeWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tr = QCoreApplication.translate
        
        self.buildCmake = BuildCMake(FixHoudiniPlugin())
        self.basicui = Ui_Widget()
        self.basicui.setupUi(self)
        self.setWindowTitle(self.tr("HDKCMakeWindow", "HDK CMake Tools"))

        self.basicui.lineEditHoudiniPath.setText(str(hroot.getHFS()))

        self.addButtontoGroup()
        self.createSignals()

    def addButtontoGroup(self):
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.basicui.pushButtonHDKPathOpen)
        self.buttonGroup.addButton(self.basicui.pushButtonHoudiniPathOpen)
        self.buttonGroup.addButton(self.basicui.pushButtonProjectBuild)
    
    def createSignals(self):
        self.buttonGroup.buttonClicked.connect(self.onbtnGroupClicked)

    def buildCMakeProject(self, folder):
        print(folder)
        self.buildCmake.setHDKPATH(folder)
        self.buildCmake.build()

    def onbtnGroupClicked(self, e):
        if (e == self.basicui.pushButtonHDKPathOpen):
                HDKfolder = QFileDialog.getExistingDirectory(self,
                                                  self.tr("HDKCMakeWindow", "Select HDK Project Path"),
                                                  "D:\\")
                self.basicui.lineEditHDKPath.setText(HDKfolder)

        if (e == self.basicui.pushButtonHoudiniPathOpen):
                HFSfolder = QFileDialog.getExistingDirectory(self,
                                                  self.tr("HDKCMakeWindow", "Select Houdini Root Path"),
                                                  str(hroot.getHFS()))
                self.basicui.lineEditHoudiniPath.setText(HFSfolder)

        if (e == self.basicui.pushButtonProjectBuild):
            if (self.basicui.lineEditHDKPath.text() and self.basicui.lineEditHoudiniPath.text()):
                self.buildCMakeProject(self.basicui.lineEditHDKPath.text())
            else:
                pass


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = HDKCMakeWindow()
    ex.show()
    sys.exit(app.exec_())
