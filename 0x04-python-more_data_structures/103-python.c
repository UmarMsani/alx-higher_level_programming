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
	if (!p || !PyObject_IsInstance(p, (PyObject *)&PyBytes_Type))
	{
		printf("Not a Python bytes object.\n");
		return;
	}

	Py_ssize_t bytes_size = ((PyVarObject *)p)->ob_size;
	char *bytes_data = ((PyBytesObject *)p)->ob_sval;

	printf("Python bytes info:\n");
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", bytes_size);
	printf("  trying string: %s\n", bytes_data);

	printf("  first %ld bytes: ", bytes_size);
	for (Py_ssize_t i = 0; i < bytes_size; ++i)
	{
		printf("%02x", (unsigned char)bytes_data[i]);
		if (i < bytes_size - 1)
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
	if (!p || !PyObject_IsInstance(p, (PyObject *)&PyList_Type))
	{
		printf("Not a Python list.\n");
		return;
	}

	Py_ssize_t list_size = ((PyVarObject *)p)->ob_size;
	printf("Python list info:\n");
	printf("[*] Size of the list: %ld\n", list_size);

	for (Py_ssize_t i = 0; i < list_size; ++i)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}
