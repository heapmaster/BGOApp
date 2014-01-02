console.log("Loading collections/countries.js");

App.Collections.CountryCollection = Backbone.Collection.extend({
  model: App.Models.Country,
  url: 'http://bgo.herokuapp.com/countries',
  parse: function(response) {
    return response.countries;
  }
});
