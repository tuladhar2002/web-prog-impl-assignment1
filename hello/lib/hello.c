#include <stdio.h>

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
		printf("Usage: %s <-String to be printed out->\n", argv[0]);
	}

	printf("Hello %s!\n", argv[1]);
	return 0;
}
