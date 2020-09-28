#include <Python.h>
#include <stdio.h>

int isValidStr(const char *s);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - ?
 * @p: ?
 */
void print_python_list(PyObject *p)
{
	unsigned int size;
	unsigned int allocated;
	unsigned int i_idex; /* item index */
	const char *i_name;	 /* item name */
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = (unsigned int)((PyVarObject *)(p))->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i_idex = 0; i_idex < size; i_idex++)
	{
		item = ((PyListObject *)p)->ob_item[i_idex];
		i_name = item->ob_type->tp_name;
		printf("Element %d: %s\n", i_idex, i_name);
		if (strcmp("bytes", i_name) == 0)
			print_python_bytes(item);
		else if (strcmp("float", i_name) == 0)
			print_python_float(item);
	}
}

/**
 * print_python_bytes - ?
 * @p: ?
 */
void print_python_bytes(PyObject *p)
{
	unsigned int size;
	const char *str;
	unsigned int s_idx; /* str index */

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = (unsigned int)PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %u\n", size);
	printf("  trying string: ");

	/* Create my own PyByte_AsString()*/
	str = ((PyBytesObject *)p)->ob_sval;

	if (isValidStr(str))
		printf("%s\n", str);
	else
		printf("??\n");

	printf("  first %d bytes: ", (size > 9) ? 10 : size + 1);
	for (s_idx = 0; s_idx < size + 1 && s_idx < 10; s_idx++)
	{
		printf("%02x", str[s_idx] & 0xFF);
		if (s_idx + 1 < size + 1 && s_idx + 1 < 10)
			putchar(' ');
		else
			putchar('\n');
	}
}

/**
 * print_python_float - ?
 * @p: ?
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	double floatpy;
	char *strpy;
	floatpy = ((PyFloatObject *)p)->ob_fval;
	strpy = PyOs_double_to_string(floatpy, "r", 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("value: %s\n", strpy);
}

/**
 * isValidStr - ?
 * @s: ?
 * Return: ?
 */
int isValidStr(const char *s)
{
	while (*s)
	{
		if (*s < ' ' || '~' < *s) /* revisar si no es desde 0 */
			return (0);
		s++;
	}
	return (1);
}
