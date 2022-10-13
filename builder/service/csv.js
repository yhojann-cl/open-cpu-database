const fs = require('fs');
const ObjectsToCsv = require("objects-to-csv");

class CSVBuilder {

    async build(data, basePath){
        console.log('Generating CSV repository project ...');

        const filePath = `${basePath}/cpu.csv`;

        if(fs.existsSync(filePath))
            fs.unlink(filePath, e => { if(e) throw e });

        new ObjectsToCsv(data.list.map(item => ({
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
        }))).toDisk(filePath);

        return data;
    }
}

module.exports = CSVBuilder;