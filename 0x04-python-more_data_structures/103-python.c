#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - To Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Not a Python bytes object.\n");
		return;
	}

	printf("Python bytes info:\n");
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	printf("  first %ld bytes: ", ((PyVarObject *)p)->ob_size);
	for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; ++i)
	{
		printf("%02x", ((PyBytesObject *)p)->ob_sval[i] & 0xFF);
		if (i < ((PyVarObject *)p)->ob_size - 1)
		{
			printf(" ");
		}
	}
	printf("\n");
}

/**
 * print_python_list - To Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Not a Python list.\n");
		return;
	}

	printf("Python list info:\n");
	printf("[*] Size of the list: %ld\n", PyList_Size(p));

	for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
