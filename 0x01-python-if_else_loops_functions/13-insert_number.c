#include "lists.h"
/**
 * insert_node - insert a number into a sorted linked list
 * @head: pointer to the pointer of the first node or listint_t list
 * @number: Integer to be included into the new node
 * Return: On success of the address of the new node, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new_node;

	if (head == NULL)
		return (NULL);
	tmp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node-> = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (tmp->n > number)
	{
		*head = new_node;
		new_node->next = tmp;
		return (new_node);
	}
	while (tmp->next != NULL)
	{
		if (tmp->next->n > number)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
			return (new_node);
		}
		tmp = tmp->next;
	}
	tmp->next = new_node;
	return (new_node);
}
