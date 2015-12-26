console.log("Loading models/match.js");

App.Models.Match = Backbone.Model.extend({
  url: 'http://www.bgolympics.com/matches',
  defaults: {
    players: []
  },
  initialize: function(option) {
    _.bindAll(this, 'get_standing_by_country');
  },
  get_standing_by_country: function(country_id) {
    var country = _.find(this.attributes.countries, function(country) { return country.countryId == country_id });
    
    return { place:country.place, points:country.points };
  }
});
