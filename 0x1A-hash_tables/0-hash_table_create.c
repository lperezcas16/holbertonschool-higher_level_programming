#include "hash_tables.h"

/**
 * hash_table_create - Function to create hash tables
 * @size: the size of the hash table
 *
 * Return: pointer to the hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *head = NULL;

	head = malloc(sizeof(hash_table_t));

	if (!head)
		return (NULL);
	head->array = calloc(size, sizeof(hash_node_t));
	if (!head->array)
		return (NULL);
	head->size = size;
	return (head);
}
