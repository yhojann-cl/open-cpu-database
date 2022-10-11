# Open CPU Database

A complete universal json CPU database for developers.
Please help us keep this database up to date through pull request contributions.


## Supported

- Architectures: `x86_64`.


## Structure

In json format the root data is:

- `root.version`: Version of the database. The structure can be changed in each major version.
- `root.list`: Is the list of CPU items separated by each architecture.

For each CPU item the format is:

| Data type | Key name                     | Description                                           |
|-----------|------------------------------|-------------------------------------------------------|
| `String`  | `name`                       | Full name of the CPU model.                           |
| `String`  | `codename`                   | Codename of the CPU.                                  |
| `Integer` | `cores.total`                | Total of cores (physical and virtual).                |
| `Integer` | `cores.physical`             | Total of physical cores.                              |
| `Integer` | `speedGhz.min`               | Minimal speed in Ghz.                                 |
| `Integer` | `speedGhz.max`               | Maximum speed in Ghz.                                 |
| `String`  | `socket`                     | Physical socket model type.                           | 
| `Integer` | `size`                       | Size of the physical CPU.                             |
| `String`  | `size.measure`               | Measure of the size of CPU (usually in `nanometers`). |
| `Integer` | `size.value`                 | Value of the size of CPU (usually in `nanometers`).   |
| `String`  | `cacheL3.measure`            | Measure of size of Level 3 Cache                      |
| `Integer` | `cacheL3.size`               | Size of Level 3 Cache                                 |
| `String`  | `thermalDesignPower.measure` | Measure of Thermal Design Power (usually in `watts`). |
| `Integer` | `thermalDesignPower.value`   | Value of Thermal Design Power (usually in `watts`).   |
| `String`  | `released`                   | Released date in `yyyy-mm-dd` format.                 |

