# Copyright (c) 2013, Chris Stillson <stillson@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import _pycapsi
import io
#General file I/O.

CAP_READ                = 0x0000000000000001L   # read/recv
CAP_WRITE               = 0x0000000000000002L   # write/send
CAP_MMAP                = 0x0000000000000004L   # mmap
CAP_MAPEXEC             = 0x0000000000000008L   # mmap(2) as exec
CAP_FEXECVE             = 0x0000000000000010L
CAP_FSYNC               = 0x0000000000000020L
CAP_FTRUNCATE           = 0x0000000000000040L
CAP_SEEK                = 0x0000000000000080L

# VFS methods.
CAP_FCHFLAGS            = 0x0000000000000100L
CAP_FCHDIR              = 0x0000000000000200L
CAP_FCHMOD              = 0x0000000000000400L
CAP_FCHOWN              = 0x0000000000000800L
CAP_FCNTL               = 0x0000000000001000L
CAP_FPATHCONF           = 0x0000000000002000L
CAP_FLOCK               = 0x0000000000004000L
CAP_FSCK                = 0x0000000000008000L
CAP_FSTAT               = 0x0000000000010000L
CAP_FSTATFS             = 0x0000000000020000L
CAP_FUTIMES             = 0x0000000000040000L
CAP_CREATE              = 0x0000000000080000L
CAP_DELETE              = 0x0000000000100000L
CAP_MKDIR               = 0x0000000000200000L
CAP_RMDIR               = 0x0000000000400000L
CAP_MKFIFO              = 0x0000000000800000L

# Lookups - used to constrain *at() calls.
CAP_LOOKUP              = 0x0000000001000000L

# Extended attributes.
CAP_EXTATTR_DELETE      = 0x0000000002000000L
CAP_EXTATTR_GET         = 0x0000000004000000L
CAP_EXTATTR_LIST        = 0x0000000008000000L
CAP_EXTATTR_SET         = 0x0000000010000000L

# Access Control Lists.
CAP_ACL_CHECK           = 0x0000000020000000L
CAP_ACL_DELETE          = 0x0000000040000000L
CAP_ACL_GET             = 0x0000000080000000L
CAP_ACL_SET             = 0x0000000100000000L

# Socket operations.
CAP_ACCEPT              = 0x0000000200000000L
CAP_BIND                = 0x0000000400000000L
CAP_CONNECT             = 0x0000000800000000L
CAP_GETPEERNAME         = 0x0000001000000000L
CAP_GETSOCKNAME         = 0x0000002000000000L
CAP_GETSOCKOPT          = 0x0000004000000000L
CAP_LISTEN              = 0x0000008000000000L
CAP_PEELOFF             = 0x0000010000000000L
CAP_SETSOCKOPT          = 0x0000020000000000L
CAP_SHUTDOWN            = 0x0000040000000000L

CAP_SOCK_ALL            = (CAP_ACCEPT | CAP_BIND | CAP_CONNECT \
         | CAP_GETPEERNAME | CAP_GETSOCKNAME | CAP_GETSOCKOPT \
         | CAP_LISTEN | CAP_PEELOFF | CAP_SETSOCKOPT | CAP_SHUTDOWN)

# Mandatory Access Control.
CAP_MAC_GET             = 0x0000080000000000L
CAP_MAC_SET             = 0x0000100000000000L

# Methods on semaphores.
CAP_SEM_GETVALUE        = 0x0000200000000000L
CAP_SEM_POST            = 0x0000400000000000L
CAP_SEM_WAIT            = 0x0000800000000000L

# kqueue events.
CAP_POLL_EVENT          = 0x0001000000000000L
CAP_POST_EVENT          = 0x0002000000000000L

# Strange and powerful rights that should not be given lightly.
CAP_IOCTL               = 0x0004000000000000L
CAP_TTYHOOK             = 0x0008000000000000L

# Process management via process descriptors.
CAP_PDGETPID            = 0x0010000000000000L
CAP_PDWAIT              = 0x0020000000000000L
CAP_PDKILL              = 0x0040000000000000L

# The mask of all valid method rights.
CAP_MASK_VALID          = 0x007fffffffffffffL

