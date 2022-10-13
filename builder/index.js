const fs = require('fs');
const { unlink } = require('fs/promises');
const ObjectsToCsv = require('objects-to-csv');


class Builder{

    constructor() {
        console.log('Loading main database ...');
        this.loadMainDatabase()
        .then(data => this.makeDart(data))
        .then(data => this.makeC(data))
        .then(data => this.makePython(data))
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

class CPUTechnologyNode {
  final String unit;
  final double value;

  const CPUTechnologyNode({ required this.unit, required this.value });
}

class CPUCache {
  final String unit;
  final double size;

  const CPUCache({ required this.unit, required this.size });
}

class CPUThermalDesignPower {
  final String unit;
  final double value;

  const CPUThermalDesignPower({ required this.unit, required this.value });
}

class CPU {
  final String name;
  final String codename;
  final String architecture;
  final CPUCores cores;
  final CPUSpeed speed;
  final String socket;
  final CPUTechnologyNode technologyNode;
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
    required this.technologyNode,
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
      technologyNode: const CPUTechnologyNode(unit: '${item.technologyNode.unit}', value: ${item.technologyNode.value}),
      cacheL3: const CPUCache(unit: '${item.cacheL3.unit}', size: ${item.cacheL3.size}),
      thermalDesignPower: const CPUThermalDesignPower(unit: '${item.thermalDesignPower.unit}', value: ${item.thermalDesignPower.value}),
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

        `.trim(), (e) => { if(e) throw e }));

        return data;
    }

    async makePython(data) {
      console.log('Generating Python repository project ...');

      await this.deleteIfExist('../database/python/cpu.py')
      .then(() => fs.writeFile('../database/python/cpu.py', `

from typing import Final, Optional

class _ValueAndUnit:
  value: Final[float]
  unit: Final[str]

  def __init__(self, value: float, unit: str) -> None:
    self.value = value
    self.unit = unit

  def __str__(self) -> str:
    return f'{self.value} {self.unit}'

  def __repr__(self) -> str:
    return f'{__class__.__name__}(value={self.value}, unit={self.unit})'

class CPUCores:
  total: Final[int]
  physical: Final[int]

  def __init__(self, total: int, physical: int) -> None:
    self.total = total
    self.physical = physical

  def __str__(self) -> str:
    return f'{self.total} total cores, {self.physical} physical cores'

  def __repr__(self) -> str:
    return f'{__class__.__name__}(total={self.total}, physical={self.physical})'

class CPUSpeed:
  min: Final[float]
  max: Final[float]

  def __init__(self, min: float, max: float) -> None:
    self.min = min
    self.max = max

  def __str__(self) -> str:
    return f'{self.min} GHz min, {self.max} GHz max'

  def __repr__(self) -> str:
    return f'{__class__.__name__}(min={self.min}, max={self.max})'

class CPUTechnologyNode(_ValueAndUnit):
  pass

class CPUCache():
  size: Final[float]
  unit: Final[str]

  def __init__(self, size: float, unit: str) -> None:
    self.size = size
    self.unit = unit

  def __str__(self) -> str:
    return f'{self.size} {self.unit}'

  def __repr__(self) -> str:
    return f'{__class__.__name__}(size={self.size}, unit={self.unit})'

class CPUThermalDesignPower(_ValueAndUnit):
  pass

class CPU():
  name: Final[str]
  codename: Final[str]
  architecture: Final[str]
  cores: Final[CPUCores]
  speed: Final[CPUSpeed]
  socket: Final[str]
  technologyNode: Final[CPUTechnologyNode]
  cacheL3: Final[CPUCache]
  thermalDesignPower: Final[CPUThermalDesignPower]
  released: Final[Optional[str]]

  def __init__(self, name: str, codename: str, architecture: str, cores: CPUCores, speed: CPUSpeed, socket: str, technologyNode: CPUTechnologyNode, cacheL3: CPUCache, thermalDesignPower: CPUThermalDesignPower, released: Optional[str] = None):
    self.name = name
    self.codename = codename
    self.architecture = architecture
    self.cores = cores
    self.speed = speed
    self.socket = socket
    self.technologyNode = technologyNode
    self.cacheL3 = cacheL3
    self.thermalDesignPower = thermalDesignPower
    self.released = released

  def __str__(self):
    return (
    f' - name: {self.name}\\n'
    f' - codename: {self.codename}\\n'
    f' - architecture: {self.architecture}\\n'
    f' - cores: {self.cores}\\n'
    f' - speed: {self.speed}\\n'
    f' - socket: {self.socket}\\n'
    f' - technologyNode: {self.technologyNode}\\n'
    f' - cacheL3: {self.cacheL3}\\n'
    f' - thermalDesignPower: {self.thermalDesignPower}\\n'
    f' - released: {self.released if self.released else "unknown"}'
    )

  def __repr__(self):
    return ('CPU('
    f'name={self.name}, '
    f'codename={self.codename}, '
    f'architecture={self.architecture}, '
    f'cores={self.cores.__repr__()}, '
    f'speed={self.speed.__repr__()}, '
    f'socket={self.socket}, '
    f'technologyNode={self.technologyNode.__repr__()}, '
    f'cacheL3={self.cacheL3.__repr__()}, '
    f'thermalDesignPower={self.thermalDesignPower.__repr__()}, '
    f'released={self.released}'
    ')')

# CPU Repository. Example of usage: \`cpu = CPURepository.findByName('Milan-X')\`
class CPURepository:
  items: list[CPU] = [
    ${data.list.map(item => `
    CPU(
      name='${item.name}',
      codename='${item.codename}',
      architecture='${item.architecture}',
      cores=CPUCores(total=${item.cores.total}, physical=${item.cores.physical}),
      speed=CPUSpeed(min=${item.speedGhz.min}, max=${item.speedGhz.max}),
      socket='${item.socket}',
      technologyNode=CPUTechnologyNode(unit='${item.technologyNode.unit}', value=${item.technologyNode.value}),
      cacheL3=CPUCache(unit='${item.cacheL3.unit}', size=${item.cacheL3.size}),
      thermalDesignPower=CPUThermalDesignPower(unit='${item.thermalDesignPower.unit}', value=${item.thermalDesignPower.value}),
      released=${(item.released != null) ? `'${item.released}'` : `None`}
    )
    `.trim()).join(',\n    ')}
  ]

  # Find CPU by model name, or thrown a StopIteration exception if not found.
  @classmethod
  def findByName(cls, name: str) -> CPU:
    return next(item for item in cls.items if item.name == name)

  # Find CPU by model codename, or thrown a StopIteration exception if not found.
  @classmethod
  def findByCodename(cls, codename: str) -> CPU:
    return next(item for item in cls.items if item.codename == codename)

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
            technologyNodeUnit: item.technologyNode.unit,
            technologyNodeValue: item.technologyNode.value,
            cacheL3Unit: item.cacheL3.unit,
            cacheL3Size: item.cacheL3.size,
            thermalDesignPowerUnit: item.thermalDesignPower.unit,
            thermalDesignPowerValue: item.thermalDesignPower.value,
            released: (item.released != null) ? item.released : ''
        })))).toDisk('../database/cpu.csv'));

        return data;
    }
}

// Run the controller
new Builder();

// For readme list items: require('./database/cpu.json').list.map(item => item.name).sort().join(', ');
