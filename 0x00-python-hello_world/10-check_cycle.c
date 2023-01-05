#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a single -linked list contains a cycle
 * @list: A singly-limked list
 * Return: 0 if there is no cycle and 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);
	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);
		turtle = turtle->next;
		hare = hare->next->next;
	}
	return (0);
}
