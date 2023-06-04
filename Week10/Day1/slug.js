var slugify = require('slugify')

slugify('some string') // some-string

// if you prefer something other than '-' as separator
const result = slugify('some string',{replacement:'*'}) // some_string
console.log(result)