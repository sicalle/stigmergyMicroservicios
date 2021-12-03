const mongoose = require('mongoose');

const registrationSchema = new mongoose.Schema({
  nombre: {
    type: String,
    trim: true,
  },
  tipoComida: {
    type: String,
    trim: true,
  },
  imagen: {
    type: String,
    trim: true,
  },
});

module.exports = mongoose.model('Registration', registrationSchema);
