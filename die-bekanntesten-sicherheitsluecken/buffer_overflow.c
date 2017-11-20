#include <stdio.h>

int main() {
	char input[100];

	printf("Please give me some input:\n");
	gets(input);

	printf("Thank you for: %s\n", input);
}
