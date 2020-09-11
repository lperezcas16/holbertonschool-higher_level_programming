#include <Python.h>
void print_python_bytes(PyObject *p);
/**
 * print_python_list - Function
 * @p: pyobject
 * Return: void
 */
void print_python_list(PyObject *p)
{
    int i;
    PyListObject *type = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zu\n", PyList_Size(p));
    printf("[*] Allocated = %zu\n", type->allocated);
    for (i = 0; i < PyList_Size(p); i++)
    {
        printf("Element %d: %s\n", i, type->ob_item[i]->ob_type->tp_name);
        if (strcmp(type->ob_item[i]->ob_type->tp_name, "bytes") == 0)
            print_python_bytes(type->ob_item[i]);
    }
}
/**
 * print_python_bytes - Function
 * @p: pyobject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *s;
    unsigned int i;

    printf("[.] bytes object info\n");
    s = (PyBytesObject *)p;
    if (PyBytes_Check(s))
    {
        printf("  size: %ld\n", s->ob_base.ob_size);
        printf("  trying string: %s\n", s->ob_sval);
        printf("  first %ld bytes:", s->ob_base.ob_size + 1 <= 10 ? s->ob_base.ob_size + 1 : 10);
        for (i = 0; i < s->ob_base.ob_size + 1 && i < 10; i++)
        {
            printf(" %02x", s->ob_sval[i] & 0xff);
        }
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