cap_dict = {
CAP_ACCEPT : "CAP_ACCEPT",
CAP_ACL_CHECK : "CAP_ACL_CHECK",
CAP_ACL_DELETE : "CAP_ACL_DELETE",
CAP_ACL_GET : "CAP_ACL_GET",
CAP_ACL_SET : "CAP_ACL_SET",
CAP_BIND : "CAP_BIND",
CAP_CONNECT : "CAP_CONNECT",
CAP_CREATE : "CAP_CREATE",
CAP_DELETE : "CAP_DELETE",
CAP_EXTATTR_DELETE : "CAP_EXTATTR_DELETE",
CAP_EXTATTR_GET : "CAP_EXTATTR_GET",
CAP_EXTATTR_LIST : "CAP_EXTATTR_LIST",
CAP_EXTATTR_SET : "CAP_EXTATTR_SET",
CAP_FCHDIR : "CAP_FCHDIR",
CAP_FCHFLAGS : "CAP_FCHFLAGS",
CAP_FCHMOD : "CAP_FCHMOD",
CAP_FCHOWN : "CAP_FCHOWN",
CAP_FCNTL : "CAP_FCNTL",
CAP_FEXECVE : "CAP_FEXECVE",
CAP_FLOCK : "CAP_FLOCK",
CAP_FPATHCONF : "CAP_FPATHCONF",
CAP_FSCK : "CAP_FSCK",
CAP_FSTAT : "CAP_FSTAT",
CAP_FSTATFS : "CAP_FSTATFS",
CAP_FSYNC : "CAP_FSYNC",
CAP_FTRUNCATE : "CAP_FTRUNCATE",
CAP_FUTIMES : "CAP_FUTIMES",
CAP_GETPEERNAME : "CAP_GETPEERNAME",
CAP_GETSOCKNAME : "CAP_GETSOCKNAME",
CAP_GETSOCKOPT : "CAP_GETSOCKOPT",
CAP_IOCTL : "CAP_IOCTL",
CAP_LISTEN : "CAP_LISTEN",
CAP_LOOKUP : "CAP_LOOKUP",
CAP_MAC_GET : "CAP_MAC_GET",
CAP_MAC_SET : "CAP_MAC_SET",
CAP_MAPEXEC : "CAP_MAPEXEC",
CAP_MASK_VALID : "CAP_MASK_VALID",
CAP_MKDIR : "CAP_MKDIR",
CAP_MKFIFO : "CAP_MKFIFO",
CAP_MMAP : "CAP_MMAP",
CAP_PDGETPID : "CAP_PDGETPID",
CAP_PDKILL : "CAP_PDKILL",
CAP_PDWAIT : "CAP_PDWAIT",
CAP_PEELOFF : "CAP_PEELOFF",
CAP_POLL_EVENT : "CAP_POLL_EVENT",
CAP_POST_EVENT : "CAP_POST_EVENT",
CAP_READ : "CAP_READ",
CAP_RMDIR : "CAP_RMDIR",
CAP_SEEK : "CAP_SEEK",
CAP_SEM_GETVALUE : "CAP_SEM_GETVALUE",
CAP_SEM_POST : "CAP_SEM_POST",
CAP_SEM_WAIT : "CAP_SEM_WAIT",
CAP_SETSOCKOPT : "CAP_SETSOCKOPT",
CAP_SHUTDOWN : "CAP_SHUTDOWN",
CAP_SOCK_ALL : "CAP_SOCK_ALL",
CAP_TTYHOOK : "CAP_TTYHOOK",
CAP_WRITE : "CAP_WRITE",
}

def cap_show(cap):
    out_caps = []
    for icap,name in cap_dict.items():
        if cap & icap == icap:
            out_caps.append(name)

    return " ".join(out_caps)

def cap_enter():
    _pycapsi.cap_enter()

def cap_getmode():
    return bool(_pycapsi.cap_getmode())

def cap_getnew(fd, rights):
    lfd = fd
    if type(fd) != type(1):
        lfd = fd.fileno()
    if(_pycapsi.cap_getnew(fd, rights)):
        raise Exceptions.Exception("getnew fail")

def cap_getrights(fd):
    lfd = fd
    if type(fd) != type(1):
        lfd = fd.fileno()
    return _pycapsi.cap_getrights(lfd)

def _get_flag(flags):
    flagDict = { 'r':0, 'rw':2, 'w':1, }
    if flags in flagDict:
        return flagDict[flags]
    else:
        raise exceptions.ValueError("bad flag! %s" % flags)

def openat(fd, path, flags='r'):
    return io.FileIO(_pycapsi.openat(fd, path, _get_flag(flags)))

def opendir(path, flags='r'):
    return _pycapsi.opendir(path, _get_flag(flags))

