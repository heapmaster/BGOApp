console.log("Loading collections/matches.js");

App.Collections.MatchCollection = Backbone.Collection.extend({
  model: App.Models.Match,
  url: 'http://www.bgolympics.com/matches',
  initialize: function(options) {
    _.bindAll(this, 'get_matches', 'get_matches_by_country', 'get_matches_by_game');
  },
  parse: function(response) {
    return response.matches;
  },
  get_matches: function() {
    var results = _.sortBy(this.models, function(match) { return match.attributes.id * -1 });
    
    return results;
    
  },
  get_matches_by_country: function(country_id) {
    var results = new Array();
    var sorted_matches = _.sortBy(this.models, function(match) { return match.attributes.id * -1 });
    
    _.each(sorted_matches, function(match) {
      _.each(match.attributes.countries, function(country) {
        if (country.countryId == country_id) {
          results.push(match);
        }
      });
    });
    
    return results;
  },
  get_matches_by_game: function(game_id) {
    var results = new Array();
    var sorted_matches = _.sortBy(this.models, function(match) { return match.attributes.id * -1 });
    
    _.each(sorted_matches, function(match) {
      if (match.attributes.gameId == game_id) {
        results.push(match);
      }
    });
    
    return results;
  }
});
