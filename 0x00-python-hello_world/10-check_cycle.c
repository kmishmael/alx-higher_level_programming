#include "lists.h"
/**
 * check_cycle - checks if linklist has a cycle
 * @list: pointer to the linked list
 * Return: 1 if cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL;
	listint_t *fast = NULL;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
