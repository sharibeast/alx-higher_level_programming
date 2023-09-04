#include "lists.h"
/**
 * check_cycle - check cycle in  a list
 * @list: list to check
 *
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *ff = list;
	listint_t *bck = list;

	if (!list)
	{
		return (0);
	}

	while (bck && ff && ff->next)
	{
		bck = bck->next;
		ff = ff->next->next;
		if (bck == ff)
		{
			return (1);
		}
	}
	return (0);
}
