#ifndef LISTS_H
#define LISTS_H

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * struct listint_s - Singly linked list
 * @next: Points to the next node
 * @n: An integer
 *
 * Description: Singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint_end(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
void reverse_listint(listint_t **head);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif
