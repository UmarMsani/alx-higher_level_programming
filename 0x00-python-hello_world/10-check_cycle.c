#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - A Function that checks for if a singlt list has a cycle
 * @list: linked list to check
 *
 * Return: 1 if list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;  /* Pointer moving one step at a time */
	listint_t *fast = list;  /* Pointer moving two steps at a time */

	if (list == NULL || list->next == NULL)
	{
		return 0;  /* No cycle if the list is empty or has only one element */
	}

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;  /* Move slow pointer one step */
		fast = fast->next->next;  /* Move fast pointer two steps */

		if (slow == fast) {
			return (1);  /* Cycle detected */
		}
	}

	return (0);  /* No cycle found */
}
