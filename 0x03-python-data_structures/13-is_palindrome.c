#include "lists.h"

/**
 * is_palindrome - checks if linked list is palindrome
 * @head: linked list
 * Return: int 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	int size;
	int i;
	int j;
	listint_t *copy;
	int *ls;
	int status;

	copy = *head;
	for (size = 0; copy; size++)
	{
		size++;
		copy = copy->next;
	}
	ls = malloc(sizeof(int) * (size + 1));
	if (!ls)
	{
		return (-1);
	}
	copy = *head;
	for (i = 0; i < (size + 1); i++)
	{
		ls[i] = copy->n;
		copy = copy->next;
	}
	i = 0;
	j = size;
	while (i < j)
	{
		if (ls[i] == ls[j])
		{
			status = 1;
		} 
		else
		{
			status = 0;
		}
		i++;
		j--;
	}
	return (status);
}

