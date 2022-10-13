const fs = require('fs');
const DartBuilder = require('./service/dart');
const CSVBuilder = require('./service/csv');
const CBuilder = require('./service/c');

class Builder{

    constructor() {
        const dartBuilder = new DartBuilder();
        const csvBuilder = new CSVBuilder();
        const cBuilder = new CBuilder();
        const pythonBuilder = new PythonBuilder();

        console.log('Loading main database ...');
        this.loadMainDatabase()
        .then(data => dartBuilder.build(data, '../implementation/dart'))
        .then(data => cBuilder.build(data, '../implementation/c'))
        .then(data => csvBuilder.build(data, '../database'))
        .catch(e => {
            console.log('Unable build files.');
            throw e;
        });
    }

    async loadMainDatabase() {
        let data = fs.readFileSync('../database/cpu.json');
        return JSON.parse(data);
    }
}

// Run the controller
new Builder();

// For readme list items: require('./database/cpu.json').list.map(item => item.name).sort().join(', ');
