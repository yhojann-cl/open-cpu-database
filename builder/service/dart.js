const fs = require('fs');

class DartBuilder {

    async build(data, basePath) {
        console.log('Generating dart repository project ...');

        const filePath = `${basePath}/src/cpu.dart`;

        if(fs.existsSync(filePath))
            fs.unlink(filePath, e => { if(e) throw e });

        fs.writeFile(filePath, `

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

        `.trim(), (e) => { if(e) throw e });
        return data;
    }
}

module.exports = DartBuilder;