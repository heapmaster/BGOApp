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
    var matches = new Array();
    var sorted_matches = _.sortBy(this.models, function(match) { return match.attributes.game_id * -1 });
    
    _.each(sorted_matches, function(match) {
      _.each(match.attributes.countries, function(country) {
        if (country.country_id == country_id) {
          matches.push(match);
        }
      });
    });
    
    return matches;
  }
});
