#ifndef _CPU_H_
#define _CPU_H_

/* Types */

typedef struct
{
  const int total;
  const int physical;
} cpu_cores_t;

typedef struct
{
  const double min;
  const double max;
} cpu_speed_t;

typedef struct
{
  const char *const measure;
  const double value;
} cpu_technology_node_t;

typedef struct
{
  const char *const measure;
  const double size;
} cpu_cache_t;

typedef struct
{
  const char *const measure;
  const double value;
} cpu_thermal_design_power_t;

typedef struct
{
  const char *const name;
  const char *const codename;
  const char *const architecture;
  const cpu_cores_t cores;
  const cpu_speed_t speed;
  const char *const socket;
  const cpu_technology_node_t technologyNode;
  const cpu_cache_t cacheL3;
  const cpu_thermal_design_power_t thermalDesignPower;
  const char *const released;
} cpu_t;


/* Functions */

/* Find CPU by approximate model name, or return NULL if not found.
Example of usage: `const cpu_t *cpu = cpu_find_by_fuzzy_name("core i7");` */
const cpu_t *cpu_find_by_fuzzy_name(char *name);

/* Find CPU by exact model name, or return NULL if not found.
Example of usage: `const cpu_t *cpu = cpu_find_by_exact_name("Ryzen 7 5800X3D");` */
const cpu_t *cpu_find_by_exact_name(char *name);

/* Find CPU by approximate model codename, or return NULL if not found.
Example of usage: `const cpu_t *cpu = cpu_find_by_fuzzy_codename("lake");` */
const cpu_t *cpu_find_by_fuzzy_codename(char *codename);

/* Find CPU by exact model codename, or return NULL if not found.
Example of usage: `const cpu_t *cpu = cpu_find_by_exact_codename("Milan-X");` */
const cpu_t *cpu_find_by_exact_codename(char *codename);


#endif /* _CPU_H_ */
