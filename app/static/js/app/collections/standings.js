console.log("Loading collections/standings.js");

App.Collections.StandingCollection = Backbone.Collection.extend({
  model: App.Models.Standing,
  url: 'http://bgo.herokuapp.com/scores',
  initialize: function(options) {
    _.bindAll(this, 'get_ranking', 'get_percentage');
  },
  parse: function(response) {
    return response.scores;
  },
  get_ranking: function(country_id) {
    var sorted_standings = _.sortBy(this.models, function(country) { return country.attributes.score * -1; });
    var count = 0;
    var offset = 0;
    var last = 1337;
    
    for (var i = 0; i < sorted_standings.length; i += 1) {
      if (sorted_standings[i].attributes.score < last) {
        count = count + offset + 1;
        offset = 0;
      }
      else {
        offset = offset + 1;
      }
      
      last = sorted_standings[i].attributes.score;
            
      if (sorted_standings[i].attributes.id == country_id) {
        return count;
      }
    }
    
    return -1;
  },
  get_percentage: function(country_id) {
    var sorted_standings = _.sortBy(this.models, function(country) { return country.attributes.score * -1; });
    var max_score = sorted_standings[0].attributes.score;
    var country_score = _.find(this.models, function(country) { return country.attributes.id == country_id; }).attributes.score

    return country_score / max_score * 100.0;    
  }
});
