const knex = require('knex');
const dotenv = require('dotenv');

dotenv.config()

const db = knex({
    client:pg,
    connection: {
        host:,
        port:,
        user:,
        password:,
        database:,
    }
})