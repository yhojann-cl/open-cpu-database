const fs = require('fs');

class CBuilder {

    async build(data, basePath) {
        console.log('Generating C repository project ...');

        const filePath = `${basePath}/src/cpu.c`;

        if(fs.existsSync(filePath))
            fs.unlink(filePath, e => { if(e) throw e });

        fs.writeFile(filePath, `

#define _GNU_SOURCE
#include <stdlib.h>
#include <string.h>
#include "cpu.h"

static const cpu_t items[] =
{
  ${data.list.map(item => `
  {
    .name = "${item.name}",
    .codename = "${item.codename}",
    .architecture = "${item.architecture}",
    .cores = { .total = ${item.cores.total}, .physical = ${item.cores.physical} },
    .speed = { .min = ${item.speedGhz.min}, .max = ${item.speedGhz.max} },
    .socket = "${item.socket}",
    .technologyNode = { .unit = "${item.technologyNode.unit}", .value = ${item.technologyNode.value} },
    .cacheL3 = { .unit = "${item.cacheL3.unit}", .size = ${item.cacheL3.size} },
    .thermalDesignPower = { .unit = "${item.thermalDesignPower.unit}", .value = ${item.thermalDesignPower.value} },
    .released = ${(item.released != null) ? `"${item.released}"` : "NULL"}
  }
  `.trim()).join(',\n  ')}
};

#define NUM_CPU_ITEMS (sizeof(items) / sizeof(cpu_t))

const cpu_t *cpu_find_by_fuzzy_name(char *name)
{
  long unsigned i;
  for(i = 0; i < NUM_CPU_ITEMS; i++)
    if(strcasestr(items[i].name, name) != NULL)
      return &items[i];
  return NULL;
}

const cpu_t *cpu_find_by_exact_name(char *name)
{
  long unsigned i;
  for(i = 0; i < NUM_CPU_ITEMS; i++)
    if(strcmp(items[i].name, name) == 0)
      return &items[i];
  return NULL;
}

const cpu_t *cpu_find_by_fuzzy_codename(char *codename)
{
  long unsigned i;
  for(i = 0; i < NUM_CPU_ITEMS; i++)
    if(strcasestr(items[i].codename, codename) != NULL)
      return &items[i];
  return NULL;
}

const cpu_t *cpu_find_by_exact_codename(char *codename)
{
  long unsigned i;
  for(i = 0; i < NUM_CPU_ITEMS; i++)
    if(strcmp(items[i].codename, codename) == 0)
      return &items[i];
  return NULL;
}

        `.trim(), (e) => { if (e) throw e });
        return data;
    }
}

module.exports = CBuilder;