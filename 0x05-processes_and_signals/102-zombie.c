#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - function that creates an infinite loop
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * create_zombie_processes - function that creates zombie processes
 * @num_processes: number of zombie processes to create
 */
void create_zombie_processes(int num_processes)
{
	for (int i = 0; i < num_processes; i++)
	{
		pid_t pid = fork();

		if (pid < 0)
		{
			perror("fork");
			exit(EXIT_FAILURE);
		}
		else if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}
}

/**
 * main - Entry point
 *
 * Return: Always 0.
 */
int main(void)
{
	int num_zombies = 5;

	create_zombie_processes(num_zombies);

	infinite_while();

	return (0);
}
