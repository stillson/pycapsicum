==========
pycapsicum
==========

python interface to Capsicum (sandboxing)

Currently this release is for FreeBSD. It might work elsewhere, but I've only
tested it on FreeBSD

API
---

::

    import pycapsicum as pyc
    d = pyc.opendir("/tmp")
    f = open('/etc/hosts', 'r')
    pyc.cap_new(f.fileno(), pyc.CAP_READ | pyc.CAP_WRITE )

    pyc.cap_enter()
    f2 = pyc.openat(d, "foo", "rw")
    pyc.cap_show(pyc.cap_getrights(f2.fileno())
    pyc.cap_show(pyc.cap_getrights(f.fileno())
    pyc.cap_show(pyc.cap_getrights(d)


For details on the specific functions see the man pages for the man pages.

``cap_show(cap)``::
    cap -> an int capability
    prints out all the individual capabilities in a cap

``cap_enter()``::

    enters capability mode

``cap_getnew(fd, rights)``::

    set rights onto fd (which is a file object or file descriptor (int)

``cap_getrights(fd)``::

    get rights from a file descriptor or file object

``openat(d, path, flags='r')``::

    d - fd of a directory
    path - relative path to open
    flags - 'r','rw','w'
    the openat system call. Return a file object

``opendir(path, flags='r')``::

    path to open
    flags - 'r', 'rw', 'w'
    open a directory. returns an int to be passed in to openat


Once you have called ``cap_enter()`` , you can no longer open a file except with
``openat()``. Do all opens and imports before calling ``cap_enter()``. ``opendir()`` can only
be called before entering capability mode.
