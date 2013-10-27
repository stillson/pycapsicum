/*
 * Copyright (c) 2013, Chris Stillson <stillson@gmail.com>
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#define PY_SSIZE_T_CLEAN
#include <stdio.h>
#include <stdint.h>
#include <Python.h>
#include <sys/capability.h>
#include <errno.h>
#include <fcntl.h>

PyDoc_STRVAR(module_doc, "pycapsicum: Python interface to capsicum\n");

static PyObject *
capsi_cap_enter(PyObject *self, PyObject *args)
{
    int rval;

    if (!PyArg_ParseTuple(args, ""))
        return NULL;

    rval = cap_enter();
    if (rval != 0)
    {
        rval = errno;
    }
    return Py_BuildValue("i", rval);
}

//int     cap_getmode(u_int* modep);
static PyObject *
capsi_cap_getmode(PyObject *self, PyObject *args)
{
    u_int rval;

    if (!PyArg_ParseTuple(args, ""))
        return NULL;

    if (cap_getmode(&rval))
    {
        rval = errno;
    }
    return Py_BuildValue("i", rval);
}

//int     cap_new(int fd, cap_rights_t rights);
static PyObject *
capsi_cap_new(PyObject *self, PyObject *args)
{
    u_int       rval = 0;
    int         fd;
    uint64_t   rights;

    if (!PyArg_ParseTuple(args, "ik", &fd, &rights))
        return NULL;

    if (cap_new(fd, (cap_rights_t)rights))
    {
        rval = errno;
    }
    return Py_BuildValue("i", rval);
}

//int     cap_getrights(int fd, cap_rights_t *rightsp);
static PyObject *
capsi_cap_getrights(PyObject *self, PyObject *args)
{
    u_int       rval = 0;
    int         fd;
    uint64_t   rights;

    if (!PyArg_ParseTuple(args, "i",&fd))
        return NULL;

    if (cap_getrights(fd, (cap_rights_t*)&rights) )
    {
        rval = errno;
        return Py_BuildValue("i", rval);
    }

    return Py_BuildValue("k", rights);

}

//int openat(int fd, const char *path, int flags, ...);
static PyObject *
capsi_openat(PyObject *self, PyObject *args)
{
    int fd, flags, rv;
    const char *path;

    if ( !PyArg_ParseTuple(args, "isi", &fd, &path, &flags) )
        return NULL;

    rv = openat(fd, path, flags);

    return Py_BuildValue("i", rv);
}

static PyObject *
capsi_opendir(PyObject *self, PyObject *args)
{
    int flags, rv;
    const char *path;

    if ( !PyArg_ParseTuple(args, "si", &path, &flags) )
        return NULL;

    rv = open(path, flags);

    return Py_BuildValue("i", rv);
}

static PyMethodDef capsi_functions[] = {
        {"cap_enter",       capsi_cap_enter,        METH_VARARGS, "cap_enter()"},
        {"cap_getmode",     capsi_cap_getmode,      METH_VARARGS, "cap_getmode()"},
        {"cap_new",         capsi_cap_new,          METH_VARARGS, "cap_new()"},
        {"cap_getrights",   capsi_cap_getrights,    METH_VARARGS, "cap_getrights()"},
        {"openat",          capsi_openat,           METH_VARARGS, "openat()"},
        {"opendir",         capsi_opendir,          METH_VARARGS, "opendir()"},
        {NULL,      NULL}   /* Sentinel */
};

PyMODINIT_FUNC
init_pycapsi(void)
{
        PyObject *m;

        m = Py_InitModule3("_pycapsi", capsi_functions, module_doc);
        if (m == NULL)
            return;
}
