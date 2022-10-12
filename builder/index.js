const fs = require('fs');
const { unlink } = require('fs/promises');
const ObjectsToCsv = require('objects-to-csv');


class Builder{
    
    constructor() {
        console.log('Loading main database ...');
        this.loadMainDatabase()
        .then(data => this.makeDart(data))
        .then(data => this.makeC(data))
        .then(data => this.makeCSV(data))
        .catch(e => {
            console.log('Unable build database.');
            throw e;
        });
    }
    
    async loadMainDatabase() {
        let data = fs.readFileSync('../database/cpu.json');
        return JSON.parse(data);
    }
    
    async deleteIfExist(path) {
        if(fs.existsSync(path))
            return unlink(path);
    }
    
    async makeDart(data) {
        console.log('Generating dart repository project ...');
        
        await this.deleteIfExist('../database/dart/cpu.dart')
        .then(() => fs.writeFile('../database/dart/cpu.dart', `

class CPUCores {
  final int total;
  final int physical;

  const CPUCores({ required this.total, required this.physical });
}

/// CPU speed in Ghz.
class CPUSpeed {
  final double min;
  final double max;

  const CPUSpeed({ required this.min, required this.max });
}

class CPUSize {
  final String measure;
  final double value;

  const CPUSize({ required this.measure, required this.value });
}

class CPUCache {
  final String measure;
  final double size;

  const CPUCache({ required this.measure, required this.size });
}

class CPUThermalDesignPower {
  final String measure;
  final double value;

  const CPUThermalDesignPower({ required this.measure, required this.value });
}

class CPU {
  final String name;
  final String codename;
  final String architecture;
  final CPUCores cores;
  final CPUSpeed speed;
  final String socket;
  final CPUSize size;
  final CPUCache cacheL3;
  final CPUThermalDesignPower thermalDesignPower;
  final DateTime? released;

  const CPU({
    required this.name,
    required this.codename,
    required this.architecture,
    required this.cores,
    required this.speed,
    required this.socket,
    required this.size,
    required this.cacheL3,
    required this.thermalDesignPower,
    required this.released
  });
}

/// CPU Repository. Example of usage: \`CPU cpu = CPURepository().findByCodename('Milan-X');\`
class CPURepository {

  final List<CPU> items;

  CPURepository() : items = [
    ${data.list.map(item => `
    CPU(
      name: '${item.name}',
      codename: '${item.codename}',
      architecture: '${item.architecture}',
      cores: const CPUCores(total: ${item.cores.total}, physical: ${item.cores.physical}),
      speed: const CPUSpeed(min: ${item.speedGhz.min}, max: ${item.speedGhz.max}),
      socket: '${item.socket}',
      size: const CPUSize(measure: '${item.size.measure}', value: ${item.size.value}),
      cacheL3: const CPUCache(measure: '${item.cacheL3.measure}', size: ${item.cacheL3.size}),
      thermalDesignPower: const CPUThermalDesignPower(measure: '${item.thermalDesignPower.measure}', value: ${item.thermalDesignPower.value}),
      released: ${(item.released != null) ? `DateTime.parse('${item.released}')` : `null`}
    )
    `.trim()).join(',\n    ')}
  ];

  /// Find CPU by model name, or thrown a StateError exception if not found.
  CPU findByName(String name) {
    return items.where((item) => (item.name == name)).first;
  }

  /// Find CPU by model codename, or thrown a StateError exception if not found.
  CPU findByCodename(String codename) {
    return items.where((item) => (item.codename == codename)).first;
  }
}

        `.trim(), (e) => { if(e) throw e }));
        
        return data;
    }

    async makeC(data) {
      console.log('Generating C repository project ...');

      await this.deleteIfExist('../database/c/cpu.c')
      .then(() => fs.writeFile('../database/c/cpu.c', `

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
    .size = { .measure = "${item.size.measure}", .value = ${item.size.value} },
    .cacheL3 = { .measure = "${item.cacheL3.measure}", .size = ${item.cacheL3.size} },
    .thermalDesignPower = { .measure = "${item.thermalDesignPower.measure}", .value = ${item.thermalDesignPower.value} },
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

        `.trim(), (e) => { if(e) throw e }));

        return data;
    }

    async makeCSV(data){
        console.log('Generating CSV repository project ...');
        
        await this.deleteIfExist('../database/cpu.csv')
        .then(() => (new ObjectsToCsv(data.list.map(item => ({
            name: item.name,
            codename: item.codename,
            architecture: item.architecture,
            coresTotal: item.cores.total,
            coresPhysical: item.cores.physical,
            speedGzMin: item.speedGhz.min,
            speedGzMax: item.speedGhz.max,
            socket: item.socket,
            sizeMeasure: item.size.measure,
            sizeValue: item.size.value,
            cacheL3Measure: item.cacheL3.measure,
            cacheL3Size: item.cacheL3.size,
            thermalDesignPowerMeasure: item.thermalDesignPower.measure,
            thermalDesignPowerValue: item.thermalDesignPower.value,
            released: (item.released != null) ? item.released : ''
        })))).toDisk('../database/cpu.csv'));
        
        return data;
    }
}

// Run the controller
new Builder();

// For readme list items: require('./database/cpu.json').list.map(item => item.name).sort().join(', ');
