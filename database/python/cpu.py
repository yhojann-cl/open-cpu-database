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
    f' - name: {self.name}\n'
    f' - codename: {self.codename}\n'
    f' - architecture: {self.architecture}\n'
    f' - cores: {self.cores}\n'
    f' - speed: {self.speed}\n'
    f' - socket: {self.socket}\n'
    f' - technologyNode: {self.technologyNode}\n'
    f' - cacheL3: {self.cacheL3}\n'
    f' - thermalDesignPower: {self.thermalDesignPower}\n'
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

# CPU Repository. Example of usage: `cpu = CPURepository.findByName('Milan-X')`
class CPURepository:
  items: list[CPU] = [
    CPU(
      name='EPYC 7373X',
      codename='Milan-X',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=3.05, max=3.8),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=768),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=240),
      released='2022-03-22'
    ),
    CPU(
      name='EPYC 7473X',
      codename='Milan-X',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.8, max=3.7),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=768),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=240),
      released='2022-03-22'
    ),
    CPU(
      name='EPYC 7543',
      codename='Milan',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.8, max=3.7),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=225),
      released='2021-03-15'
    ),
    CPU(
      name='EPYC 7573X',
      codename='Milan-X',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.8, max=3.6),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=768),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2022-03-22'
    ),
    CPU(
      name='EPYC 75F3',
      codename='Milan',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.95, max=4),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2021-03-15'
    ),
    CPU(
      name='EPYC 7643',
      codename='Milan',
      architecture='x86_64',
      cores=CPUCores(total=96, physical=48),
      speed=CPUSpeed(min=2.3, max=3.6),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=225),
      released='2021-03-15'
    ),
    CPU(
      name='EPYC 7663',
      codename='Milan',
      architecture='x86_64',
      cores=CPUCores(total=112, physical=56),
      speed=CPUSpeed(min=2, max=3.5),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=240),
      released='2021-03-15'
    ),
    CPU(
      name='EPYC 7713',
      codename='Milan',
      architecture='x86_64',
      cores=CPUCores(total=128, physical=64),
      speed=CPUSpeed(min=2, max=3.675),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=225),
      released='2021-03-15'
    ),
    CPU(
      name='EPYC 7713P',
      codename='Milan',
      architecture='x86_64',
      cores=CPUCores(total=128, physical=64),
      speed=CPUSpeed(min=2, max=3.675),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=225),
      released='2021-03-15'
    ),
    CPU(
      name='EPYC 7763',
      codename='Milan',
      architecture='x86_64',
      cores=CPUCores(total=128, physical=64),
      speed=CPUSpeed(min=2.45, max=3.5),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2021-03-15'
    ),
    CPU(
      name='EPYC 7773X',
      codename='Milan-X',
      architecture='x86_64',
      cores=CPUCores(total=128, physical=64),
      speed=CPUSpeed(min=2.2, max=3.5),
      socket='SP3',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=768),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2022-03-22'
    ),
    CPU(
      name='Ryzen 3 4100',
      codename='Renoir',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=3.8, max=4),
      socket='AM4',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-04-04'
    ),
    CPU(
      name='Ryzen 5 4500',
      codename='Renoir',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3.6, max=4.1),
      socket='AM4',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-04-04'
    ),
    CPU(
      name='Ryzen 5 5500',
      codename='Cezanne',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3.6, max=4.2),
      socket='AM4',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-04-04'
    ),
    CPU(
      name='Ryzen 5 5600',
      codename='Vermeer',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3.5, max=4.4),
      socket='AM4',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=32),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-04-20'
    ),
    CPU(
      name='Ryzen 7 5700X',
      codename='Vermeer',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.4, max=4.6),
      socket='AM4',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=32),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-04-04'
    ),
    CPU(
      name='Ryzen 7 5800X3D',
      codename='Vermeer',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.4, max=4.5),
      socket='AM4',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=96),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=105),
      released='2022-04-20'
    ),
    CPU(
      name='Ryzen Threadripper 5990X',
      codename='Chagall',
      architecture='x86_64',
      cores=CPUCores(total=128, physical=64),
      speed=CPUSpeed(min=2.5, max=4.45),
      socket='TRX4',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released=None
    ),
    CPU(
      name='Ryzen Threadripper PRO 5945WX',
      codename='Chagall PRO',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=12),
      speed=CPUSpeed(min=4.1, max=4.5),
      socket='WRX8',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=64),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2022-03-08'
    ),
    CPU(
      name='Ryzen Threadripper PRO 5955WX',
      codename='Chagall PRO',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=4, max=4.5),
      socket='WRX8',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=64),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2022-03-08'
    ),
    CPU(
      name='Ryzen Threadripper PRO 5965WX',
      codename='Chagall PRO',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=3.8, max=4.5),
      socket='WRX8',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=128),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2022-03-08'
    ),
    CPU(
      name='Ryzen Threadripper PRO 5975WX',
      codename='Chagall PRO',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=3.6, max=4.5),
      socket='WRX8',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=128),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2022-03-08'
    ),
    CPU(
      name='Ryzen Threadripper PRO 5995WX',
      codename='Chagall PRO',
      architecture='x86_64',
      cores=CPUCores(total=128, physical=64),
      speed=CPUSpeed(min=2.7, max=4.5),
      socket='WRX8',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=256),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=280),
      released='2022-03-08'
    ),
    CPU(
      name='Core i3-10105F',
      codename='Comet Lake-R',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=3.7, max=4.4),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=6),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-03-16'
    ),
    CPU(
      name='Core i3-12100F',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=3.3, max=4.3),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=58),
      released='2022-01-01'
    ),
    CPU(
      name='Core i5-11400F',
      codename='Rocket Lake',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.6, max=4.4),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-03-16'
    ),
    CPU(
      name='Core i5-11600',
      codename='Rocket Lake',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.8, max=4.8),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-03-16'
    ),
    CPU(
      name='Core i5-11600KF',
      codename='Rocket Lake',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3.9, max=4.9),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2021-03-16'
    ),
    CPU(
      name='Core i5-12400F',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.5, max=4.4),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-01-04'
    ),
    CPU(
      name='Core i5-12490F',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3, max=4.6),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=20),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022'
    ),
    CPU(
      name='Core i5-12600KF',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=10),
      speed=CPUSpeed(min=3.7, max=4.9),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=20),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2021-11-04'
    ),
    CPU(
      name='Core i5-13600KF',
      codename='Raptor Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=3.5, max=5.1),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2022-09-27'
    ),
    CPU(
      name='Core i7-11700F',
      codename='Rocket Lake',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2.5, max=4.9),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-03-16'
    ),
    CPU(
      name='Core i7-11700KF',
      codename='Rocket Lake',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.6, max=5),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2021-03-16'
    ),
    CPU(
      name='Core i7-12700F',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=12),
      speed=CPUSpeed(min=3.3, max=4.9),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=25),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-01-04'
    ),
    CPU(
      name='Core i7-12700KF',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=12),
      speed=CPUSpeed(min=3.6, max=5),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=25),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2021-11-04'
    ),
    CPU(
      name='Core i7-13700KF',
      codename='Raptor Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=3.4, max=5.4),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2022-09-27'
    ),
    CPU(
      name='Core i9-11900F',
      codename='Rocket Lake',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2.5, max=5.2),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-03-16'
    ),
    CPU(
      name='Core i9-11900KF',
      codename='Rocket Lake',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.5, max=5.3),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2021-03-16'
    ),
    CPU(
      name='Core i9-12900F',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=2.4, max=5.1),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-01-04'
    ),
    CPU(
      name='Core i9-12900KF',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=3.2, max=5.2),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2021-11-04'
    ),
    CPU(
      name='Core i9-13900KF',
      codename='Raptor Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=24),
      speed=CPUSpeed(min=3, max=5.8),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2022-09-27'
    ),
    CPU(
      name='Xeon E-2314',
      codename='Rocket Lake-E',
      architecture='x86_64',
      cores=CPUCores(total=4, physical=4),
      speed=CPUSpeed(min=2.8, max=4.5),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-09-08'
    ),
    CPU(
      name='Xeon E-2334',
      codename='Rocket Lake-E',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=3.4, max=4.8),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-09-08'
    ),
    CPU(
      name='Xeon E-2336',
      codename='Rocket Lake-E',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.9, max=4.8),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-09-08'
    ),
    CPU(
      name='Xeon E-2378',
      codename='Rocket Lake-E',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2.6, max=4.8),
      socket='1200',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2021-09-08'
    ),
    CPU(
      name='Xeon Gold 5315Y',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.2, max=3.6),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=140),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 5317',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=12),
      speed=CPUSpeed(min=3, max=3.6),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 5318H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=36, physical=18),
      speed=CPUSpeed(min=2.5, max=3.8),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=24.75),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 5318N',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.1, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 5318S',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.1, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=165),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 5318Y',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.1, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=165),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 5320',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=52, physical=26),
      speed=CPUSpeed(min=2.2, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=39),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=185),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 5320H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=40, physical=20),
      speed=CPUSpeed(min=2.4, max=4.2),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=27.5),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 5320T',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=40, physical=20),
      speed=CPUSpeed(min=2.3, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6312U',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.4, max=3.6),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=185),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6314U',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.3, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=48),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=205),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6326',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=2.9, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=185),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6328H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=2.8, max=4.3),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=22),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=165),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6328HL',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=2.8, max=4.3),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=22),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=165),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6330',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=56, physical=28),
      speed=CPUSpeed(min=2, max=3.1),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=42),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=205),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6330H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2, max=3.7),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=33),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6334',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.6, max=3.7),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=165),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6336Y',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.4, max=3.6),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=185),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6338N',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.2, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=48),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=185),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6338T',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.1, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=165),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6342',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.8, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=230),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6346',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=3.1, max=3.6),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=205),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6348',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=56, physical=28),
      speed=CPUSpeed(min=2.6, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=42),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=235),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6348H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=2.3, max=4.2),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=33),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=165),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Gold 6354',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=36, physical=18),
      speed=CPUSpeed(min=3, max=3.6),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=39),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=205),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8351N',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=72, physical=36),
      speed=CPUSpeed(min=2.4, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=54),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=225),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8352M',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.3, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=48),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=185),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8352S',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.2, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=48),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=205),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8352V',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=72, physical=36),
      speed=CPUSpeed(min=2.5, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=54),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=195),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8353H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=36, physical=18),
      speed=CPUSpeed(min=2.5, max=3.8),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=24.75),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8354H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=36, physical=18),
      speed=CPUSpeed(min=3.1, max=4.3),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=24.75),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=205),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8356H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.9, max=4.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=35.75),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=190),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8358',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.6, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=48),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=250),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8358P',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.6, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=48),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=240),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8360H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=3, max=4.2),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=33),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=225),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8360HL',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=3, max=4.2),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=33),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=225),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8360Y',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=72, physical=36),
      speed=CPUSpeed(min=2.4, max=3.5),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=54),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=250),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8362',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.8, max=3.6),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=48),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=265),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8368',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=76, physical=38),
      speed=CPUSpeed(min=2.4, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=57),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=270),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8368Q',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=76, physical=38),
      speed=CPUSpeed(min=2.6, max=3.7),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=57),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=270),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8376H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=56, physical=28),
      speed=CPUSpeed(min=2.6, max=4.3),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=38.5),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=205),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8376HL',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=56, physical=28),
      speed=CPUSpeed(min=2.6, max=4.3),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=38.5),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=205),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8380',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=80, physical=40),
      speed=CPUSpeed(min=2.3, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=60),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=270),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8380H',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=56, physical=28),
      speed=CPUSpeed(min=2.9, max=4.3),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=38.5),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=250),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Platinum 8380HL',
      codename='Cooper Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=56, physical=28),
      speed=CPUSpeed(min=2.9, max=4.3),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=14),
      cacheL3=CPUCache(unit='MB', size=38.5),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=250),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Silver 4309Y',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2.8, max=3.6),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=105),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Silver 4310',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=12),
      speed=CPUSpeed(min=2.1, max=3.3),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=120),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Silver 4310T',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=10),
      speed=CPUSpeed(min=2.3, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=15),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=105),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Silver 4314',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=2.4, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=135),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon Silver 4316',
      codename='Ice Lake-SP',
      architecture='x86_64',
      cores=CPUCores(total=40, physical=20),
      speed=CPUSpeed(min=2.3, max=3.4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2021-04-06'
    ),
    CPU(
      name='Xeon W-3323',
      codename='Ice Lake-W',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=12),
      speed=CPUSpeed(min=3.5, max=4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=220),
      released='2021-07-29'
    ),
    CPU(
      name='Xeon W-3335',
      codename='Ice Lake-W',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=3.4, max=4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=250),
      released='2021-07-29'
    ),
    CPU(
      name='Xeon W-3345',
      codename='Ice Lake-W',
      architecture='x86_64',
      cores=CPUCores(total=48, physical=24),
      speed=CPUSpeed(min=3, max=4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=250),
      released='2021-07-29'
    ),
    CPU(
      name='Xeon W-3365',
      codename='Ice Lake-W',
      architecture='x86_64',
      cores=CPUCores(total=64, physical=32),
      speed=CPUSpeed(min=2.7, max=4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=48),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=270),
      released='2021-07-29'
    ),
    CPU(
      name='Xeon W-3375',
      codename='Ice Lake-W',
      architecture='x86_64',
      cores=CPUCores(total=76, physical=38),
      speed=CPUSpeed(min=2.5, max=4),
      socket='4189',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=57),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=270),
      released='2021-07-29'
    ),
    CPU(
      name='Ryzen 3 5125C',
      codename='Cezanne-U',
      architecture='x86_64',
      cores=CPUCores(total=4, physical=2),
      speed=CPUSpeed(min=3, max=3),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-05-05'
    ),
    CPU(
      name='Ryzen 3 5425C',
      codename='Cezanne-U',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=2.7, max=4.1),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-05-05'
    ),
    CPU(
      name='Ryzen 3 5425U',
      codename='Barcelo',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=2.7, max=4.1),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-01-06'
    ),
    CPU(
      name='Ryzen 3 PRO 5475U',
      codename='Cezanne-U',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=2.7, max=4.1),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 5 5625C',
      codename='Cezanne-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.3, max=4.3),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-05-05'
    ),
    CPU(
      name='Ryzen 5 5625U',
      codename='Barcelo',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.3, max=4.3),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-01-06'
    ),
    CPU(
      name='Ryzen 5 6600H',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3.3, max=4.5),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 5 6600HS',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3.3, max=4.5),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 5 6600U',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.9, max=4.5),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 5 7600X',
      codename='Raphael',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=4.7, max=5.3),
      socket='AM5',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=5),
      cacheL3=CPUCache(unit='MB', size=32),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=105),
      released='2022-09-27'
    ),
    CPU(
      name='Ryzen 5 PRO 5675U',
      codename='Cezanne-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.3, max=4.3),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 5 PRO 6650H',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3.3, max=4.5),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 5 PRO 6650HS',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=3.3, max=4.5),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 5 PRO 6650U',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.9, max=4.5),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 7 5825C',
      codename='Cezanne-U',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2, max=4.5),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-05-05'
    ),
    CPU(
      name='Ryzen 7 5825U',
      codename='Barcelo',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2, max=4.5),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-01-06'
    ),
    CPU(
      name='Ryzen 7 6800H',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.2, max=4.7),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 7 6800HS',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.2, max=4.7),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 7 6800U',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2.7, max=4.7),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 7 7700X',
      codename='Raphael',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=4.5, max=5.4),
      socket='AM5',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=5),
      cacheL3=CPUCache(unit='MB', size=32),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=105),
      released='2022-09-27'
    ),
    CPU(
      name='Ryzen 7 PRO 5875U',
      codename='Cezanne-U',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2, max=4.5),
      socket='FP6',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=7),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 7 PRO 6850H',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.2, max=4.7),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 7 PRO 6850HS',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.2, max=4.7),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 7 PRO 6850U',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=2.7, max=4.7),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 9 6900HS',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.3, max=4.9),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 9 6900HX',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.3, max=4.9),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 9 6980HS',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.3, max=5),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 9 6980HX',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.3, max=5),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Ryzen 9 7900X',
      codename='Raphael',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=12),
      speed=CPUSpeed(min=4.7, max=5.6),
      socket='AM5',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=5),
      cacheL3=CPUCache(unit='MB', size=64),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=170),
      released='2022-09-27'
    ),
    CPU(
      name='Ryzen 9 7950X',
      codename='Raphael',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=16),
      speed=CPUSpeed(min=4.5, max=5.7),
      socket='AM5',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=5),
      cacheL3=CPUCache(unit='MB', size=64),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=170),
      released='2022-09-27'
    ),
    CPU(
      name='Ryzen 9 PRO 6950H',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.3, max=4.9),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-04-19'
    ),
    CPU(
      name='Ryzen 9 PRO 6950HS',
      codename='Rembrandt',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=8),
      speed=CPUSpeed(min=3.3, max=4.9),
      socket='FP7',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=6),
      cacheL3=CPUCache(unit='MB', size=16),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-04-19'
    ),
    CPU(
      name='Celeron 7300',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=6, physical=5),
      speed=CPUSpeed(min=1, max=1),
      socket='BGA 1781',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=9),
      released='2022-02-23'
    ),
    CPU(
      name='Celeron 7305',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=6, physical=5),
      speed=CPUSpeed(min=1.1, max=1.1),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Celeron G6900',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=2, physical=2),
      speed=CPUSpeed(min=3.4, max=3.4),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=4),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=46),
      released='2022-01-04'
    ),
    CPU(
      name='Celeron G6900E',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=2, physical=2),
      speed=CPUSpeed(min=3, max=3),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=4),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=46),
      released='2022-01-04'
    ),
    CPU(
      name='Celeron G6900T',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=2, physical=2),
      speed=CPUSpeed(min=2.8, max=2.8),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=4),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-04'
    ),
    CPU(
      name='Celeron G6900TE',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=2, physical=2),
      speed=CPUSpeed(min=2.4, max=2.4),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=4),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-04'
    ),
    CPU(
      name='Core i3-12100',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=3.3, max=4.3),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=60),
      released='2022-01-04'
    ),
    CPU(
      name='Core i3-12100E',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=3.2, max=4.2),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=60),
      released='2022-01-04'
    ),
    CPU(
      name='Core i3-12100T',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=2.2, max=4.1),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Core i3-12100TE',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=2.1, max=4),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Core i3-1210U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=6),
      speed=CPUSpeed(min=1, max=4.4),
      socket='BGA 1781',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=10),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=9),
      released='2022-02-23'
    ),
    CPU(
      name='Core i3-1215U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=6),
      speed=CPUSpeed(min=1.2, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=10),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Core i3-1215U (IPU)',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=6),
      speed=CPUSpeed(min=1.2, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=10),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Core i3-1220P',
      codename='Alder Lake-P',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.5, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=28),
      released='2022-02-23'
    ),
    CPU(
      name='Core i3-12300',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=3.5, max=4.4),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=60),
      released='2022-01-01'
    ),
    CPU(
      name='Core i3-12300HE',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=8),
      speed=CPUSpeed(min=1.9, max=4.3),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Core i3-12300T',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=8, physical=4),
      speed=CPUSpeed(min=2.3, max=4.2),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Core i5-1230U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1, max=4.4),
      socket='BGA 1781',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=9),
      released='2022-02-23'
    ),
    CPU(
      name='Core i5-1235U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.3, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Core i5-1235U (IPU)',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.3, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Core i5-12400',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=2.5, max=4.4),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-01-04'
    ),
    CPU(
      name='Core i5-12400T',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=6),
      speed=CPUSpeed(min=1.8, max=4.2),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Core i5-1240P',
      codename='Alder Lake-P',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=12),
      speed=CPUSpeed(min=1.7, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=28),
      released='2022-02-23'
    ),
    CPU(
      name='Core i5-1240U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.1, max=4.4),
      socket='BGA 1781',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=9),
      released='2022-02-23'
    ),
    CPU(
      name='Core i5-12450H',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=8),
      speed=CPUSpeed(min=2, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Core i5-12450HX',
      codename='Alder Lake-HX',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=8),
      speed=CPUSpeed(min=2.4, max=4.4),
      socket='BGA 1964',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=55),
      released='2022-05-10'
    ),
    CPU(
      name='Core i5-1245U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.6, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Core i5-12500H',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=12),
      speed=CPUSpeed(min=2.5, max=4.5),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Core i5-1250P',
      codename='Alder Lake-P',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=12),
      speed=CPUSpeed(min=1.7, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=28),
      released='2022-02-23'
    ),
    CPU(
      name='Core i5-12600H',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=12),
      speed=CPUSpeed(min=2.7, max=4.5),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Core i5-12600HX',
      codename='Alder Lake-HX',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=12),
      speed=CPUSpeed(min=2.5, max=4.6),
      socket='BGA 1964',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=55),
      released='2022-05-10'
    ),
    CPU(
      name='Core i5-13500',
      codename='Raptor Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=10),
      speed=CPUSpeed(min=2.5, max=4.6),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=20),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022'
    ),
    CPU(
      name='Core i5-13600K',
      codename='Raptor Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=3.5, max=5.1),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2022-09-27'
    ),
    CPU(
      name='Core i7-1250U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.1, max=4.7),
      socket='BGA 1781',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=9),
      released='2022-02-23'
    ),
    CPU(
      name='Core i7-1255U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.7, max=4.7),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Core i7-1260P',
      codename='Alder Lake-P',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=12),
      speed=CPUSpeed(min=2.1, max=4.7),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=28),
      released='2022-02-23'
    ),
    CPU(
      name='Core i7-1260U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.1, max=4.7),
      socket='BGA 1781',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=9),
      released='2022-02-23'
    ),
    CPU(
      name='Core i7-12650H',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=10),
      speed=CPUSpeed(min=2.3, max=4.7),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Core i7-12650HX',
      codename='Alder Lake-HX',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=2, max=4.7),
      socket='BGA 1964',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=55),
      released='2022-05-10'
    ),
    CPU(
      name='Core i7-1265U',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=12, physical=10),
      speed=CPUSpeed(min=1.8, max=4.8),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=12),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Core i7-12700E',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=12),
      speed=CPUSpeed(min=2.1, max=4.8),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=25),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-01-01'
    ),
    CPU(
      name='Core i7-12700H',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=2.3, max=4.7),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Core i7-12700T',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=12),
      speed=CPUSpeed(min=1.4, max=4.7),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=25),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Core i7-12700TE',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=12),
      speed=CPUSpeed(min=1.4, max=4.6),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=25),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-01'
    ),
    CPU(
      name='Core i7-1270P',
      codename='Alder Lake-P',
      architecture='x86_64',
      cores=CPUCores(total=16, physical=12),
      speed=CPUSpeed(min=2.2, max=4.8),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=18),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=28),
      released='2022-02-23'
    ),
    CPU(
      name='Core i7-12800H',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=2.4, max=4.8),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Core i7-12800HE',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=2.4, max=4.6),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-01'
    ),
    CPU(
      name='Core i7-12800HX',
      codename='Alder Lake-HX',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=2, max=4.8),
      socket='BGA 1964',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=25),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=55),
      released='2022-05-10'
    ),
    CPU(
      name='Core i7-1280P',
      codename='Alder Lake-P',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=1.8, max=4.8),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=28),
      released='2022-02-23'
    ),
    CPU(
      name='Core i7-12850HX',
      codename='Alder Lake-HX',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=2.1, max=4.8),
      socket='BGA 1964',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=25),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=55),
      released='2022-05-10'
    ),
    CPU(
      name='Core i7-13700K',
      codename='Raptor Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=3.4, max=5.4),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2022-09-27'
    ),
    CPU(
      name='Core i9-12900',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=2.4, max=5.1),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-01-04'
    ),
    CPU(
      name='Core i9-12900E',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=2.3, max=5),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=65),
      released='2022-01-04'
    ),
    CPU(
      name='Core i9-12900H',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=2.5, max=5),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-04'
    ),
    CPU(
      name='Core i9-12900HK',
      codename='Alder Lake-H',
      architecture='x86_64',
      cores=CPUCores(total=20, physical=14),
      speed=CPUSpeed(min=2.5, max=5),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=24),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=45),
      released='2022-01-04'
    ),
    CPU(
      name='Core i9-12900HX',
      codename='Alder Lake-HX',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=2.3, max=5),
      socket='BGA 1964',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=55),
      released='2022-05-10'
    ),
    CPU(
      name='Core i9-12900KS',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=3.4, max=5.5),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=150),
      released='2022-04-05'
    ),
    CPU(
      name='Core i9-12900T',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=1.4, max=4.9),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-04'
    ),
    CPU(
      name='Core i9-12900TE',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=1.1, max=4.8),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-04'
    ),
    CPU(
      name='Core i9-12950HX',
      codename='Alder Lake-HX',
      architecture='x86_64',
      cores=CPUCores(total=24, physical=16),
      speed=CPUSpeed(min=2.3, max=5),
      socket='BGA 1964',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=30),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=55),
      released='2022-05-10'
    ),
    CPU(
      name='Core i9-13900',
      codename='Raptor Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=24),
      speed=CPUSpeed(min=2, max=5.6),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2022'
    ),
    CPU(
      name='Core i9-13900K',
      codename='Raptor Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=32, physical=24),
      speed=CPUSpeed(min=3, max=5.8),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=36),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=125),
      released='2022-09-27'
    ),
    CPU(
      name='Pentium 8500',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=6, physical=5),
      speed=CPUSpeed(min=1, max=4.4),
      socket='BGA 1781',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=9),
      released='2022-02-23'
    ),
    CPU(
      name='Pentium 8505',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=6, physical=5),
      speed=CPUSpeed(min=1.2, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Pentium 8505 (IPU)',
      codename='Alder Lake-U',
      architecture='x86_64',
      cores=CPUCores(total=6, physical=5),
      speed=CPUSpeed(min=1.2, max=4.4),
      socket='BGA 1744',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=8),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=15),
      released='2022-02-23'
    ),
    CPU(
      name='Pentium Gold G7400',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=4, physical=2),
      speed=CPUSpeed(min=3.7, max=3.7),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=6),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=46),
      released='2022-01-04'
    ),
    CPU(
      name='Pentium Gold G7400E',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=4, physical=2),
      speed=CPUSpeed(min=3.6, max=3.6),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=6),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=46),
      released='2022-01-04'
    ),
    CPU(
      name='Pentium Gold G7400T',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=4, physical=2),
      speed=CPUSpeed(min=3.1, max=3.1),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=6),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-04'
    ),
    CPU(
      name='Pentium Gold G7400TE',
      codename='Alder Lake-S',
      architecture='x86_64',
      cores=CPUCores(total=4, physical=2),
      speed=CPUSpeed(min=3, max=3),
      socket='1700',
      technologyNode=CPUTechnologyNode(unit='nanometers', value=10),
      cacheL3=CPUCache(unit='MB', size=6),
      thermalDesignPower=CPUThermalDesignPower(unit='watts', value=35),
      released='2022-01-04'
    )
  ]

  # Find CPU by model name, or thrown a StopIteration exception if not found.
  @classmethod
  def findByName(cls, name: str) -> CPU:
    return next(item for item in cls.items if item.name == name)

  # Find CPU by model codename, or thrown a StopIteration exception if not found.
  @classmethod
  def findByCodename(cls, codename: str) -> CPU:
    return next(item for item in cls.items if item.codename == codename)