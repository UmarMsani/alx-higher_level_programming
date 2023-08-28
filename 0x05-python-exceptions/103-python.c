#include <Python.h>
#include <stdio.h>
#include <floatobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about a Python list object.
 * @p: PyObject representing a Python list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: PyObject representing a Python bytes object.
 */
void print_python_bytes(PyObject *p) {
	Py_ssize_t size, i;
	const char *data;

	if (!PyBytes_Check(p)) {
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", data);
	printf("  [.] first %ld bytes:", (size > 10) ? 10 : size);

	for (i = 0; i < ((size > 10) ? 10 : size); i++)
		printf(" %02x", (unsigned char)data[i]);

	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: PyObject representing a Python float object.
 */
void print_python_float(PyObject *p) {
	double value;

	if (!PyFloat_Check(p)) {
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	value = PyFloat_AS_DOUBLE(p);

	printf("[.] float object info\n");
	printf("  [.] value: %lf\n", value);
}
