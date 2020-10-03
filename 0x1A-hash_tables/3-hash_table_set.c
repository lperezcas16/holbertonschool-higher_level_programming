#include "hash_tables.h"

/**
 * hash_table_set - add element to the hash table
 * @ht: hast to add
 * @key: the key for the hash
 * @value: value associated with the key
 *
 * Return: success or not
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	hash_node_t *new = NULL, *list = NULL;
	unsigned long int i = 0;

	if (!new || !list || !ht)
		return (0);
	new = malloc(sizeof(hash_node_t));
	if (!new)
		return (0);
	list = key_index((const unsigned char *)key, ht->size);
}
