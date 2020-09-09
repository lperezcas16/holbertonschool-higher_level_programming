#include <stdlib.h>
#include "Python.h"
/**
 * print_python_list_info - Prints basic info from python list.
 * @p: Python list.
 * Return: None.
 */
void print_python_list_info(PyObject *p)
{
	int alloc, i = 0;

	int len = Py_SIZE(p);

	PyObject *obj;

	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] alloc = %d\n", alloc);

	while (i < len)
	{
		printf("Element %i: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i++;
	}
}
