const express = require('express');
const mongoose = require('mongoose');

const router = express.Router();
const Registration = mongoose.model('Registration');

router.get('/', (req, res) => {
  Registration.find()
  .then((registrations) => {
    console.log(registrations[1])
    res.render('index', { title: 'Stigmergy - Restaurantes', registrations });
  })
  .catch(() => { res.send('Lo sentimos, ha ocurrido un error.'); });
});

router.post('/', (req, res) => {
  //console.log(req.body);
  const registration = new Registration(req.body);
  registration.save()
  .then(() => { 
    Registration.find()
  .then((registrations) => {
    console.log(registrations[1])
    res.render('index', { title: 'Stigmergy - Restaurantes', registrations });
  })
  .catch(() => { res.send('Lo sentimos, ha ocurrido un error.'); });
   })
  .catch((err) => {
    console.log(err);
    res.send('Sorry! Something went wrong.');
  });
 // 
});

//router.get('/restaurantes', (req, res) => {
  //Registration.find()
  //.then((registrations) => {
   // console.log(registrations)
    //res.render('restaurantes', { title: 'Listing registrations', registrations });
  //})
  //.catch(() => { res.send('Lo sentimos, ha ocurrido un error.'); });
//});

router.get('/restaurantes/:id', (req, res) => {
  Registration.find({ nombre: req.params.id }, function(err, registrations) {
    if (err)
        res.send(err);
    res.render('restaurantes', { title: `Stigmergy-${req.params.id}` , registrations });
});
});

router.get('/restaurantesNombre', (req, res) => {
  Registration.find({ nombre: req.query.nombre }, function(err, registrations) {
    if (err)
        res.send(err);
    res.render('restaurantes', { title: `Stigmergy-${req.query.nombre}` , registrations });
});
});

//router.get('/eliminar', (req, res) => {
 // Registration.deleteMany({ nombre: 'Mister Lee' }, function (err) {
   // if(err) console.log(err);
    //console.log("Successful deletion");
  //});
//});

module.exports = router;
