# Open CPU Database

A complete universal json CPU database for developers.
Please help us keep this database up to date through pull request contributions.


## Structure

In json format the root data is:

| Data type | Key name          | Description                                                                  |
|-----------|-------------------|------------------------------------------------------------------------------|
| `String`  | `root.version`    | Version of the database. The structure can be changed in each major version. |
| `String`  | `root.repository` | Path of the repository of the database (for upgrades).                       |
| `List`    | `root.list`       | Is the list of CPU items.                                                    |

For each CPU item the format is:

| Data type | Key name                     | Description                                                 |
|-----------|------------------------------|-------------------------------------------------------------|
| `String`  | `name`                       | Full name of the CPU model.                                 |
| `String`  | `codename`                   | Codename of the CPU.                                        |
| `String`  | `architecture`               | Architecture of the CPU, by example `x86_64`.               |
| `Integer` | `cores.total`                | Total of cores (physical and virtual).                      |
| `Integer` | `cores.physical`             | Total of physical cores.                                    |
| `Float`   | `speedGhz.min`               | Minimal speed in Ghz.                                       |
| `Float`   | `speedGhz.max`               | Maximum speed in Ghz.                                       |
| `String`  | `socket`                     | Physical socket model type.                                 | 
| `Integer` | `size`                       | Size of the physical CPU.                                   |
| `String`  | `size.measure`               | Measure of the size of CPU (usually in `nanometers`).       |
| `Integer` | `size.value`                 | Value of the size of CPU (usually in `nanometers`).         |
| `String`  | `cacheL3.measure`            | Measure of size of Level 3 Cache (usually in `KB` or `MB`). |
| `Float`   | `cacheL3.size`               | Size of Level 3 Cache.                                      |
| `String`  | `thermalDesignPower.measure` | Measure of Thermal Design Power (usually in `watts`).       | 
| `Integer` | `thermalDesignPower.value`   | Value of Thermal Design Power (usually in `watts`).         |
| `String`  | `released`                   | Released date in `yyyy-mm-dd` format.                       |

Example of the json structure:

```json
{
    "version": "2.0.0-stable",
    "repository": "https://github.com/yhojann-cl/open-cpu-database",
    "list": [
        {
            "name": "EPYC 7373X",
            "codename": "Milan-X",
            "architecture": "x86_64",
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
```

## Supported

