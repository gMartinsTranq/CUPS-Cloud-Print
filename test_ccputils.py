#    CUPS Cloudprint - Print via Google Cloud Print
#    Copyright (C) 2011 Simon Cadman
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ccputils import Utils
import os, logging

def test_SetupLogging():
    testLogFile = '/tmp/testccp.log'
    assert Utils.SetupLogging(testLogFile) == True
    logging.error('test_setupLogging error test')
    assert os.path.exists(testLogFile) == True
    os.unlink(testLogFile)

def test_fileIsPDFFails():
    assert Utils.fileIsPDF('testfiles/NotPdf.txt') == False

def test_fileIsPDFSucceeds():
    assert Utils.fileIsPDF('testfiles/Test Page.pdf') == True

def test_fileIsPDFErrors():
    assert Utils.fileIsPDF("-dsadsa") == False

def test_whichFails():
    assert Utils.which('dsaph9oaghd9ahdsadsadsadsadasd') == None

def test_whichSucceeds():
    assert Utils.which('bash') in ( '/bin/bash', '/usr/bin/bash', '/usr/sbin/bash' )

def test_isExeSucceeds():
    if os.path.exists('/usr/bin/sh'):
        assert Utils.is_exe( "/usr/bin/sh" ) == True
    else:
        assert Utils.is_exe( "/bin/sh" ) == True

def test_isExeFails():
    assert Utils.is_exe( "/dev/null" ) == False
    

def test_getLPID():
    assert int(Utils.GetLPID()) > 0
    assert Utils.GetLPID() != None
    
    import grp
    
    workingPrintGroupName = 'lp'
    try:
        grp.getgrnam(workingPrintGroupName)
    except:
        workingPrintGroupName = 'cups'
        pass
    
    assert Utils.GetLPID('brokendefault', 'brokenalternative', False) == None
    assert int(Utils.GetLPID('brokendefault', workingPrintGroupName, False)) > 0
    assert Utils.GetLPID('brokendefault', workingPrintGroupName, False) != None