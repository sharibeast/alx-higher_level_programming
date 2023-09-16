#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/*
 * is_palindrome - one argument
 * @head: pointer
 *
 * Description: check value if it is palindrome
 * Return: 1 if true or 0 when false
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int count_var = 0, ct = 0, half_var;
	int *buf = NULL;

	if (!head)
	{
		return (0);
	}
	if (!*head)
	{
		return (1);
	}
	ptr = *head;
	while (ptr && ptr->next)
	{
		ptr = ptr->next;
		count_var++;
	}
	buf = malloc(sizeof(int) * count_var);
	if (!buf)
		return (0);

	ptr = *head;
	count_var = 0;
	while (ptr)
	{
		buf[count_var] = ptr->n;
		count_var++;
		ptr = ptr->next;
	}
	half_var = count_var / 2;

	while (half_var)
	{
		if (buf[ct] != buf[count_var - 1])
			return (0);
		half_var--;
		ct++;
		count_var--;
	}
	free(buf);
	return (1);
}
