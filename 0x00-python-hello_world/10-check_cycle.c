#include "lists.h"
/**
 * check_cycle - find loop
 * @head: pointer to the list
 * Return: node that start loop
 */
int check_cycle(listint_t *head)
{
	listint_t *tmp, *other_tmp;

	if (!head || !head->next)
		return (0);
	tmp = head->next;
	other_tmp = head->next->next;
	while (tmp && other_tmp && other_tmp->next)
	{
		if (tmp == other_tmp)
			return (1);
		tmp = tmp->next;
		other_tmp = other_tmp->next->next;
	}
	return (0);
}
