console.log("Loading collections/matches.js");

App.Collections.MatchCollection = Backbone.Collection.extend({
  model: App.Models.Match,
  url: 'http://bgo.herokuapp.com/matches',
  initialize: function(options) {
    _.bindAll(this, 'get_matches_by_country');
  },
  parse: function(response) {
    return response.matches;
  },
  get_matches_by_country: function(country_id) {
    var results = new Array();
    var sorted_matches = _.sortBy(this.models, function(match) { return match.attributes.gameId * -1 });
    
    _.each(sorted_matches, function(match) {
      _.each(match.attributes.countries, function(country) {
        if (country.countryId == country_id) {
          results.push(match);
        }
      });
    });
    
    return results;
  }
});
