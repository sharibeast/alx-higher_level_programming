#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - insert an element in ordered list
 * @head: ptr to first element
 * @number: node to put new node
 * Return: address of inserted nd
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_new = NULL;
	listint_t *tmp = NULL;
	listint_t *curr_node = *head;

	if (head == NULL)
	{
		return (NULL);
	}

	node_new = malloc(sizeof(listint_t));
	if (node_new == NULL)
		return (NULL);
	node_new->n = number;
	node_new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		node_new->next = *head;
		return (*head = node_new);
	}
	else
	{
		while (curr_node && curr_node->n < number)
		{
			tmp = curr_node;
			curr_node = curr_node->next;
		}
		tmp->next = node_new;
		node_new->next = curr_node;
	}
	return (node_new);
}
