#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if the linked list is a palindrome
 * @head: the header
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	int buff[3000], len = 0;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	temp = *head;
	for (len = 0; temp; len++)
	{
		buff[len] = temp->n;
		temp = temp->next;
	}
	len--;
	temp = *head;
	for (; temp; len--)
	{
		if (buff[len] != temp->n)
		{
			return (0);
		}
		temp = temp->next;
	}

	return (1);
}