- **Architectures** supported: `x86_64`.
- **CPU Models** supported: Celeron 7300, Celeron 7305, Celeron G6900, Celeron G6900E, Celeron G6900T, Celeron G6900TE, Core i3-10105F, Core i3-12100, Core i3-12100E, Core i3-12100F, Core i3-12100T, Core i3-12100TE, Core i3-1210U, Core i3-1215U, Core i3-1215U (IPU), Core i3-1220P, Core i3-12300, Core i3-12300HE, Core i3-12300T, Core i5-11400F, Core i5-11600, Core i5-11600KF, Core i5-1230U, Core i5-1235U, Core i5-1235U (IPU), Core i5-12400, Core i5-12400F, Core i5-12400T, Core i5-1240P, Core i5-1240U, Core i5-12450H, Core i5-12450HX, Core i5-1245U, Core i5-12490F, Core i5-12500H, Core i5-1250P, Core i5-12600H, Core i5-12600HX, Core i5-12600KF, Core i5-13500, Core i5-13600K, Core i5-13600KF, Core i7-11700F, Core i7-11700KF, Core i7-1250U, Core i7-1255U, Core i7-1260P, Core i7-1260U, Core i7-12650H, Core i7-12650HX, Core i7-1265U, Core i7-12700E, Core i7-12700F, Core i7-12700H, Core i7-12700KF, Core i7-12700T, Core i7-12700TE, Core i7-1270P, Core i7-12800H, Core i7-12800HE, Core i7-12800HX, Core i7-1280P, Core i7-12850HX, Core i7-13700K, Core i7-13700KF, Core i9-11900F, Core i9-11900KF, Core i9-12900, Core i9-12900E, Core i9-12900F, Core i9-12900H, Core i9-12900HK, Core i9-12900HX, Core i9-12900KF, Core i9-12900KS, Core i9-12900T, Core i9-12900TE, Core i9-12950HX, Core i9-13900, Core i9-13900K, Core i9-13900KF, EPYC 7373X, EPYC 7473X, EPYC 7543, EPYC 7573X, EPYC 75F3, EPYC 7643, EPYC 7663, EPYC 7713, EPYC 7713P, EPYC 7763, EPYC 7773X, Pentium 8500, Pentium 8505, Pentium 8505 (IPU), Pentium Gold G7400, Pentium Gold G7400E, Pentium Gold G7400T, Pentium Gold G7400TE, Ryzen 3 4100, Ryzen 3 5125C, Ryzen 3 5425C, Ryzen 3 5425U, Ryzen 3 PRO 5475U, Ryzen 5 4500, Ryzen 5 5500, Ryzen 5 5600, Ryzen 5 5625C, Ryzen 5 5625U, Ryzen 5 6600H, Ryzen 5 6600HS, Ryzen 5 6600U, Ryzen 5 7600X, Ryzen 5 PRO 5675U, Ryzen 5 PRO 6650H, Ryzen 5 PRO 6650HS, Ryzen 5 PRO 6650U, Ryzen 7 5700X, Ryzen 7 5800X3D, Ryzen 7 5825C, Ryzen 7 5825U, Ryzen 7 6800H, Ryzen 7 6800HS, Ryzen 7 6800U, Ryzen 7 7700X, Ryzen 7 PRO 5875U, Ryzen 7 PRO 6850H, Ryzen 7 PRO 6850HS, Ryzen 7 PRO 6850U, Ryzen 9 6900HS, Ryzen 9 6900HX, Ryzen 9 6980HS, Ryzen 9 6980HX, Ryzen 9 7900X, Ryzen 9 7950X, Ryzen 9 PRO 6950H, Ryzen 9 PRO 6950HS, Ryzen Threadripper 5990X, Ryzen Threadripper PRO 5945WX, Ryzen Threadripper PRO 5955WX, Ryzen Threadripper PRO 5965WX, Ryzen Threadripper PRO 5975WX, Ryzen Threadripper PRO 5995WX, Xeon E-2314, Xeon E-2334, Xeon E-2336, Xeon E-2378, Xeon Gold 5315Y, Xeon Gold 5317, Xeon Gold 5318H, Xeon Gold 5318N, Xeon Gold 5318S, Xeon Gold 5318Y, Xeon Gold 5320, Xeon Gold 5320H, Xeon Gold 5320T, Xeon Gold 6312U, Xeon Gold 6314U, Xeon Gold 6326, Xeon Gold 6328H, Xeon Gold 6328HL, Xeon Gold 6330, Xeon Gold 6330H, Xeon Gold 6334, Xeon Gold 6336Y, Xeon Gold 6338N, Xeon Gold 6338T, Xeon Gold 6342, Xeon Gold 6346, Xeon Gold 6348, Xeon Gold 6348H, Xeon Gold 6354, Xeon Platinum 8351N, Xeon Platinum 8352M, Xeon Platinum 8352S, Xeon Platinum 8352V, Xeon Platinum 8353H, Xeon Platinum 8354H, Xeon Platinum 8356H, Xeon Platinum 8358, Xeon Platinum 8358P, Xeon Platinum 8360H, Xeon Platinum 8360HL, Xeon Platinum 8360Y, Xeon Platinum 8362, Xeon Platinum 8368, Xeon Platinum 8368Q, Xeon Platinum 8376H, Xeon Platinum 8376HL, Xeon Platinum 8380, Xeon Platinum 8380H, Xeon Platinum 8380HL, Xeon Silver 4309Y, Xeon Silver 4310, Xeon Silver 4310T, Xeon Silver 4314, Xeon Silver 4316, Xeon W-3323, Xeon W-3335, Xeon W-3345, Xeon W-3365 and Xeon W-3375.


## For pull requests

Add your changes to main database file located in `./database/cpu.json` only (CI action automatically generate all other files).
You can also create an issue to report new changes.
