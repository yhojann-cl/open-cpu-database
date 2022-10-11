# Open CPU Database

A complete universal json CPU database for developers.
Please help us keep this database up to date through pull request contributions.


## Supported

- Architectures: `x86_64`.


## Structure

In json format the root data is:

| Data type | Key name          | Description                                                                  |
|-----------|-------------------|------------------------------------------------------------------------------|
| `String`  | `root.version`    | Version of the database. The structure can be changed in each major version. |
| `String`  | `root.repository` | Path of the repository of the database (for upgrades).                       |
| `List`    | `root.list`       | Is the list of CPU items separated by each architecture.                     |

For each CPU item the format is:

| Data type | Key name                     | Description                                           |
|-----------|------------------------------|-------------------------------------------------------|
| `String`  | `name`                       | Full name of the CPU model.                           |
| `String`  | `codename`                   | Codename of the CPU.                                  |
| `Integer` | `cores.total`                | Total of cores (physical and virtual).                |
| `Integer` | `cores.physical`             | Total of physical cores.                              |
| `Float`   | `speedGhz.min`               | Minimal speed in Ghz.                                 |
| `Float`   | `speedGhz.max`               | Maximum speed in Ghz.                                 |
| `String`  | `socket`                     | Physical socket model type.                           | 
| `Integer` | `size`                       | Size of the physical CPU.                             |
| `String`  | `size.measure`               | Measure of the size of CPU (usually in `nanometers`). |
| `Integer` | `size.value`                 | Value of the size of CPU (usually in `nanometers`).   |
| `String`  | `cacheL3.measure`            | Measure of size of Level 3 Cache                      |
| `Integer` | `cacheL3.size`               | Size of Level 3 Cache                                 |
| `String`  | `thermalDesignPower.measure` | Measure of Thermal Design Power (usually in `watts`). |
| `Integer` | `thermalDesignPower.value`   | Value of Thermal Design Power (usually in `watts`).   |
| `String`  | `released`                   | Released date in `yyyy-mm-dd` format.                 |

Example:

```json
{
    "version": "0.0.0-stable",
    "repository": "https://github.com/yhojann-cl/open-cpu-database",
    "list": {
        "x86_64": [
            {
                "name": "EPYC 7373X",
                "codename": "Milan-X",
                "cores": {
                    "total": 32,
                    "physical": 16
                },
                "speedGhz": {
                    "min": 3.05,
                    "max": 3.8
                },
                "socket": "SP3",
                "size": {
                    "measure": "nanometers",
                    "value": 7
                },
                "cacheL3": {
                    "measure": "MB",
                    "size": 768
                },
                "thermalDesignPower": {
                    "measure": "watts",
                    "value": 240
                },
                "released": "2022-03-22"
            }
        ]
    }
}
```
