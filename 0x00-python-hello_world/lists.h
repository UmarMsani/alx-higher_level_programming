#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - The singly linked list
 * @n: Integer
 * @next: pointer to the next node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);

#endif
