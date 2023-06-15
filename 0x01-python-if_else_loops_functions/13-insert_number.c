#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current = NULL;
    listint_t *new_node;

    if (head == NULL)
    {
        return (NULL);
    }
    current = *head;
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        return (NULL);
    }
    new_node->n = number;
    new_node->next = NULL;
    while (current != NULL)
    {
        if (current->n <= number)
        {
            if (current->next->n > number)
            {
                new_node->next = current->next;
                current->next = new_node;
                return (new_node);
            }
            else if (current->next == NULL)
            {
                current->next = new_node;
                return (new_node);
            }
        }
        current = current->next;
    }
    return (NULL);
}
