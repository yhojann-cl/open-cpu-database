#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cpu.h"

static void print_help(char *prg_name, int exit_code)
{
	printf("Usage: %s OPTION NAME\n\n", prg_name);
	printf("Available OPTION:\n");
	printf("      --fuzzy-name\n");
	printf("      --exact-name\n");
	printf("      --fuzzy-codename\n");
	printf("      --exact-codename\n");
	printf("  -h, --help\n");
	exit(exit_code);
}

int main(int argc, char *argv[])
{
	if(argc < 3)
		print_help(argv[0], 1);

	char *option     = argv[1];
	char *name       = argv[2];
	const cpu_t *cpu = NULL;

	if(strcmp(option, "--fuzzy-name") == 0)
		cpu = cpu_find_by_fuzzy_name(name);
	else if(strcmp(option, "--exact-name") == 0)
		cpu = cpu_find_by_exact_name(name);
	else if(strcmp(option, "--fuzzy-codename") == 0)
		cpu = cpu_find_by_fuzzy_codename(name);
	else if(strcmp(option, "--exact-codename") == 0)
		cpu = cpu_find_by_exact_codename(name);
	else if((strcmp(option, "-h") == 0) || (strcmp(option, "--help") == 0))
		print_help(argv[0], 0);
	else
		print_help(argv[0], 1);

	if(cpu == NULL)
	{
		printf("'%s' not found in database.\n", name);
		return 2;
	}
	else
	{
		printf("'%s' found in database:\n", name);
		printf(" - name: %s\n", cpu->name);
		printf(" - codename: %s\n", cpu->codename);
		printf(" - architecture: %s\n", cpu->architecture);
		printf(" - cores: %i total, %i physical\n", cpu->cores.total, cpu->cores.physical);
		printf(" - speed: %.02f GHz min, %.02f GHz max\n", cpu->speed.min, cpu->speed.max);
		printf(" - socket: %s\n", cpu->socket);
		printf(" - technology node: %.02f %s\n", cpu->technologyNode.value, cpu->technologyNode.unit);
		printf(" - cache L3: %.0f %s\n", cpu->cacheL3.size, cpu->cacheL3.unit);
		printf(" - thermal design power: %.02f %s\n", cpu->thermalDesignPower.value, cpu->thermalDesignPower.unit);
		printf(" - released: %s\n", (cpu->released) == NULL ? "unknown" : cpu->released);
		return 0;
	}
}
